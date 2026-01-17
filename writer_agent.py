import os
import google.generativeai as genai

def generate_everything(topic, tone):
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
    
    # ONE BIG PROMPT: Find news + Analyze + Write
    prompt = f"""
    You are an expert researcher and social media ghostwriter.
    
    TASK:
    1. Find 3 recent and trending news stories about the topic: {topic}.
    2. For each story, explain the "So What?" (why it matters to professionals).
    3. Extract a "Power Quote" or "Hook" from the news.
    4. Write 3 social media posts (LinkedIn, X, Facebook) in a {tone} tone.
    
    TONE GUIDE:
    - Naija Centric: Use Nigerian English/Pidgin flair and local context.
    - Authoritative: Bold, expert, and decisive.
    - Humorous: Witty and lighthearted.
    - Professional: Polished and business-ready.
    
    Please format the output clearly so it's easy to read.
    """
    
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Oops, the machine got stuck: {str(e)}"
