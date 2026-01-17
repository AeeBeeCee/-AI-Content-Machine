import os
import google.generativeai as genai

def generate_all_posts(raw_news, tone):
    api_key = os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        return "Error: I can't find your Google API Key!"
    
    genai.configure(api_key=api_key)
    
    # Automatically find a working model
    model_name = "gemini-1.5-flash"
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            model_name = m.name
            break
            
    model = genai.GenerativeModel(model_name)
    
    # Instructions for the AI to handle your new features
    prompt = f"""
    You are a professional social media ghostwriter. 
    
    YOUR GOAL:
    1. Digest the news below and extract the "So What?" (why does this matter to a professional audience?).
    2. Find a "Power Quote" or a catchy "Hook" from the news.
    3. Write 3 posts (LinkedIn, X, Facebook) in a {tone} tone.
    
    TONE GUIDE:
    - If "Naija Centric": Use Nigerian English/Pidgin flair, relatable local context, and high energy.
    - If "Authoritative": Be bold, expert-level, and decisive.
    - If "Humorous": Use wit, irony, or lighthearted jokes.
    - If "Professional": Be polished, clear, and business-ready.
    
    NEWS CONTENT:
    {raw_news}
    """
    
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Oops, the writer got stuck: {str(e)}"
