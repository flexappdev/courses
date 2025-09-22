from __future__ import print_function
import os
import time
import json
import re
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
from google.oauth2.credentials import Credentials
from slugify import slugify
from googleapiclient.errors import HttpError

CLIENT_SECRET_FILE = 'dev/credentials.json'
SCOPES = [
    'https://www.googleapis.com/auth/presentations',
    'https://www.googleapis.com/auth/drive'
]
TOKEN_FILE = 'token.json'
TEMPLATE_NAME = "2025-TEMPLATE"  # Template presentation name

def safe_batch_update(service, presentation_id, requests, max_retries=5):
    """
    Executes a batchUpdate with exponential backoff in case of rate limit errors.
    """
    retries = 0
    while retries < max_retries:
        try:
            service.presentations().batchUpdate(
                presentationId=presentation_id,
                body={'requests': requests}
            ).execute()
            return
        except HttpError as e:
            if e.resp.status == 429:
                wait_time = 2 ** retries
                print(f"Rate limit exceeded, waiting {wait_time} seconds before retrying...")
                time.sleep(wait_time)
                retries += 1
            else:
                raise
    print("Max retries exceeded.")

def main(json_folder: str):
    """
    Main entry point:
    
    1. Loads the first JSON file from the folder.
    2. Creates a new presentation from the template (TEMPLATE_NAME).
    3. Populates:
         - Slide 1 (Title Slide) with course_title (listData.title) and course_subtitle (listData.tagline or first few words of listData.content if tagline is "NA").
         - Slides 2+ for each listItem in listItems:
              • section_title → listItems.title
              • section_content → consists of listItems.tagline (italicised on the first line), followed by listItems.description,
                and then "Key ideas:" with the ranked key ideas on separate lines.
    4. Authenticates with Google Slides and Drive APIs only once.
    5. Finds the template presentation using TEMPLATE_NAME.
    """
    json_files = get_json_files(json_folder)
    if not json_files:
        print(f"No JSON files found in {json_folder}")
        return

    # Process only the first JSON file
    for json_file in json_files[0:]:
        print(f"Processing JSON file: {json_file}")
        doc_json = parse_json(json_file)

        list_data = doc_json.get("listData", {})
        # New presentation name from listData.title
        course_title = list_data.get("title", "Untitled")
        new_presentation_name = slugify(str(course_title))
        print(f"New presentation name = {new_presentation_name}")

        # Course subtitle: use listData.tagline unless it is "NA", then use first few words of listData.content
        course_subtitle = list_data.get("tagline", "")
        if course_subtitle.strip().upper() == "NA":
            content = list_data.get("content", "")
            course_subtitle = " ".join(content.split()[:10])  # first 10 words

        # Authenticate once
        slides_service, drive_service = auth_slides()

        # Find the template presentation using TEMPLATE_NAME
        template_id = find_template(drive_service)
        if not template_id:
            print(f"Template '{TEMPLATE_NAME}' not found.")
            return

        # If a presentation with this name exists, delete it
        existing_id = find_presentation_by_name(drive_service, new_presentation_name)
        if existing_id:
            print(f"A presentation named '{new_presentation_name}' already exists (ID: {existing_id}). Deleting it...")
            drive_service.files().delete(fileId=existing_id).execute()

        # Duplicate the template presentation
        new_id = duplicate_template(drive_service, template_id, new_presentation_name)
        if not new_id:
            continue

        # Populate the new presentation using the JSON data
        populate_slides(slides_service, new_id, doc_json, course_title, course_subtitle)
        print(f"Finished processing JSON file: {json_file}\n")
    print("All JSON files processed.")

def get_json_files(json_folder: str):
    """Returns a list of .json file paths in the given folder."""
    return [os.path.join(json_folder, f) for f in os.listdir(json_folder) if f.endswith('.json')]

def parse_json(json_file: str) -> dict:
    """Loads and returns the JSON data from the given file."""
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data

def auth_slides():
    """Authenticates to Google Slides and Drive APIs. Returns (slides_service, drive_service)."""
    creds = None
    if os.path.exists(TOKEN_FILE):
        creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)
    if not creds:
        flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
            CLIENT_SECRET_FILE, SCOPES
        )
        creds = flow.run_local_server(port=0)
        with open(TOKEN_FILE, 'w') as token:
            token.write(creds.to_json())
    slides_service = googleapiclient.discovery.build('slides', 'v1', credentials=creds)
    drive_service = googleapiclient.discovery.build('drive', 'v3', credentials=creds)
    return slides_service, drive_service

