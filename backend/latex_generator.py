import json

def build_latex_prompt(resume_json, latex_template):
    # Use the same LaTeX generation prompt as in your notebook
    return f"""
    You are a LaTeX resume generator. I have given you a resume template and a resume JSON.

    {json.dumps(resume_json)}

    Please format it using the following LaTeX template as inspiration:

    {latex_template}

    Generate a complete, well-formatted LaTeX document starting with \documentclass that follows the style of the template while incorporating all the information from the JSON data. The output should be ready to compile into a PDF. 
    Return only raw LaTeX code without wrapping it in triple backticks or Markdown formatting. Do not prefix the code with ```latex or anything else. Start with \documentclass....
    Only include sections if they contain at least one experience, project, or education entry. Do not include empty LaTeX environments with no items.
    """

def generate_latex_resume(client, resume_json, latex_template, model):
    prompt = build_latex_prompt(resume_json, latex_template)
    response = client.models.generate_content(
        contents=prompt,
        model=model
    )
    return response.candidates[0].content.parts[0].text
