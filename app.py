import os
import streamlit as st
from news_agent import fetch_news
from writer_agent import generate_all_posts

st.set_page_config(page_title="AI Content Machine Pro", layout="wide")

st.title("🤖 AI Content Machine Pro")
st.subheader("Your Personal Digital Ghostwriter & Designer")

st.divider()
st.info("🔑 Step 1: Enter your Google API Key.")
api_key_input = st.text_input("Paste your Google API Key here:", type="password")

if api_key_input:
    os.environ["GOOGLE_API_KEY"] = api_key_input
    st.success("✅ Key accepted!")
    
    st.divider()
    
    # NEW: Tone and Topic Selection
    col1, col2 = st.columns(2)
    
    with col1:
        st.info("📰 Step 2: What is the topic?")
        topic = st.text_input("Enter a topic:", "Artificial Intelligence")
        
    with col2:
        st.info("🎭 Step 3: Choose your Tone")
        tone = st.selectbox("Select a Tone of Voice:", 
                            ["Professional", "Humorous", "Authoritative", "Naija Centric"])

    # NEW: Image Generation Toggle
    generate_image = st.checkbox("🎨 Generate a matching AI Image for these posts?")

    if st.button("🚀 Generate My Content"):
        with st.spinner("Researching, Writing, and Designing..."):
            # 1. Fetch News
            news = fetch_news(topic)
            
            # 2. Generate Posts with the chosen Tone
            drafts = generate_all_posts(news, tone)
            
            # 3. Show Results
            st.subheader("📝 Your Social Media Drafts")
            st.write(drafts)
            
            # 4. Mock Image Generation (Placeholder for now)
            if generate_image:
                st.divider()
                st.subheader("🎨 AI Image Suggestion")
                st.info(f"Generating a {tone} style graphic for: {topic}...")
                st.warning("Note: Image generation (DALL-E) requires a paid API. For now, I've prepared the 'plumbing' for it!")
else:
    st.warning("Waiting for your API Key...")
    st.stop()
