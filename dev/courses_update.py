import os
import shutil
import re



import os
import re

def print_images_for_each_markdown(input_folder):
    """
    Iterates through each Markdown file in the given folder, extracts image paths,
    and prints the image id (filename without extension) for each file.
    
    :param input_folder: Path to the folder containing Markdown files.
    """
    if not os.path.exists(input_folder):
        print(f"Folder '{input_folder}' does not exist.")
        return

    md_files = [f for f in os.listdir(input_folder) if f.endswith('.md')]

    if not md_files:
        print("No Markdown files found in the specified folder.")
        return

    image_pattern = re.compile(r'!\[.*?\]\((.*?)\)')

    for md_file in md_files:
        file_path = os.path.join(input_folder, md_file)
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        images = image_pattern.findall(content)

        print(f"Image ids in {md_file}:")
        if images:
            for img in images:
                # Extract the filename and remove its extension to get the id
                image_id = os.path.splitext(os.path.basename(img))[0].rstrip('-')  # Remove trailing '-'
                image_id = image_id.replace("-", " ")  # Replace all '-' with ' '
                print(image_id)
        else:
            print("No images found.")

        print("-" * 50)


def rename_files_in_folder(input_folder: str) -> None:
    """
    Recursively renames all files in the input_folder. The new filename is converted
    to lowercase, spaces are replaced with dashes, and any special characters (apart from
    letters, numbers, dashes, underscores, and dots) are removed.
    """
    for root, _, files in os.walk(input_folder):
        for old_filename in files:
            # Original file path
            old_filepath = os.path.join(root, old_filename)
            
            # Convert filename to lowercase and replace spaces with dashes
            new_filename = old_filename.lower().replace(' ', '-')
            # Remove any characters that are not a-z, 0-9, dash, underscore or dot.
            new_filename = re.sub(r'[^a-z0-9\-_.]', '', new_filename)
            
            # If the new filename is the same as the old one, skip renaming
            if new_filename == old_filename:
                continue
            
            # Determine the new file path
            new_filepath = os.path.join(root, new_filename)
            
            # Check if a file with the new filename already exists; if so, append a suffix.
            counter = 1
            base_name, ext = os.path.splitext(new_filename)
            while os.path.exists(new_filepath):
                new_filename = f"{base_name}-{counter}{ext}"
                new_filepath = os.path.join(root, new_filename)
                counter += 1
            
            try:
                os.rename(old_filepath, new_filepath)
                print(f"Renamed: {old_filepath} -> {new_filepath}")
            except Exception as e:
                print(f"Error renaming {old_filepath}: {e}")


def copy_to_updated_folder(input_folder: str, output_folder: str) -> None:
    """
    Copies files from input_folder to output_folder, performs basic Markdown validations,
    and records steps in log.md as a ranked list. Also logs stats about input_folder.
    """
    # Ensure output_folder exists
    os.makedirs(output_folder, exist_ok=True)
    
    log_entries = []

    # Walk through the input_folder structure
    for root, dirs, files in os.walk(input_folder):
        # Recreate the folder structure in the output_folder
        relative_path = os.path.relpath(root, input_folder)
        if relative_path == ".":
            relative_path = ""
        dest_path = os.path.join(output_folder, relative_path)
        os.makedirs(dest_path, exist_ok=True)
        
        for file_name in files:
            source_file = os.path.join(root, file_name)
            destination_file = os.path.join(dest_path, file_name)
            
            # Avoid copying a file onto itself
            if os.path.abspath(source_file) == os.path.abspath(destination_file):
                log_entries.append(f"Skipped (same file): {source_file}")
                continue
            
            # If the file is Markdown, perform a basic validation check
            if file_name.lower().endswith(".md"):
                with open(source_file, "r", encoding="utf-8") as md_file:
                    content = md_file.read()
                if "#" not in content:
                    # Log a warning but still copy the file
                    log_entries.append(f"Warning: Markdown file missing heading '#': {source_file}")
                log_entries.append(f"Processed Markdown file: {source_file} -> {destination_file}")
            else:
                log_entries.append(f"Copied file: {source_file} -> {destination_file}")
            
            # Copy the file from the source to the destination
            shutil.copy2(source_file, destination_file)
    
    # Write all log entries to log.md in the output_folder as a ranked list
    log_path = os.path.join(output_folder, "log.md")
    with open(log_path, "w", encoding="utf-8") as log_file:
        for i, entry in enumerate(log_entries, 1):
            log_file.write(f"{i}. {entry}\n")


