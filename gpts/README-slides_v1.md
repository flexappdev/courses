# Courses App

The Courses App lets you Generates a Course on a speicic topic both as a markdown and export as PDF.  It creates a markdown page of a course  with intro,  up to 10 key sections, conclusion.  It will also Generates a slide deck with background images, title, description, tagline, short description and taglines


## Process
1. Generate course (GPT Assistant)
1. Update Course (markdown file)
1. Add Images to .md and revise
1. Add Copy to Images & Export
1. Export As PDF
1. Create Podcast

## 1-Generate Course (English Teacher GPTS)
1. English Teacher GPTS (GPT Assistant): https://chatgpt.com/g/g-GkYUg9VX0-english-teacher
1. Generate course based on keyword: "AI RAG"
1. Review & Update Response

```
## Generate Image prompts
1. [course name] Intoduction - image prompts
1. copy/paste 
1. Review
```

## 2-Update Course
1. Create .md file: _PRIVATE > courses > _orginal > course.md
1. Copy/Paste content from chatgpt
1. Update and move from _orginal to updated

```
clear && cd ~/_PRIVATE/ && source venv/bin/activate && cd courses && python3 main.py


- add function add_presentation_section 
that adds a ## Slides section at the bottom of the markdow document
a json of all the section with title, tagline, short desciption and image url

```

## 3-Add Images to .md and revise
1. Generate images for each section (introduction, )

```
clear && cd ~/IMAGES/ && source venv/bin/activate && python3 main.py
```

## 4-Add Copy to Images & Export
## Export As PDF
## Create Podcast


## GPTS: English Teacher

1. Name: "English Teacher"
1. Description: "Create courses based on template and assists English Teacher"
1. Instructions: Gen Doc in format, Gen Images (view Bwlow)
1. Conversation starters: max 4
1. Knowledge: pdf adeed
1. Capabilities:  
1. Actions: NA
1. Edit GPTS: https://chatgpt.com/gpts/editor/g-GkYUg9VX0


### Instructions
1. When ask "Course [keyword]" Generate a 1000 words course on the specified "keyword",  in markodwn with one H1 and 15 H2 sections (topics, introduction, objectives, topics 1 to 10, next steps, conclusion) in the below course format.  
1. Each Section should be about 200 words, most a taglline
1. When ask "Course images", generate an image prompt for each h2 section  "[course name] [section name] - image prompt"


### Course format
```
# Introduction to Python Programming

This is course in 12 key sections.

## Topics
[TOC]

## Introduction

Welcome to **Introduction to Python Programming**! This course is designed for beginners who are new to programming. Python is a versatile and powerful programming language used in various fields such as web development, data analysis, artificial intelligence, and more. By the end of this course, you'll have a solid foundation in Python and be able to build simple applications.

## Objectives

By the end of this course, you will:

1. Understand the basic syntax and structure of Python.
2. Write and execute Python scripts.
3. Work with variables, data types, and operators.
4. Implement control flow using conditionals and loops.
5. Create and manipulate data structures like lists, dictionaries, and tuples.
6. Define and use functions to organize code.
7. Handle exceptions and errors gracefully.

## Section 1: Getting Started with Python

### Overview

In this section, we'll set up your Python environment and write your first Python program.

### Topics Covered

- Installing Python
- Setting up an Integrated Development Environment (IDE)
- Writing and running your first Python script
- Understanding the Python interpreter

![Setting Up Python](../images/setup_python.png)

## Section 2: Variables and Data Types

### Overview

Learn about variables and the different data types available in Python.

### Topics Covered

- Variables and assignment
- Numbers (integers, floats)
- Strings and string manipulation
- Booleans
- Type conversion

![Data Types](../images/data_types.png)

## Section 3: Control Flow

### Overview

Control the flow of your programs using conditionals and loops.

### Topics Covered

- If, elif, else statements
- For loops
- While loops
- Break and continue statements
- Nested loops

![Control Flow](../images/control_flow.png)

## Section 4: Functions

### Overview

Organize your code into reusable functions.

### Topics Covered

- Defining functions
- Function arguments and return values
- Scope and lifetime of variables
- Lambda functions
- Built-in functions

![Functions](../images/functions.png)

## Section 5: Data Structures

### Overview

Work with Python's built-in data structures to store and manipulate data.

### Topics Covered

- Lists and list comprehensions
- Dictionaries
- Tuples
- Sets
- Manipulating data structures

![Data Structures](../images/data_structures.png)

## Conclusion

Congratulations on completing the **Introduction to Python Programming** course! You've learned the fundamentals of Python programming and are now equipped to build your own projects. Continue practicing by exploring more advanced topics and applying your skills to real-world problems.

![Congratulations](../images/congratulations.png)

```


