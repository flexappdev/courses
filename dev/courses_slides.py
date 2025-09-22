import os
import re
import io
import requests
import textwrap
from PIL import Image, ImageDraw, ImageFont

def create_image_with_title(header: str, original_image_url: str, output_path: str,
                            tagline: str = None, overview: str = None, key_ideas: list = None) -> bool:
    """
    Downloads the original image from original_image_url and draws a semi‑transparent overlay at the top containing:
      - The header (centred, large font)
      - An optional tagline (centred, just below the header)
      - A main content area split into two columns:
          * Left column (with extra horizontal padding): overview text (left‑aligned)
          * Right column (with extra horizontal padding): key ideas (with "Key Ideas:" at the top and bullet points below, left‑aligned)
    The resulting image is saved to output_path.
    Returns True if successful, False otherwise.
    """
    try:
        response = requests.get(original_image_url)
        response.raise_for_status()
    except Exception as e:
        print(f"Failed to download image for header '{header}': {e}")
        return False

    try:
        image = Image.open(io.BytesIO(response.content)).convert("RGBA")
    except Exception as e:
        print(f"Error processing image for header '{header}': {e}")
        return False

    draw = ImageDraw.Draw(image)
    padding = 10  # general vertical padding

    # Define font sizes and load fonts – adjust paths as needed
    header_font_size = 60
    tagline_font_size = 40
    content_font_size = 30

    try:
        header_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", header_font_size)
    except IOError:
        header_font = ImageFont.load_default()
        print("Warning: TTF font not found for header, using default font.")

    try:
        tagline_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", tagline_font_size)
    except IOError:
        tagline_font = ImageFont.load_default()
        print("Warning: TTF font not found for tagline, using default font.")

    try:
        content_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", content_font_size)
    except IOError:
        content_font = ImageFont.load_default()
        print("Warning: TTF font not found for content, using default font.")

    # --- Compute header and tagline areas ---
    header_width, header_height = draw.textsize(header, font=header_font)
    header_box_height = header_height + 2 * padding

    if tagline:
        tagline_text = tagline  # assumed already cleaned
        tagline_width, tagline_height = draw.textsize(tagline_text, font=tagline_font)
        tagline_box_height = tagline_height + 2 * padding
    else:
        tagline_box_height = 0

    # --- Compute main content area (split into two columns with extra horizontal padding) ---
    total_width = image.width
    # Define extra horizontal margin for the columns so text doesn't reach the very edge.
    column_margin = 20
    left_column_x = column_margin
    left_column_width = (total_width // 2) - 2 * column_margin
    right_column_x = (total_width // 2) + column_margin
    right_column_width = (total_width // 2) - 2 * column_margin

    line_height = content_font.getsize("A")[1]
    line_spacing = 4

    # Wrap overview text for the left column.
    if overview:
        avg_char_width = content_font.getsize("A")[0]
        max_chars_overview = max(1, int(left_column_width / avg_char_width))
        overview_lines = textwrap.wrap(overview, width=max_chars_overview)
    else:
        overview_lines = []

    # Prepare key ideas for the right column.
    key_lines = []
    if key_ideas:
        key_lines.append("Key Ideas:")
        avg_char_width = content_font.getsize("A")[0]
        max_chars_key = max(1, int(right_column_width / avg_char_width))
        for idea in key_ideas:
            idea_clean = idea.lstrip("- ").strip()
            wrapped = textwrap.wrap(idea_clean, width=max_chars_key - 2)
            if wrapped:
                wrapped[0] = "- " + wrapped[0]
                for i in range(1, len(wrapped)):
                    wrapped[i] = "  " + wrapped[i]
            else:
                wrapped = ["- " + idea_clean]
            key_lines.extend(wrapped)
    else:
        key_lines = []

    overview_height = (len(overview_lines) * line_height + (len(overview_lines) - 1) * line_spacing) if overview_lines else 0
    key_height = (len(key_lines) * line_height + (len(key_lines) - 1) * line_spacing) if key_lines else 0
    main_content_height = max(overview_height, key_height) + 2 * padding

    # Total overlay height is header + tagline + main content.
    total_overlay_height = header_box_height + tagline_box_height + main_content_height

    # Create a semi‑transparent overlay for the text background.
    overlay = Image.new("RGBA", (image.width, total_overlay_height), (0, 0, 0, 150))
    image.paste(overlay, (0, 0), overlay)

    # --- Draw the header and tagline ---
    header_text_x = (total_width - header_width) // 2
    header_text_y = padding
    draw.text((header_text_x, header_text_y), header, fill=(255, 255, 255, 255), font=header_font)

    current_y = header_box_height
    if tagline:
        tagline_text_x = (total_width - tagline_width) // 2
        tagline_text_y = current_y + padding
        draw.text((tagline_text_x, tagline_text_y), tagline_text, fill=(255, 255, 255, 255), font=tagline_font)
    current_y += tagline_box_height

    # --- Draw main content in two columns ---
    main_content_top = current_y + padding

    # Left column (overview)
    y_overview = main_content_top
    for line in overview_lines:
        draw.text((left_column_x, y_overview), line, fill=(255, 255, 255, 255), font=content_font)
        y_overview += line_height + line_spacing

    # Right column (key ideas)
    y_key = main_content_top
    for line in key_lines:
        draw.text((right_column_x, y_key), line, fill=(255, 255, 255, 255), font=content_font)
        y_key += line_height + line_spacing

    try:
        image.convert("RGB").save(output_path)
        print(f"Created slide image: {output_path}")
    except Exception as e:
        print(f"Error saving image for header '{header}': {e}")
        return False

    return True

def extract_sections_from_markdown(content: str):
    """
    Extracts sections from Markdown content.
    Each section starts with '## ' and includes the header and the subsequent lines until the next header.
    Returns a list of dictionaries with keys 'header' and 'lines'.
    """
    sections = []
    current_section = None
    for line in content.splitlines():
        if line.startswith("## "):
            if current_section is not None:
                sections.append(current_section)
            header = line[3:].strip()
            current_section = {"header": header, "lines": []}
        else:
            if current_section is not None:
                current_section["lines"].append(line)
    if current_section is not None:
        sections.append(current_section)
    return sections

def parse_section_content(lines):
    """
    Parses a section's lines to extract:
      - Tagline: the first non‑empty line enclosed in '**'
      - Overview: the text block following the tagline up to the '**Key Ideas:**' marker
      - Key ideas: bullet points (lines starting with '-' after the '**Key Ideas:**' marker)
    Ignores any image markdown lines.
    Returns a tuple: (tagline, overview, key_ideas)
    """
    tagline = None
    overview_lines = []
    key_ideas = []
    state = "overview"  # Start in the overview state

    for line in lines:
        line_stripped = line.strip()
        if line_stripped.startswith("!["):
            continue
        if not line_stripped:
            continue

        if line_stripped.startswith("**Key Ideas:**"):
            state = "key_ideas"
            continue

        if state == "overview" and tagline is None and line_stripped.startswith("**") and line_stripped.endswith("**"):
            tagline = line_stripped.strip("*").strip()
            continue

        if state == "overview":
            overview_lines.append(line_stripped)
        elif state == "key_ideas":
            if line_stripped.startswith("-"):
                key_ideas.append(line_stripped)
            else:
                key_ideas.append(line_stripped)

    overview = " ".join(overview_lines).strip() if overview_lines else None
    return tagline, overview, key_ideas

def add_slides_section(output_folder: str, slides_folder: str) -> None:
    """
    Processes all Markdown files in output_folder, and for each H2 section:
      - Extracts the header (slide title), tagline, overview, and key ideas.
      - Generates a new slide image using an image fetched from the S3 bucket (using the 1280 folder).
      - Ignores any in‑document image markdown.
    A '## Slides' section is then appended to each Markdown file, displaying the generated slide images.
    At the end, a list of all headers for which images were missing is printed.
    """
    slides_dir = os.path.join(output_folder, slides_folder)
    os.makedirs(slides_dir, exist_ok=True)

    excluded_headers = {"json", "h2s", "table of contents", "slides"}
    missing_images = []

    for root, _, files in os.walk(output_folder):
        for file_name in files:
            if file_name.lower().endswith(".md"):
                file_path = os.path.join(root, file_name)
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()

                content = re.sub(r"\n## Slides\s*\n[\s\S]*", "", content)
                sections = extract_sections_from_markdown(content)
                slides_html = '<div style="display: flex; flex-wrap: wrap;">\n'
                for section in sections:
                    header = section["header"]
                    if header.lower() in excluded_headers:
                        continue

                    tagline, overview, key_ideas = parse_section_content(section["lines"])
                    sanitized = re.sub(r"[^\w\s-]", "", header).replace(" ", "-").lower()
                    new_image_filename = f"{sanitized}.jpg"
                    new_image_path = os.path.join(slides_dir, new_image_filename)
                    original_image_url = f"https://com25.s3.eu-west-2.amazonaws.com/1280/{sanitized}.jpg"

                    success = create_image_with_title(header, original_image_url, new_image_path,
                                                      tagline=tagline, overview=overview, key_ideas=key_ideas)
                    if not success:
                        missing_images.append(header)

                    slides_html += (
                        '  <div style="margin: 10px; display: inline-block;">\n'
                        f'    <img src="{slides_folder}/{new_image_filename}" alt="{header}" '
                        'style="max-width: 150px; display: block;">\n'
                        "  </div>\n"
                    )
                slides_html += "</div>"

                slides_section = "\n\n## Slides\n\n" + slides_html
                updated_content = content + slides_section

                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(updated_content)

    print("Added '## Slides' section with new images in the slides folder to all Markdown files.")
    if missing_images:
        print("\nMissing images for the following headers:")
        for header in missing_images:
            print(header)
    else:
        print("\nNo missing images detected.")

# Example usage:
# add_slides_section("output_folder_path", "slides_folder")