import os
import re

def add_images_to_h2_sections(output_folder: str) -> None:
    """
    Iterates over all Markdown files in output_folder and, for each H2 header,
    inserts an image immediately after the header. The image URL is generated from
    the header text (using a sanitised version) and references your S3 bucket.
    
    Any previously inserted image lines (with the generated URL pattern) are removed 
    before adding new ones.
    """
    # Define headers to exclude if required.
    excluded_headers = {"json", "h2s", "table of contents", "slides"}

    for root, _, files in os.walk(output_folder):
        for file_name in files:
            if file_name.lower().endswith(".md"):
                file_path = os.path.join(root, file_name)
                with open(file_path, "r", encoding="utf-8") as f:
                    lines = f.readlines()

                new_lines = []
                for line in lines:
                    # Remove previously auto-inserted image lines (they start with "![")
                    # and have our S3 bucket URL pattern.
                    if re.match(r"^!\[.*\]\(https://com25\.s3\.eu-west-2\.amazonaws\.com/640/.*\)", line.strip()):
                        continue

                    new_lines.append(line.rstrip("\n"))
                    
                    # If the line is an H2 header, insert an image line after it.
                    if line.startswith("## "):
                        header_text = line[3:].strip()
                        if header_text.lower() in excluded_headers:
                            continue
                        # Sanitize the header text to generate a filename-friendly string.
                        sanitized = re.sub(r"[^\w\s-]", "", header_text).replace(" ", "-").lower()
                        # Generate the image URL.
                        image_url = f"https://com25.s3.eu-west-2.amazonaws.com/640/{sanitized}.jpg"
                        # Create a Markdown image reference (alt text is just the header text).
                        image_markdown = f"![{header_text}]({image_url})"
                        new_lines.append(image_markdown)

                # Write the updated content back to the file.
                updated_content = "\n".join(new_lines) + "\n"
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(updated_content)

    print("Added images to H2 sections in all Markdown files.")


import os
import re
import json

def add_json_section(output_folder: str) -> None:
    """
    Goes through all Markdown files in the output_folder and adds a '## JSON' section
    at the bottom of each document. This section includes a JSON object listing all sections
    with title, tagline, short description, and image URL.
    """
    for root, _, files in os.walk(output_folder):
        for file_name in files:
            if file_name.lower().endswith(".md"):
                file_path = os.path.join(root, file_name)
                with open(file_path, "r", encoding="utf-8") as md_file:
                    content = md_file.read()

                # Prepare to extract sections
                sections = []
                lines = content.splitlines()
                current_section = None
                tagline = None
                short_desc = []

                for line in lines:
                    # Detect h2 headers (## Section Title)
                    if line.startswith("## "):
                        if current_section is not None:
                            sections.append({
                                "title": current_section,
                                "tagline": tagline if tagline else "",
                                "short_description": " ".join(short_desc).strip(),
                                "image_url": f"https://com25.s3.eu-west-2.amazonaws.com/640/{re.sub(r'[^\w\s-]', '', current_section).replace(' ', '-').lower()}.jpg"
                            })
                        current_section = line[3:].strip()
                        tagline = None
                        short_desc = []
                    # Detect tagline line (ignoring case)
                    elif line.lower().startswith("**tagline**"):
                        tagline_match = re.search(r"\*\*tagline\*\*: _(.+)_", line, re.IGNORECASE)
                        if tagline_match:
                            tagline = tagline_match.group(1).strip()
                    # Collect lines for short description unless it's a Key Points line
                    elif line.strip() and not line.startswith("**Key Points**"):
                        short_desc.append(line.strip())

                # Add the last section if it exists
                if current_section is not None:
                    sections.append({
                        "title": current_section,
                        "tagline": tagline if tagline else "",
                        "short_description": " ".join(short_desc).strip(),
                        "image_url": f"https://com25.s3.eu-west-2.amazonaws.com/640/{re.sub(r'[^\w\s-]', '', current_section).replace(' ', '-').lower()}.jpg"
                    })

                # Create the JSON object for the sections
                json_section = {
                    "slides": sections
                }
                json_output = json.dumps(json_section, indent=4)

                # Append the ## JSON section with the JSON to the document
                updated_content = content + "\n\n## JSON\n\n```json\n" + json_output + "\n```"

                # Write the updated content back to the file
                with open(file_path, "w", encoding="utf-8") as md_file:
                    md_file.write(updated_content)

    print("Added '## JSON' section with JSON to all Markdown files.")

