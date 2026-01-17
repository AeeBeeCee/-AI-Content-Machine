import os
import google.generativeai as genai

def fetch_news(topic ):
    """
    Fetches news related to the topic.
    In a real scenario, this might use a search API.
    For now, we will use LLM to simulate finding news.
    """
    api_key = os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        return "Error: GOOGLE_API_KEY not set."
    
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-2.0-flash") # Or another available model
    
    prompt = f"Find 3 recent news stories about {topic}. Provide the title and a mock URL for each."
    
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error fetching news: {str(e)}"
