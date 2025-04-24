# Latex-based Resume Generator

This repository contains a **Latex-based Resume Generator** that was originally created as part of the **[Gen AI Intensive Course Capstone 2025Q1](https://www.kaggle.com/competitions/gen-ai-intensive-course-capstone-2025q1)**. Initially developed as a notebook for event submission, it has now been evolved into a fully functional **Streamlit app** to generate customizable resumes with a clean and professional layout using **LaTeX** templates.

## Overview

The project is designed to help users generate personalized resumes through an interactive web interface. By inputting basic information (such as name, contact details, skills, education, etc.), users can generate a downloadable LaTeX file which can be compiled into a beautifully formatted resume.

### Key Features

- **Customizable LaTeX templates** 
- **Zero Manual Editing**
- **Interactive UI** 
- **Downloadable LaTeX and PDF output** .

## Folder Structure
```
📂latex-resume-generator/
 │ config.py   # pydantic settings to manage API keys
 │ latex-based-resume-generator.ipynb   # notebook implementation 
 │ requirements.txt   # python dependencies
 ├───📂backend 
    │ latex_generator.py   # Generates LaTeX code from structured data
    │ main.py   # Backend entry point (No API logic yet)
    │ parser.py   # Parses raw input into json
    │ utils.py   # Utility/helper functions
    │ init.py   # Initializes python module
 ├───📂frontend 
    │ app.py   # Streamlit frontend application
```

## Usage
### Prerequisites
Ensure you have the following installed:
- Python 3.8+
- [MiKTeX](https://miktex.org/download)
### Install Dependencies
```bash
pip install -r requirements.txt
```
### Run the Streamlit App
```bash
python -m streamlit run app.py
```
## Example Output

Here’s a screenshot of the **generated resume** from the app:

![Resume Screenshot](assets/Screenshot%202025-04-24%20173529.png)
![Resume Screenshot](assets/Screenshot%202025-04-24%20173706.png)
