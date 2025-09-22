from __future__ import print_function
import os
import re
import time
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

def main(output_folder: str):
    """
    Main entry point:
    
    1. Get all Markdown files in output_folder.
    2. For each Markdown file:
         - Parse the markdown into doc_json.
         - Slugify the h1 for a new presentation name.
         - Extract subtitle from the first section (first 100 words of the intro).
         - If a Slides file with that new name already exists, delete it.
         - Duplicate the '2025' template.
         - Populate the duplicated slides:
              * First slide: set title and subtitle.
              * Second slide remains as template.
              * Remove all subsequent slides.
              * For each section, duplicate the template slide, reposition and fill it.
              * Add a final summary table slide.
    3. Authenticate with Google Slides and Drive APIs only once.
    4. Find the '2025' template only once.
    """
    md_files = get_markdown_files(output_folder)
    if not md_files:
        print(f"No Markdown files found in {output_folder}")
        return

    # Authenticate once
    slides_service, drive_service = auth_slides()

    # Find '2025' template once
    template_id = find_2025(drive_service)
    if not template_id:
        print("Template '2025' not found.")
        return

    # Process each markdown file
    for md_file in md_files:
        print(f"Processing markdown file: {md_file}")

        # Parse the markdown file
        doc_json = parse_markdown(md_file)

        # Slugify new presentation name from h1
        h1_title = doc_json.get('h1', 'Untitled')
        new_presentation_name = slugify(str(h1_title))
        print(f"New presentation name = {new_presentation_name}")

        # Extract subtitle from the first section's content (first 100 words)
        subtitle_text = ""
        if doc_json.get('sections'):
            first_section_content = doc_json['sections'][0].get('content', '')
            words = first_section_content.split()
            subtitle_text = " ".join(words[:100])
        
        # If a presentation with this name exists, delete it
        existing_id = find_presentation_by_name(drive_service, new_presentation_name)
        if existing_id:
            print(f"A presentation named '{new_presentation_name}' already exists (ID: {existing_id}). Deleting it...")
            drive_service.files().delete(fileId=existing_id).execute()

        # Duplicate the template presentation
        new_id = duplicate_2025(drive_service, template_id, new_presentation_name)
        if not new_id:
            continue

        # Populate the new slides with markdown data (including subtitle)
        populate_slides(slides_service, new_id, doc_json, subtitle_text)
        print(f"Finished processing markdown file: {md_file}\n")

    print("All markdown files processed.")

def get_markdown_files(output_folder: str):
    """
    Returns a list of .md file paths in the given folder.
    """
    md_files = []
    for filename in os.listdir(output_folder):
        if filename.endswith('.md'):
            md_files.append(os.path.join(output_folder, filename))
    return md_files

