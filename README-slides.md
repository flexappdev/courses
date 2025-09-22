# Presentation a Day - FastAPI Version 2

## Introduction
This project is a FastAPI app designed to generate Google Slides presentations from JSON objects. It features:
- A home endpoint for authentication.
- A generate endpoint to create presentations from JSON files.

## Table of Contents
1. [Brainstorming](#brainstorming)
2. [Key Features](#key-features)
3. [Backend Setup](#backend-setup)
4. [Frontend Setup](#frontend-setup)
5. [Publishing and Testing](#publishing-and-testing)

## Brainstorming
The initial idea was to create a simple app that generates presentations from JSON objects.

## Key Features
- **Home Endpoint:** Authenticates with Google Slides.
- **Generate Endpoint:** Lists JSON files, allows selection, and generates slides.

## Backend Setup
1. Create `app.py`:
   ```python
   from fastapi import FastAPI, HTTPException
   from pydantic import BaseModel
   import os, json

   app = FastAPI()

   class MarkdownInput(BaseModel):
       content: str

   @app.get("/")
   def home():
       return {"message": "Google Slides authentication page"}

   @app.get("/json-objects")
   def get_json_objects():
       json_folder = 'path/to/json/files'
       json_files = [f for f in os.listdir(json_folder) if f.endswith('.json')]
       json_objects = []
       for file in json_files:
           with open(os.path.join(json_folder, file), 'r') as f:
               json_objects.append(json.load(f))
       return json_objects

   @app.post("/generate")
   def generate_presentation(input: MarkdownInput):
       # Placeholder logic for presentation generation
       return {"message": "Presentation generated"}
   ```

## Frontend Setup
1. **Directory Structure:**
   ```
   your_project/
   ├── app.py
   ├── templates/
   │   ├── base.html
   │   ├── home.html
   │   └── generate.html
   └── static/
       ├── css/
       └── js/
   ```

2. **Base Template (`base.html`):**
   ```html
   <!DOCTYPE html>
   <html>
   <head>
       <title>{% block title %}{% endblock %}</title>
   </head>
   <body>
       {% block content %}{% endblock %}
   </body>
   </html>
   ```

3. **Home Template (`home.html`):**
   ```html
   {% extends "base.html" %}

   {% block title %}Home{% endblock %}

   {% block content %}
   <h1>Google Slides Authentication</h1>
   <!-- Add authentication UI here -->
   {% endblock %}
   ```

4. **Generate Template (`generate.html`):**
   ```html
   {% extends "base.html" %}

   {% block title %}Generate Presentation{% endblock %}

   {% block content %}
   <h1>Generate Presentation</h1>
   <table id="jsonTable">
       <!-- Table populated dynamically -->
   </table>
   <button type="button" onclick="generate()">Generate</button>
   <script src="/static/js/generate.js"></script>
   {% endblock %}
   ```

5. **Static Files:**
   Add necessary CSS and JavaScript files under `static/`.

6. **`generate.js`:**
   ```javascript
   document.addEventListener('DOMContentLoaded', () => {
       fetch('/json-objects')
           .then(response => response.json())
           .then(data => {
               const table = document.getElementById('jsonTable');
               data.forEach((obj, index) => {
                   let row = table.insertRow();
                   let cell1 = row.insertCell(0);
                   let cell2 = row.insertCell(1);
                   cell1.innerHTML = `<input type="radio" name="jsonSelect" value='${JSON.stringify(obj)}'>`;
                   cell2.innerHTML = obj.title;
               });
           });
   });

   function generate() {
       const selected = document.querySelector('input[name="jsonSelect"]:checked');
       if (!selected) {
           alert('Please select a JSON object.');
           return;
       }

       const content = selected.value;
       fetch('/generate', {
           method: 'POST',
           headers: {
               'Content-Type': 'application/json'
           },
           body: JSON.stringify({ content })
       }).then(response => response. json())
         .then(result => {
             alert(result.message);
         }).catch(error => {
             console.error('Error:', error);
         });
   }
   ```

## Publishing and Testing
1. **Test Locally:**
   - Run the FastAPI app: `uvicorn app:app
[media pointer="sediment://file_00000000750c41f69eaefaf04b41aac4"]