def find_template(drive_service) -> str:
    """Searches for a presentation with the name specified in TEMPLATE_NAME."""
    query = f"mimeType='application/vnd.google-apps.presentation' and name='{TEMPLATE_NAME}'"
    response = drive_service.files().list(q=query, pageSize=1).execute()
    files = response.get('files', [])
    return files[0]['id'] if files else None

def find_presentation_by_name(drive_service, name: str) -> str:
    """Searches for a presentation by exact name."""
    query = f"mimeType='application/vnd.google-apps.presentation' and name='{name}'"
    response = drive_service.files().list(q=query, pageSize=1).execute()
    files = response.get('files', [])
    return files[0]['id'] if files else None

def duplicate_template(drive_service, template_id: str, new_name: str) -> str:
    """Copies the template presentation, naming it 'new_name'."""
    if not template_id:
        print("No template found.")
        return None
    body = {'name': new_name}
    new_file = drive_service.files().copy(fileId=template_id, body=body).execute()
    return new_file.get('id')

def populate_slides(slides_service, presentation_id: str, doc_json: dict, course_title: str, course_subtitle: str):
    """
    Populates the presentation as follows:
      - Slide 1: Set course_title and course_subtitle from listData.
      - For the section slides:
            Use slide 2 of the template as the section slide template.
            For the first listItem, reuse slide 2; for subsequent items, duplicate slide 2.
            Then fill each with:
              • section_title from listItems.title
              • section_content composed of listItems.tagline (italicised on the first line), followed by listItems.description,
                and then "Key ideas:" with the ranked key ideas on separate lines.
    """
    # Get presentation details
    presentation = slides_service.presentations().get(presentationId=presentation_id).execute()
    slides = presentation.get('slides', [])
    if len(slides) < 2:
        print("The template must have at least 2 slides (one for title and one for section template).")
        return

    # Slide 1: Populate title slide
    populate_title_slide(slides_service, presentation_id, slides[0], course_title, course_subtitle)

    # Use slide 2 as the section slide template
    section_template_id = slides[1].get('objectId')

    # We'll reuse slide 2 for the first list item and duplicate for additional items.
    list_items = doc_json.get("listItems", [])
    print(f"Debug: Found {len(list_items)} list items.")
    if not list_items:
        print("No list items found; nothing more to populate.")
        return

    # Fill slide 2 with the first list item
    fill_section_slide(slides_service, presentation_id, section_template_id, list_items[0])
    # For list items 2+, duplicate slide 2 and fill
    for idx, section in enumerate(list_items[1:], start=2):
        new_slide_id = f"slide_section_{idx}"
        requests = [
            {
                'duplicateObject': {
                    'objectId': section_template_id,
                    'objectIds': {
                        section_template_id: new_slide_id
                    }
                }
            },
            {
                'updateSlidesPosition': {
                    'slideObjectIds': [new_slide_id],
                    'insertionIndex': idx
                }
            }
        ]
        safe_batch_update(slides_service, presentation_id, requests)
        fill_section_slide(slides_service, presentation_id, new_slide_id, section)
    print("Finished populating slides.")

def populate_title_slide(slides_service, presentation_id, slide_obj, title_text: str, subtitle_text: str):
    """
    Populates Slide 1 with course title and course subtitle.
    Assumes the slide has at least two text shapes.
    The subtitle (tagline) is set in italic.
    """
    page_elements = slide_obj.get('pageElements', [])
    text_shape_ids = []
    for elem in page_elements:
        shape_data = elem.get('shape')
        if shape_data and 'text' in shape_data:
            text_shape_ids.append(elem.get('objectId'))
        if len(text_shape_ids) == 2:
            break

    if not text_shape_ids:
        print("No text shapes found on the title slide.")
        return

    requests = []
    # First text shape: course title
    requests.append({
        'deleteText': {
            'objectId': text_shape_ids[0],
            'textRange': {'type': 'ALL'}
        }
    })
    requests.append({
        'insertText': {
            'objectId': text_shape_ids[0],
            'insertionIndex': 0,
            'text': title_text
        }
    })
    # Second text shape: course subtitle (tagline)
    if len(text_shape_ids) > 1:
        requests.append({
            'deleteText': {
                'objectId': text_shape_ids[1],
                'textRange': {'type': 'ALL'}
            }
        })
        requests.append({
            'insertText': {
                'objectId': text_shape_ids[1],
                'insertionIndex': 0,
                'text': subtitle_text
            }
        })
        # Set the entire subtitle text to italic
        requests.append({
            'updateTextStyle': {
                'objectId': text_shape_ids[1],
                'style': {'italic': True},
                'textRange': {'type': 'ALL'},
                'fields': 'italic'
            }
        })
    safe_batch_update(slides_service, presentation_id, requests)
    print(f"Populated title slide with '{title_text}' and subtitle.")