def parse_markdown(md_file: str) -> dict:
    """
    Returns a dict with:
    {
       'h1': '... title ...',
       'sections': [
          {
             'title': '...',
             'tagline': '...',
             'content': '...',
             'image_url': '...'
          },
          ...
       ]
    }

    Naively:
      - The first line with # is h1.
      - Lines with ## indicate a new section.
      - The remainder is section content.
    """
    result = {
        'h1': None,
        'sections': []
    }
    with open(md_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    current_section = None
    for line in lines:
        line_strip = line.strip()
        if line_strip.startswith('# '):
            result['h1'] = line_strip[2:].strip()
        elif line_strip.startswith('## '):
            if current_section:
                result['sections'].append(current_section)
            current_section = {
                'title': line_strip[3:].strip(),
                'tagline': '',
                'content': '',
                'image_url': ''
            }
        else:
            if current_section:
                current_section['content'] += line + "\n"

    if current_section:
        result['sections'].append(current_section)
    return result

def auth_slides():
    """
    Authenticates to Google Slides and Drive APIs.
    Returns (slides_service, drive_service).
    """
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

def find_2025(drive_service) -> str:
    """
    Searches for a presentation named '2025'.
    Returns the file ID or None if not found.
    """
    response = drive_service.files().list(
        q="mimeType='application/vnd.google-apps.presentation' and name='2025'",
        pageSize=1
    ).execute()
    files = response.get('files', [])
    if not files:
        return None
    return files[0]['id']

def find_presentation_by_name(drive_service, name: str) -> str:
    """
    Searches for a presentation by exact name.
    Returns the file ID or None if not found.
    """
    query = f"mimeType='application/vnd.google-apps.presentation' and name='{name}'"
    response = drive_service.files().list(q=query, pageSize=1).execute()
    files = response.get('files', [])
    if not files:
        return None
    return files[0]['id']

def duplicate_2025(drive_service, template_id: str, new_name: str) -> str:
    """
    Copies the '2025' presentation, naming it 'new_name'.
    Returns the new file's ID.
    """
    if not template_id:
        print("No template (2025) found.")
        return None
    body = {'name': new_name}
    new_file = drive_service.files().copy(fileId=template_id, body=body).execute()
    return new_file['id']

def populate_slides(slides_service, presentation_id: str, doc_json: dict, subtitle_text: str):
    """
    Populates the presentation as follows:
      - First slide: set title (doc_json['h1']) and subtitle (first 100 words from first section).
      - Second slide is used as a template.
      - Remove all slides after the second.
      - For each section, duplicate the template slide, reposition and fill in content.
      - Add a final summary table slide.
    """
    if not presentation_id:
        return

    # Fetch presentation details
    presentation = slides_service.presentations().get(presentationId=presentation_id).execute()
    slides = presentation.get('slides', [])
    if len(slides) < 2:
        print("Need at least 2 slides in the template (1 for title, 1 for sections).")
        return

    # Populate first slide with title and subtitle
    populate_title_slide(slides_service, presentation_id, slides[0], doc_json.get('h1', 'Untitled'), subtitle_text)

    # Use the second slide as the template for sections
    template_slide_id = slides[1].get('objectId')

    # Remove all slides after the second one
    for slide_obj in slides[2:]:
        delete_request = {
            'deleteObject': {
                'objectId': slide_obj.get('objectId')
            }
        }
        safe_batch_update(slides_service, presentation_id, [delete_request])

    # Process each section: duplicate the template slide, reposition and fill
    sections = doc_json.get('sections', [])
    section_data_list = []  # To build final summary table

    for idx, sec in enumerate(sections, start=1):
        new_slide_id = f"slide_section_{idx}"  # Unique ID for the new slide
        requests = [
            {
                'duplicateObject': {
                    'objectId': template_slide_id,
                    'objectIds': {
                        template_slide_id: new_slide_id
                    }
                }
            },
            {
                'updateSlidesPosition': {
                    'slideObjectIds': [new_slide_id],
                    'insertionIndex': 2 + (idx - 1)
                }
            }
        ]
        safe_batch_update(slides_service, presentation_id, requests)
        fill_section_slide(slides_service, presentation_id, new_slide_id, sec)
        parsed = parse_section_content(sec)
        section_data_list.append({
            'title': sec.get('title', ''),
            'tagline': parsed['tagline'],
            'overview': parsed['overview'],
            'items': parsed['items']
        })

    # Create the final summary table slide
    create_summary_table_slide(slides_service, presentation_id, section_data_list)
    print("Finished populating slides.")

def populate_title_slide(slides_service, presentation_id, slide_obj, title_text: str, subtitle_text: str):
    """
    Populates the title slide with the title and subtitle.
    Assumes the slide contains at least two text shapes.
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
    # Set title in the first text shape
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
    # Set subtitle in the second text shape (if available)
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
    safe_batch_update(slides_service, presentation_id, requests)
    print(f"Populated title slide with: '{title_text}' and subtitle.")

def fill_section_slide(slides_service, presentation_id, slide_id: str, section: dict):
    """
    For a section slide:
      - Finds up to two text shapes.
      - The first shape is used for the section title.
      - The second shape is used for the content (with line breaks removed).
    """
    deck = slides_service.presentations().get(
        presentationId=presentation_id,
        fields="slides(pageElements,objectId)",
    ).execute()

    new_slide = None
    for s in deck.get('slides', []):
        if s.get('objectId') == slide_id:
            new_slide = s
            break

    if not new_slide:
        print(f"Could not find duplicated slide with ID '{slide_id}'")
        return

    page_elements = new_slide.get('pageElements', [])
    text_shape_ids = []
    for elem in page_elements:
        shape = elem.get('shape')
        if shape and 'text' in shape:
            text_shape_ids.append(elem.get('objectId'))
        if len(text_shape_ids) == 2:
            break

    title_text = section.get('title', '')
    raw_content = section.get('content', '')
    content_text = raw_content.replace("\n", " ").strip()

    requests = []
    if text_shape_ids:
        # Set section title in first text shape
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
    if len(text_shape_ids) > 1:
        # Set section content in second text shape
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
    if requests:
        safe_batch_update(slides_service, presentation_id, requests)
        print(f"Populated slide '{slide_id}' with title='{title_text}'")

def parse_section_content(section: dict) -> dict:
    """
    Breaks the section['content'] into:
      - tagline: the first line,
      - overview: text before '**Key Ideas:**',
      - items: text after '**Key Ideas:**' formatted as an ordered list.
    """
    lines = section.get('content', '').strip().splitlines()
    tagline = lines[0].strip() if lines else ''
    body = "\n".join(lines[1:]).strip() if len(lines) > 1 else ''

    overview = body
    items = ''

    if '**Key Ideas:**' in body:
        parts = body.split('**Key Ideas:**', 1)
        overview = parts[0].strip()
        items_raw = parts[1].strip() if len(parts) > 1 else ''
        if items_raw:
            items_list = [line.strip() for line in items_raw.splitlines() if line.strip()]
            if not items_list:
                items_list = [item.strip() for item in items_raw.split(',') if item.strip()]
            items = "\n".join(f"{i+1}. {item}" for i, item in enumerate(items_list))
    return {
        'tagline': tagline,
        'overview': overview,
        'items': items
    }

def create_summary_table_slide(slides_service, presentation_id: str, sections_data: list):
    """
    Adds a new blank slide at the end, creates a table with columns:
      1) Title
      2) Tagline
      3) Overview
      4) Items
    Fills one row per section in sections_data.
    """
    new_slide_id = "final_summary_slide"
    create_slide_request = {
        'createSlide': {
            'objectId': new_slide_id,
            'slideLayoutReference': {
                'predefinedLayout': 'BLANK'
            }
        }
    }
    safe_batch_update(slides_service, presentation_id, [create_slide_request])

    rows = len(sections_data) + 1  # Header row plus data rows
    cols = 4
    table_shape_id = "summary_table_shape"

    create_table_request = {
        'createTable': {
            'objectId': table_shape_id,
            'elementProperties': {
                'pageObjectId': new_slide_id,
                'size': {
                    'width': {'magnitude': 800, 'unit': 'PT'},
                    'height': {'magnitude': 300, 'unit': 'PT'}
                },
                'transform': {
                    'scaleX': 1,
                    'scaleY': 1,
                    'translateX': 50,
                    'translateY': 50,
                    'unit': 'PT'
                }
            },
            'rows': rows,
            'columns': cols
        }
    }
    safe_batch_update(slides_service, presentation_id, [create_table_request])

    headers = ["Title", "Tagline", "Overview", "Items"]
    requests = []
    for col_idx, header_text in enumerate(headers):
        requests.append(set_table_cell_text_request(table_shape_id, 0, col_idx, header_text))

    for row_idx, sec in enumerate(sections_data, start=1):
        requests.append(set_table_cell_text_request(table_shape_id, row_idx, 0, sec.get('title', '')))
        requests.append(set_table_cell_text_request(table_shape_id, row_idx, 1, sec.get('tagline', '')))
        requests.append(set_table_cell_text_request(table_shape_id, row_idx, 2, sec.get('overview', '')))
        requests.append(set_table_cell_text_request(table_shape_id, row_idx, 3, sec.get('items', '')))

    if requests:
        safe_batch_update(slides_service, presentation_id, requests)
    print("Created summary table slide.")

def set_table_cell_text_request(table_object_id, row_idx, col_idx, text):
    """
    Returns a request dict to insert 'text' into the cell at (row_idx, col_idx) of the table.
    """
    return {
        'insertText': {
            'objectId': table_object_id,
            'cellLocation': {
                'rowIndex': row_idx,
                'columnIndex': col_idx
            },
            'insertionIndex': 0,
            'text': text
        }
    }

if __name__ == '__main__':
    main('./some_output_folder')