import os
import re

def add_h2s_section(output_folder: str) -> None:
    """
    Goes through all Markdown files in the output_folder and adds (or replaces) a '## H2S' section
    at the bottom of each document. This section lists all H2 headers present in the document,
    formatted within a code block.
    """
    for root, _, files in os.walk(output_folder):
        for file_name in files:
            if file_name.lower().endswith(".md"):
                file_path = os.path.join(root, file_name)
                with open(file_path, "r", encoding="utf-8") as md_file:
                    content = md_file.read()
                
                # Remove any existing "## H2S" section to avoid duplication
                content = re.sub(r"\n## H2S\s*\n```[\s\S]*?```", "", content)
                
                # Extract all H2 headers (ignore any header that might be "## H2S")
                lines = content.splitlines()
                h2_headers = []
                for line in lines:
                    if line.startswith("## ") and not line.startswith("## H2S"):
                        header_text = line[3:].strip()
                        h2_headers.append(header_text)
                
                # Create a code block with the extracted H2 headers
                h2s_block = "```\n" + "\n".join(h2_headers) + "\n```"
                
                # Append the new "## H2S" section with the code block to the document
                updated_content = content + "\n\n## H2S\n" + h2s_block
                
                with open(file_path, "w", encoding="utf-8") as md_file:
                    md_file.write(updated_content)
    
    print("Added '## H2S' section with all H2 headers to all Markdown files.")

import os
import re

def print_missing_images_headers(output_folder: str) -> None:
    """
    Scans all Markdown files in the output_folder and, for each missing image (i.e. an image
    referenced via Markdown syntax that does not exist on disc), records the most recent H2 header.
    At the end, it prints a code block containing the unique list of H2 headers where missing images were found.
    
    Only lines starting with "## " (apart from a header like "## Missing Images") are considered.
    Remote image URLs are ignored.
    If a missing image is encountered before any H2 header is defined, the filename is used as a default header.
    """
    missing_headers = []
    
    for root, _, files in os.walk(output_folder):
        for file_name in files:
            if file_name.lower().endswith(".md"):
                file_path = os.path.join(root, file_name)
                with open(file_path, "r", encoding="utf-8") as md_file:
                    lines = md_file.readlines()
                
                current_header = None
                default_header = f"File: {file_name}"
                
                for line in lines:
                    # Update current_header if a H2 header is encountered (ignoring "## Missing Images")
                    header_match = re.match(r"^## (?!Missing Images)(.+)$", line)
                    if header_match:
                        current_header = header_match.group(1).strip()
                    
                    # Look for Markdown image references in the line
                    for img_match in re.finditer(r'!\[.*?\]\((.*?)\)', line):
                        img_ref = img_match.group(1).strip('\'"')
                        # Ignore remote URLs
                        if img_ref.startswith("http://") or img_ref.startswith("https://") or img_ref.startswith("//"):
                            continue
                        # Use the Markdown file's directory as the base for the image path
                        image_path = os.path.join(os.path.dirname(file_path), img_ref)
                        if not os.path.exists(image_path):
                            # If there's no current header, use the file name as the default header
                            missing_headers.append(current_header if current_header else default_header)
    
    # Remove duplicates while preserving order
    unique_headers = list(dict.fromkeys(missing_headers))
    
    if unique_headers:
        print("```\n" + "\n".join(unique_headers) + "\n```")
    else:
        print("```\nNo missing images found.\n```")
    
# Example usage:
# print_missing_images_headers("/path/to/your/output_folder")
