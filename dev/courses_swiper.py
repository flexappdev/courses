import os
import re
import io
import requests
from PIL import Image, ImageOps, ImageDraw, ImageFont

def create_image_with_title(header: str, description: str, original_image_url: str, output_path: str) -> None:
    """
    Downloads the original image from original_image_url, overlays the header (centrally)
    and the description (below the header) onto the image with a semi-transparent background,
    and saves the new image to output_path.
    """
    try:
        response = requests.get(original_image_url)
        response.raise_for_status()
    except Exception as e:
        print(f"Failed to download image for header '{header}': {e}")
        return

    try:
        image = Image.open(io.BytesIO(response.content)).convert("RGBA")
        image = ImageOps.exif_transpose(image)
    except Exception as e:
        print(f"Error processing image for header '{header}': {e}")
        return

    draw = ImageDraw.Draw(image)

    # Load fonts for header and description.
    try:
        header_font = ImageFont.truetype("DejaVuSans.ttf", 40)
    except Exception as e:
        print(f"Could not load TTF font for header, falling back to default: {e}")
        header_font = ImageFont.load_default()

    try:
        description_font = ImageFont.truetype("DejaVuSans.ttf", 30)
    except Exception as e:
        print(f"Could not load TTF font for description, falling back to default: {e}")
        description_font = ImageFont.load_default()

    # Calculate text sizes.
    header_width, header_height = draw.textsize(header, font=header_font)
    if description:
        description_width, description_height = draw.textsize(description, font=description_font)
    else:
        description_width, description_height = 0, 0

    gap = 10  # Gap between header and description.
    total_text_height = header_height + (gap + description_height if description else 0)

    # Calculate vertical starting point so that the entire text block is centred.
    block_top = (image.height - total_text_height) // 2

    # Calculate header position (centred horizontally).
    header_x = (image.width - header_width) // 2
    header_y = block_top

    if description:
        description_x = (image.width - description_width) // 2
        description_y = header_y + header_height + gap

    # Determine bounding box for the text block.
    padding = 20
    if description:
        left = min(header_x, description_x)
        right = max(header_x + header_width, description_x + description_width)
        bottom = description_y + description_height
    else:
        left = header_x
        right = header_x + header_width
        bottom = header_y + header_height
    top = block_top
    rect_coords = [left - padding, top - padding, right + padding, bottom + padding]
    draw.rectangle(rect_coords, fill=(0, 0, 0, 128))

    # Draw the header text.
    draw.text((header_x, header_y), header, fill=(255, 255, 255, 255), font=header_font)
    # Draw the description text if provided.
    if description:
        draw.text((description_x, description_y), description, fill=(255, 255, 255, 255), font=description_font)

    image.convert("RGB").save(output_path)
    print(f"Created slide image: {output_path}")

def add_swiper_section(output_folder: str, slides_folder: str) -> None:
    """
    Iterates over Markdown files in the output_folder and adds (or replaces)
    a '## Swiper Slides' section at the bottom of each document.
    
    For each H2 header (excluding common non-slide headers), it extracts the header
    and the first non-empty line following it as the description. It then generates
    a slide image in the slides folder (using create_image_with_title) and builds
    a SwiperJS slider section that utilises these images as background images.
    """
    # Create the slides folder inside the output folder.
    slides_dir = os.path.join(output_folder, slides_folder)
    os.makedirs(slides_dir, exist_ok=True)

    excluded_headers = {"json", "h2s", "table of contents", "slides", "swiper slides"}

    # Iterate over Markdown files.
    for root, _, files in os.walk(output_folder):
        for file_name in files:
            if file_name.lower().endswith(".md"):
                file_path = os.path.join(root, file_name)
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()

                # Remove any existing Swiper Slides section.
                content = re.sub(r"\n## Swiper Slides\s*\n[\s\S]*", "", content)

                lines = content.splitlines()
                slides = []

                # Extract slide data: header and its following description.
                for i, line in enumerate(lines):
                    if line.startswith("## "):
                        header = line[3:].strip()
                        if header.lower() in excluded_headers:
                            continue
                        description = ""
                        # Look ahead for the first non-empty line that doesn't start with "## ".
                        j = i + 1
                        while j < len(lines) and lines[j].strip() == "":
                            j += 1
                        if j < len(lines) and not lines[j].startswith("## "):
                            description = lines[j].strip()
                        slides.append((header, description))

                # Build the Swiper slider HTML.
                swiper_html = """
<!-- Swiper slider -->
<link rel="stylesheet" href="https://unpkg.com/swiper/swiper-bundle.min.css" />
<div class="swiper-container">
  <div class="swiper-wrapper">
"""
                # Generate each slide.
                for header, description in slides:
                    sanitized = re.sub(r"[^\w\s-]", "", header).replace(" ", "-").lower()
                    new_image_filename = f"{sanitized}.jpg"
                    new_image_path = os.path.join(slides_dir, new_image_filename)
                    # Construct the original image URL (adjust if needed).
                    original_image_url = f"https://com25.s3.eu-west-2.amazonaws.com/640/{sanitized}.jpg"
                    
                    # Create the image with title and description.
                    create_image_with_title(header, description, original_image_url, new_image_path)
                    
                    slide_html = f"""
    <div class="swiper-slide" style="background-image: url('{slides_folder}/{new_image_filename}'); background-size: cover; background-position: center;">
      <div class="slide-content" style="padding: 20px; background: rgba(0, 0, 0, 0.5);">
        <h2 style="color: #fff;">{header}</h2>
        <p style="color: #fff;">{description}</p>
      </div>
    </div>
"""
                    swiper_html += slide_html

                swiper_html += """
  </div>
  <!-- Add Pagination -->
  <div class="swiper-pagination"></div>
  <!-- Add Navigation -->
  <div class="swiper-button-prev"></div>
  <div class="swiper-button-next"></div>
</div>
<script src="https://unpkg.com/swiper/swiper-bundle.min.js"></script>
<script>
  var swiper = new Swiper('.swiper-container', {
    loop: true,
    pagination: {
      el: '.swiper-pagination',
      clickable: true,
    },
    navigation: {
      nextEl: '.swiper-button-next',
      prevEl: '.swiper-button-prev',
    },
  });
</script>
"""

                swiper_section = "\n\n## Swiper Slides\n\n" + swiper_html
                updated_content = content + swiper_section

                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(updated_content)

                print(f"Added Swiper Slides section to {file_path}")

# Example usage:
# add_swiper_section("path/to/output_folder", "slides")
