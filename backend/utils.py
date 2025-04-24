import subprocess

def compile_latex_to_pdf(tex_path: str, output_dir: str = "."):
    subprocess.run(["pdflatex", "-output-directory", output_dir, tex_path], check=True)

def load_template(template_path: str) -> str:
    with open(template_path, "r", encoding="utf-8") as f:
        return f.read()

