import streamlit as st
import pdfplumber
from backend.main import process_resume
from config import settings
from streamlit_pdf_viewer import pdf_viewer 

st.title("LaTeX-based Resume Generator")

# Section 1: Resume Input
with st.expander("Upload Resume or Enter Text", expanded=True):
    col1, col2 = st.columns(2)
    
    with col1:
        # PDF upload for resume (Search result [2][6])
        uploaded_pdf = st.file_uploader("Upload PDF Resume", type=["pdf"])
        if uploaded_pdf:
            with pdfplumber.open(uploaded_pdf) as pdf:
                resume_text = "\n".join([page.extract_text() for page in pdf.pages])
        else:
            resume_text = st.text_area("Or Enter Resume Text", height=300)

    with col2:
        # LaTeX template upload (Existing functionality)
        uploaded_template = st.file_uploader("Upload LaTeX Template (.tex)", type=["tex"])
        template_path = settings.LATEX_TEMPLATE_PATH  # Default
        if uploaded_template:
            template_path = "uploaded_template.tex"
            with open(template_path, "wb") as f:
                f.write(uploaded_template.read())

# Section 2: Generation and Preview
if st.button("Generate Resume"):
    with st.spinner("Generating your resume..."):
        try:
            pdf_path, tex_path = process_resume(resume_text, template_path)
            st.session_state.generated_pdf = pdf_path
            st.success("Resume generated!")
            
            # Preview PDF (Search result [3][5])
            with st.expander("PDF Preview", expanded=True):
                pdf_viewer(pdf_path, width=700)
            
            # Download buttons (Search result [4])
            col_d1, col_d2 = st.columns(2)
            with col_d1:
                with open(pdf_path, "rb") as f:
                    st.download_button("Download PDF", f, file_name="resume.pdf")
            with col_d2:
                with open(tex_path, "rb") as f:
                    st.download_button("Download LaTeX", f, file_name="resume.tex")
                    
        except Exception as e:
            st.error(f"Error generating resume: {str(e)}")