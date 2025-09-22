import os
import glob
import re
import json
from slugify import slugify

def main(input_folder):
    """
    Loops through all markdown (.md) files in the input_folder,
    parses each file, and writes the corresponding JSON file into a "json"
    folder located at the same level as the input_folder, with the same base name.
    """
    parent_dir = os.path.dirname(os.path.abspath(input_folder))
    output_folder = os.path.join(parent_dir, "json")
    os.makedirs(output_folder, exist_ok=True)
    
    markdown_files = glob.glob(os.path.join(input_folder, "*.md"))
    if not markdown_files:
        print("No markdown files found in the folder:", input_folder)
        return

    for md_file in markdown_files:
        parsed_data = parse_markdown_file(md_file)
        base_name = os.path.splitext(os.path.basename(md_file))[0]
        output_file = os.path.join(output_folder, f"{base_name}.json")
        with open(output_file, "w", encoding="utf-8") as outfile:
            json.dump(parsed_data, outfile, indent=2, ensure_ascii=False)
        print(f"Processed '{md_file}' -> '{output_file}'")

def parse_markdown_file(filepath):
    """
    Parse a single markdown file and return a dictionary with the following structure:

    {
      "_id": <slugified H1 text>,
      "listData": {
         "id": <slugified H1 text>,
         "date": "2025-01-03 19:14:51.233702",
         "name": <H1 title>,
         "status": "WIP",
         "cat": "NA",
         "slug": <slugified H1 text>,
         "title": <H1 title>,
         "tagline": "NA",
         "description": "NA",
         "db": "2025DB",
         "collection": "QA",
         "data": "NA",
         "cta": " https://www.amazon.co.uk/?tag=fs08-21",
         "year": "2025",
         "image": "NA",
         "content": <text following H1>,
         "topics": <py list of topics extracted from the dedicated "topics" H2, each formatted without duplicate numbering>
      },
      "listItems": [
         {
           "id": <slugified H2 text>,
           "name": <H2 title>,
           "status": "WIP",
           "cat": "NA",
           "slug": <slugified H2 text>,
           "title": <H2 title>,
           "tagline": <first non-empty line under H2 or "NA">,
           "description": <text before "**Key Ideas:**" or "NA">,
           "key-ideas": <list of key ideas (minus trailing image if present), or empty list>,
           "db": "2025DB",
           "collection": "COURSES",
           "data": "GPT4",
           "cta": " https://www.amazon.co.uk/?tag=fs08-21",
           "year": "2025",
           "image": <first markdown image URL if any or "NA">,
           "rank": <starting at 1 among non-topics items>
         },
         ...
      ]
    }
    """
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Process the H1 heading and its following text
    h1_match = re.search(r'^# (.+)$', content, re.MULTILINE)
    if h1_match:
        h1_title = h1_match.group(1).strip()
        _id = slugify(h1_title)
        h1_end = h1_match.end()
        next_heading_match = re.search(r'\n#+ ', content[h1_end:])
        if next_heading_match:
            list_data_text = content[h1_end : h1_end + next_heading_match.start()].strip()
        else:
            list_data_text = content[h1_end:].strip()
        if not list_data_text:
            list_data_text = "NA"
    else:
        h1_title = "NA"
        _id = "NA"
        list_data_text = "NA"

    # Build the listData dictionary with the additional keys
    listData = {
        "id": _id,
        "date": "2025-01-03 19:14:51.233702",
        "name": h1_title if h1_title != "NA" else "NA",
        "status": "WIP",
        "cat": "NA",
        "slug": _id,
        "title": h1_title if h1_title != "NA" else "NA",
        "tagline": "NA",
        "description": "NA",
        "db": "2025DB",
        "collection": "QA",
        "data": "NA",
        "cta": " https://www.amazon.co.uk/?tag=fs08-21",
        "year": "2025",
        "image": "NA",
        "content": list_data_text,
        "topics": []  # to be populated from the dedicated topics H2 section if present
    }

    listItems = []
    topics_list = []
    rank_counter = 1
    h2_matches = list(re.finditer(r'^## (.+)$', content, re.MULTILINE))
    for m in h2_matches:
        title = m.group(1).strip()
        item_slug = slugify(title)
        start = m.end()
        end = h2_matches[h2_matches.index(m)+1].start() if h2_matches.index(m) < len(h2_matches) - 1 else len(content)
        section_text = content[start:end].strip()
        # Get all non-empty lines from this section
        lines = [line.strip() for line in section_text.splitlines() if line.strip()]
        
        # If this H2 heading is "topics", use its lines for topics extraction and skip adding to listItems
        if item_slug == "topics":
            topics_list = lines  # assume each non-empty line is a topic
            continue

        # Otherwise, process as a normal listItem
        tagline = lines[0] if lines else "NA"
        description = "\n".join(lines[1:]) if len(lines) > 1 else "NA"

        # Process description to separate key ideas if present, and convert them into a list
        key_ideas = []
        if "**Key Ideas:**" in description:
            parts = description.split("**Key Ideas:**", 1)
            description = parts[0].strip() or "NA"
            key_ideas_text = parts[1].strip()
            key_ideas = [line.lstrip('-* ').strip() for line in key_ideas_text.splitlines() if line.strip()]
            if key_ideas and re.match(r'^!\[.*\]\(.*\)$', key_ideas[-1]):
                key_ideas.pop()

        # Look for a markdown image pattern: ![alt text](url)
        image_match = re.search(r'!\[.*?\]\((.*?)\)', section_text)
        image = image_match.group(1) if image_match else "NA"

        item = {
            "id": item_slug,
            "name": title,
            "status": "WIP",
            "cat": "NA",
            "slug": item_slug,
            "title": title,
            "tagline": tagline if tagline else "NA",
            "description": description if description else "NA",
            "key-ideas": key_ideas,
            "db": "2025DB",
            "collection": "COURSES",
            "data": "GPT4",
            "cta": " https://www.amazon.co.uk/?tag=fs08-21",
            "year": "2025",
            "image": image if image else "NA",
            "rank": rank_counter
        }
        rank_counter += 1
        listItems.append(item)

    # Process topics_list if present.
    # Remove any existing numbering from each topic line and re-number them.
    if topics_list:
        formatted_topics = []
        for i, topic in enumerate(topics_list):
            # Remove any leading numbering like "1. " or "1) "
            stripped_topic = re.sub(r'^\d+[\.\)]\s*', '', topic)
            formatted_topics.append(f"{i+1}. {stripped_topic}")
        listData["topics"] = formatted_topics
    else:
        listData["topics"] = []

    data = {
        "_id": _id,
        "listData": listData,
        "listItems": listItems
    }
    return data

if __name__ == '__main__':
    # Adjust the folder path as needed
    input_folder = "./markdown_files"  # change this to your actual markdown folder path
    main(input_folder)
