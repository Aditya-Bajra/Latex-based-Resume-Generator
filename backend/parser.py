import json
from google.genai import Client, types

def build_parsing_prompt(resume_text: str) -> str:
   
    return f"""
    You are a precise and flexible resume parser.

    Convert the following resume into structured JSON with these fields:

    - name
    - contact: {{email, phone, linkedin, github, website}}
    - summary (if present, otherwise empty string)
    - education: list of {{degree, university, year, gpa (if present)}}
    - experience: list of {{title, company, location (if present), years, descriptions (list of bullet points)}}
    - skills: {{technical (list), soft (list if present), languages (list if present)}}
    - projects (if present): list of {{name, description, technologies}}
    - other_sections (if present): dictionary where keys are section names (like 'Certifications', 'Awards', 'Publications', etc.) and values are lists of strings or key-value objects where appropriate.

    Any information not fitting the core fields should go into `other_sections`.

    For missing information, use empty strings or empty lists.

    Here is an example:

    Resume:
    Jane Smith  
    Email: jane@example.com  
    Phone: 555-321-9876  
    LinkedIn: linkedin.com/in/janesmith  
    GitHub: github.com/janesmith  

    Education:  
    M.Sc. in Data Science, ABC University, 2021  

    Experience:  
    - Data Scientist at XYZ Corp (2021–2023)  
    Led model development for customer churn prediction using Python and scikit-learn.  
    Improved accuracy by 15% through hyperparameter tuning.  
    Deployed models using Docker and Flask APIs.  

    Skills:  
    Python, Machine Learning, Pandas, Docker, Flask  

    Projects:  
    - Customer Churn Predictor  
    Developed a model to predict churn with 85% accuracy using historical behavior data.  
    Technologies: Python, scikit-learn, pandas  

    Certifications:  
    - AWS Certified Machine Learning – Specialty  

    ---

    Now parse the following resume:

    Resume:
    {resume_text}
    """
def parse_resume(client: Client, resume_text: str, model: str):
    prompt = build_parsing_prompt(resume_text)
    response = client.models.generate_content(
        model=model,
        contents=prompt,
        config=types.GenerateContentConfig(
            temperature=0.2,
            response_mime_type="application/json"
        )
    )
    return json.loads(response.candidates[0].content.parts[0].text)
