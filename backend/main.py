from google.genai import Client
from config import settings
from .parser import parse_resume
from .latex_generator import generate_latex_resume
from .utils import compile_latex_to_pdf, load_template, save_file

def process_resume(resume_text: str, template_path: str):
    client = Client(api_key=settings.GOOGLE_API_KEY)
    resume_json = parse_resume(client, resume_text, settings.GEMINI_MODEL)
    latex_template = load_template(template_path)
    latex_code = generate_latex_resume(client, resume_json, latex_template, settings.GEMINI_MODEL)
    with open("generated_resume.tex", "w", encoding="utf-8") as f:
        f.write(latex_code)
    compile_latex_to_pdf("generated_resume.tex")
    return "generated_resume.pdf", "generated_resume.tex"
