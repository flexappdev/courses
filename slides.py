import sys
import os


# Add the top-level folder to sys.path
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
# import dev.markdown.update_pages as update_pages
import dev.courses_json as courses_json
import dev.courses_update as courses_update
import dev.courses_slides as courses_slides
import dev.courses_swiper as courses_swiper
import dev.courses_google_slides as courses_google_slides





"""
clear && cd ~/cline/ && source venv/bin/activate && cd courses && python3 slides.py
clear && cd ~/cline/ && source venv/bin/activate && cd courses && python3 main.py
clear && cd ~/cline/ && source venv/bin/activate && cd courses && python3 main.py


"""



print("Courses main")


# def create_presenation()

def main():
    # 2025
    input_folder = "_original/"
    output_folder = "updated/"
    slides_folder = "slides/"
    json_folder = "json/"

    # 2024
    # input_folder = "docs/_2024/"
    # output_folder = "docs/2024/"
    # markdown_folder = "docs/2024/"
    # db_name = "2025DB"
    # collection_name = "QA"


    ## COURSES UPDATES
    courses_update.rename_files_in_folder(input_folder)
    # courses_update.print_images_for_each_markdown(input_folder)

    courses_json.main(input_folder)
    # courses_update.copy_to_updated_folder(input_folder, output_folder)
    # courses_update.add_images_to_h2_sections(output_folder)
    # courses_update.add_json_section(output_folder)
    # courses_update.add_h2s_section(output_folder)
    # courses_update.print_missing_images_headers(output_folder)

    
    ## Google Slides Update
    courses_google_slides.main(json_folder)

    ## COURSES SLIDES
    # courses_slides.main(output_folder)
    # courses_update.copy_to_updated_folder(input_folder, output_folder)
    # courses_slides.add_slides_section(output_folder, slides_folder)
    # courses_swiper.add_swiper_section(output_folder, slides_folder)

    # update_pages.copy_to_prod_folder(input_folder, output_folder)
    # update_pages.remove_h2_images_section(output_folder)

    # markdown_to_json.main(output_folder, db_name, collection_name)
    # update_pages.main(markdown_folder, db_name, collection_name)

    # update_pages.add_images(output_folder)
    # Example usage
    # update_pages.move_h2_conclusion_section_to_bottom(output_folder)

    # update_pages.save_to_mongo(output_folder, db_name, collection_name)
    # Example usage
    # check_lad.main(output_folder)
    # print("copy_top_prod_folder completed.")

main()