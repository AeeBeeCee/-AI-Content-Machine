import os
import google.generativeai as genai

def generate_all_posts(raw_news):
    api_key = os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        return "Error: I can't find your Google API Key!"
    
    genai.configure(api_key=api_key)
    
    # MAGIC TRICK: Automatically find a working model
    model_name = "gemini-1.5-flash"
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            model_name = m.name
            break
            
    model = genai.GenerativeModel(model_name)
    prompt = f"Based on the news below, write a LinkedIn post, an X post, and a Facebook post:\n\n{raw_news}"
    
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Oops, the writer got stuck: {str(e)}"
