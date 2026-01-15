import os
import google.generativeai as genai

def fetch_news(topic):
    api_key = os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        return "Error: I can't find your Google API Key!"
    
    genai.configure(api_key=api_key)
    # We are using "gemini-pro" - this is a very stable name
    model = genai.GenerativeModel("gemini-pro")
    
    prompt = f"Find 3 recent and trending news stories about {topic}. For each story, give me a catchy title and a short summary."
    
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Oops, something went wrong: {str(e)}"
