import os
import streamlit as st
from news_agent import fetch_news
from writer_agent import generate_all_posts

# 1. This sets up the title of your website
st.set_page_config(page_title="AI Content Machine", layout="wide")

# 2. This part asks for your secret Google API Key in the sidebar
if "GOOGLE_API_KEY" not in os.environ or not os.environ["GOOGLE_API_KEY"]:
    st.sidebar.warning("⚠️ Please enter your Google API Key to start.")
    api_key = st.sidebar.text_input("Google API Key", type="password")
    if api_key:
        os.environ["GOOGLE_API_KEY"] = api_key
        st.sidebar.success("Key accepted!")
    else:
        st.stop()

# 3. The main screen text
st.title("🤖 AI Content Machine")
st.subheader("Your Personal Digital Ghostwriter")

# 4. A box where you type what you want to write about
topic = st.text_input("What topic should I research today?", "Artificial Intelligence")

# 5. The big "Go" button
if st.button("Generate My Posts"):
    with st.spinner("Searching for news and writing your posts..."):
        # First, find the news
        news = fetch_news(topic)
        st.success("Found the latest news!")
        
        # Second, write the posts
        drafts = generate_all_posts(news)
        
        # Show the final result on the screen
        st.divider()
        st.subheader("📝 Your Social Media Drafts")
        st.write(drafts)
