from models.gemini_config import model

def get_response(prompt):
    response = model.generate_content(prompt)
    return response.text