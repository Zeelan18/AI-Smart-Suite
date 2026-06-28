from models.gemini_config import model

def summarize_text(text, summary_type):

    prompt = f"""
    Summarize the following text.

    Summary Type: {summary_type}

    Text:
    {text}
    """

    response = model.generate_content(prompt)

    return response.text