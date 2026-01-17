import os
import google.generativeai as genai

def generate_all_posts(raw_news ):
    """
    Generates social media posts based on the provided news.
    """
    api_key = os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        return "Error: GOOGLE_API_KEY not set."
    
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-2.0-flash")
    
    prompt = f"Based on the following news, generate 3 social media posts (Twitter, LinkedIn, Instagram):\n\n{raw_news}"
    
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error generating posts: {str(e)}"
