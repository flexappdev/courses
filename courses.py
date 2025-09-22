import streamlit as st

st.set_page_config(
    page_title="English Teacher Course",
    page_icon=":books:",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Sidebar Menu
with st.sidebar:
    st.title("Course Menu")
    menu_selection = st.radio(
        "Go to",
        ("Courses", "README", "Slides", "Images", "Audio", "Video", "DOCAI"),
    )

# Content based on menu selection
if menu_selection == "Courses":
    st.title("Courses Overview")
    st.write("Welcome to the English Teacher courses!")
    st.write("This courses covers various aspects of teaching English.")
    import os
    st.write(f"Current working directory: {os.getcwd()}")
    st.write("Courses in /courses/json:")
    import os
    import json
    json_files = os.listdir("courses/json")
    for i, file in enumerate(json_files):
        st.markdown(f"{i+1}. <span style='color: var(--primary);'>{file}</span>", unsafe_allow_html=True)
    if json_files:
        try:
            with open(f"courses/json/{json_files[0]}", "r") as f:
                data = json.load(f)
            st.json(data)
        except json.JSONDecodeError:
            st.error(f"Error decoding JSON file: {json_files[0]}")

elif menu_selection == "README":
    st.title("README")
    with open("courses/README.md", "r") as f:
        readme_content = f.read()
    st.markdown(readme_content)

elif menu_selection == "Slides":
    st.title("Slides")
    st.write("Content related to slides will be displayed here.")
    # Add slide content here

elif menu_selection == "Images":
    st.title("Images")
    import os
    image_dir = "IMAGES/images"
    image_files = os.listdir(image_dir)
    cols = st.columns(4)  # Display in 4 columns
    for i, image_file in enumerate(image_files[:100]):
        with cols[i % 4]:
            st.image(os.path.join(image_dir, image_file), caption=image_file)

elif menu_selection == "Audio":
    st.title("Audio")
    st.write("Content related to audio will be displayed here.")
    # Add audio content here

elif menu_selection == "Video":
    st.title("Video")
    st.write("Content related to video will be displayed here.")
    # Add video content here

elif menu_selection == "DOCAI":
    st.title("DOCAI")
    with open("courses/gpts/DOCAI.md", "r") as f:
        docai_content = f.read()
    st.markdown(docai_content)
