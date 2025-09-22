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
    Parse a single markdown file and return a dictionary.
    """
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove bold markers ("**") from text
    content = re.sub(r'\*\*(.*?)\*\*', r'\1', content)

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

    listData = {
        "id": _id,
        "name": h1_title,
        "content": list_data_text
    }

    return {"_id": _id, "listData": listData}

if __name__ == '__main__':
    input_folder = "./markdown_files"  # change this to your actual markdown folder path
    main(input_folder)
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
    Parses a markdown file and extracts structured data including H1, H2 sections, topics, and key details.
    """
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Process H1 heading and its following text
    h1_match = re.search(r'^# (.+)$', content, re.MULTILINE)
    if h1_match:
        h1_title = h1_match.group(1).strip()
        _id = slugify(h1_title)
        h1_end = h1_match.end()
        next_heading_match = re.search(r'\n#+ ', content[h1_end:])
        list_data_text = content[h1_end : h1_end + next_heading_match.start()].strip() if next_heading_match else content[h1_end:].strip()
    else:
        h1_title, _id, list_data_text = "NA", "NA", "NA"

    # Initialize listData dictionary
    listData = {
        "id": _id,
        "date": "2025-01-03 19:14:51.233702",
        "name": h1_title,
        "status": "WIP",
        "cat": "NA",
        "slug": _id,
        "title": h1_title,
        "tagline": "NA",
        "description": "NA",
        "db": "2025DB",
        "collection": "QA",
        "data": "NA",
        "cta": " https://www.amazon.co.uk/?tag=fs08-21",
        "year": "2025",
        "image": "NA",
        "content": list_data_text,
        "topics": []
    }

    listItems, topics_list = [], []
    rank_counter = 1
    h2_matches = list(re.finditer(r'^## (.+)$', content, re.MULTILINE))
    
    for i, m in enumerate(h2_matches):
        title = m.group(1).strip()
        item_slug = slugify(title)
        start = m.end()
        end = h2_matches[i+1].start() if i < len(h2_matches) - 1 else len(content)
        section_text = content[start:end].strip()
        lines = [line.strip() for line in section_text.splitlines() if line.strip()]
        
        if item_slug == "topics":
            topics_list = lines
            continue

        tagline = lines[0] if lines else "NA"
        description = "\n".join(lines[1:]) if len(lines) > 1 else "NA"
        
        key_ideas = []
        if "**Key Ideas:**" in description:
            parts = description.split("**Key Ideas:**", 1)
            description = parts[0].strip() or "NA"
            key_ideas_text = parts[1].strip()
            key_ideas = [line.lstrip('-* ').strip() for line in key_ideas_text.splitlines() if line.strip()]
            if key_ideas and re.match(r'^!\[.*\]\(.*\)$', key_ideas[-1]):
                key_ideas.pop()

        image_match = re.search(r'!\[.*?\]\((.*?)\)', section_text)
        image = image_match.group(1) if image_match else "NA"

        item = {
            "id": item_slug,
            "name": title,
            "status": "WIP",
            "cat": "NA",
            "slug": item_slug,
            "title": title,
            "tagline": tagline,
            "description": description,
            "key-ideas": key_ideas,
            "db": "2025DB",
            "collection": "COURSES",
            "data": "GPT4",
            "cta": " https://www.amazon.co.uk/?tag=fs08-21",
            "year": "2025",
            "image": image,
            "rank": rank_counter
        }
        rank_counter += 1
        listItems.append(item)

    if topics_list:
        formatted_topics = [f"{i+1}. {re.sub(r'^\d+[\.\)]\s*', '', topic)}" for i, topic in enumerate(topics_list)]
        listData["topics"] = formatted_topics

    return {"_id": _id, "listData": listData, "listItems": listItems}

if __name__ == '__main__':
    input_folder = "./markdown_files"
    main(input_folder)
