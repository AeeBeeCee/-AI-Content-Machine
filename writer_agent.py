import os
import google.generativeai as genai

def generate_all_posts(raw_news):
    # Again, we tell the machine to use your secret API Key
    api_key = os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        return "Error: I can't find your Google API Key!"
    
    # Connect to the AI "Brain"
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-2.0-flash")
    
    # Instructions for the AI to be your Ghostwriter
    prompt = f"""
    You are a professional social media ghostwriter. 
    Based on the news below, write 3 different posts:
    1. A professional LinkedIn post (with hashtags).
    2. A punchy X (Twitter) post (under 280 characters).
    3. A friendly Facebook post.
    
    Here is the news:
    {raw_news}
    """
    
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Oops, the writer got stuck: {str(e)}"
