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
    
    # NEW PROMPT: Added Reliability Check and Calendar Planning
    prompt = f"""
    You are an expert researcher, fact-checker, and social media ghostwriter.
    
    TASK:
    1. RESEARCH: Find 3 recent news stories about: {topic}.
    2. RELIABILITY CHECK: For each story, give a "Reliability Score" (1-10) and a quick reason why (e.g., "From a major tech outlet" or "Sounds like speculative hype").
    3. ANALYSIS: Explain the "So What?" for professionals.
    4. CONTENT: Write a LinkedIn, X, and Facebook post in a {tone} tone.
    5. CALENDAR: Suggest which day of the week (Monday-Friday) each story would be best to post.
    
    TONE GUIDE:
    - Naija Centric: Use Nigerian English/Pidgin flair and local context.
    - Authoritative: Bold, expert, and decisive.
    - Humorous: Witty and lighthearted.
    - Professional: Polished and business-ready.
    
    Please format the output with clear headings like '🛡️ RELIABILITY CHECK' and '📅 SUGGESTED SCHEDULE'.
    """
    
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Oops, the machine got stuck: {str(e)}"
