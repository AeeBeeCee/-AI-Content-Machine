import os
import streamlit as st
from news_agent import fetch_news
from writer_agent import generate_all_posts

st.set_page_config(page_title="AI Content Machine", layout="wide")

st.title("🤖 AI Content Machine")
st.subheader("Your Personal Digital Ghostwriter")

st.divider()
st.info("🔑 Step 1: Enter your Google API Key below.")
api_key_input = st.text_input("Paste your Google API Key here:", type="password")

if api_key_input:
    os.environ["GOOGLE_API_KEY"] = api_key_input
    st.success("✅ Key accepted!")
    
    st.divider()
    st.info("📰 Step 2: What topic should I research today?")
    topic = st.text_input("Enter a topic:", "Artificial Intelligence")

    if st.button("🚀 Generate My Posts"):
        with st.spinner("Working..."):
            news = fetch_news(topic)
            drafts = generate_all_posts(news)
            st.subheader("📝 Your Social Media Drafts")
            st.write(drafts)
else:
    st.warning("Waiting for your API Key...")
    st.stop()
