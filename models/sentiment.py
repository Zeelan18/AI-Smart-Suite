from models.gemini_config import model

def analyze_sentiment(text):

    prompt = f"""
    Analyze the sentiment of the following text.

    Return your answer in this format:

    Sentiment:
    Confidence:
    Explanation:

    Text:
    {text}
    """

    response = model.generate_content(prompt)

    return response.text