def fill_section_slide(slides_service, presentation_id, slide_id: str, section: dict):
    """
    For a section slide:
      - The first text shape displays section_title (from listItems.title).
      - The second text shape displays section content composed of:
            • listItems.tagline (italicised on the first line),
            • followed by listItems.description,
            • then "Key ideas:" with the ranked key ideas on separate lines.
    """
    # Re-fetch the slide to get up-to-date page elements
    deck = slides_service.presentations().get(
        presentationId=presentation_id,
        fields="slides(pageElements,objectId)"
    ).execute()
    new_slide = None
    for s in deck.get('slides', []):
        if s.get('objectId') == slide_id:
            new_slide = s
            break
    if not new_slide:
        print(f"Could not find slide with ID '{slide_id}'")
        return

    page_elements = new_slide.get('pageElements', [])
    text_shape_ids = []
    for elem in page_elements:
        shape = elem.get('shape')
        if shape and 'text' in shape:
            text_shape_ids.append(elem.get('objectId'))
        if len(text_shape_ids) == 2:
            break

    # Build section content:
    section_title = section.get("title", "")
    section_tagline = section.get("tagline", "")
    section_description = section.get("description", "")
    key_ideas = section.get("key-ideas", [])
    key_ideas_text = ""
    if key_ideas:
        # Remove any pre-existing numbering from each idea.
        cleaned_ideas = [re.sub(r'^\d+\.\s*', '', idea) for idea in key_ideas]
        # Build a numbered list with each idea on a separate line.
        ranked_key_ideas = "\n".join([f"{i+1}. {idea}" for i, idea in enumerate(cleaned_ideas)])
        key_ideas_text = "Key ideas:\n" + ranked_key_ideas

    # Combine content with tagline at the top.
    content_parts = [section_tagline, section_description, key_ideas_text]
    content_text = "\n".join([part for part in content_parts if part]).strip()

    requests = []
    if text_shape_ids:
        # Update first text shape with section title.
        requests.append({
            'deleteText': {
                'objectId': text_shape_ids[0],
                'textRange': {'type': 'ALL'}
            }
        })
        requests.append({
            'insertText': {
                'objectId': text_shape_ids[0],
                'insertionIndex': 0,
                'text': section_title
            }
        })
    else:
        print(f"Debug: No text shapes found on slide {slide_id} for section title.")

    if len(text_shape_ids) > 1:
        # Update second text shape with section content.
        requests.append({
            'deleteText': {
                'objectId': text_shape_ids[1],
                'textRange': {'type': 'ALL'}
            }
        })
        requests.append({
            'insertText': {
                'objectId': text_shape_ids[1],
                'insertionIndex': 0,
                'text': content_text
            }
        })
        # If a tagline exists, set only the first line (the tagline) to italic.
        if section_tagline:
            tagline_length = len(section_tagline)
            requests.append({
                'updateTextStyle': {
                    'objectId': text_shape_ids[1],
                    'style': {'italic': True},
                    'textRange': {'type': 'FIXED_RANGE', 'startIndex': 0, 'endIndex': tagline_length},
                    'fields': 'italic'
                }
            })
    else:
        print(f"Debug: No second text shape found on slide {slide_id} for section content.")

    if requests:
        safe_batch_update(slides_service, presentation_id, requests)
        print(f"Populated section slide '{slide_id}' with title '{section_title}'.")

if __name__ == '__main__':
    main('./json')
