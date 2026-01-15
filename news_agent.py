import os
import google.generativeai as genai

def fetch_news(topic):
    api_key = os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        return "Error: I can't find your Google API Key!"
    
    genai.configure(api_key=api_key)
    
    # MAGIC TRICK: This part automatically finds a working model for you
    model_name = "gemini-1.5-flash" # Default guess
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            model_name = m.name
            break # We found one!
            
    model = genai.GenerativeModel(model_name)
    prompt = f"Find 3 recent and trending news stories about {topic}. For each story, give me a catchy title and a short summary."
    
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Oops, something went wrong: {str(e)}"
