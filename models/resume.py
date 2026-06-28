import pdfplumber
from models.gemini_config import model


def extract_text(pdf_file):
    text = ""

    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

    return text


def analyze_resume(text):

    prompt = f"""
You are an ATS Resume Analyzer.

Analyze the following resume professionally.

Return in the following format.

# Overall Resume Score (/100)

# ATS Compatibility (/100)

# Strengths

# Weaknesses

# Missing Skills

# Suggestions

Resume:

{text}

"""

    response = model.generate_content(prompt)

    return response.text