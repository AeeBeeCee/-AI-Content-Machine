import os
import streamlit as st
from news_agent import fetch_news
from writer_agent import generate_all_posts

# 1. Title of your website
st.set_page_config(page_title="AI Content Machine", layout="wide")

st.title("🤖 AI Content Machine")
st.subheader("Your Personal Digital Ghostwriter")

# 2. THE KEY BOX - Now right in the middle of the screen!
st.divider()
st.info("🔑 Step 1: Enter your Google API Key below to unlock the machine.")
api_key_input = st.text_input("Paste your Google API Key here:", type="password")

# 3. Save the key so the other files can find it
if api_key_input:
    os.environ["GOOGLE_API_KEY"] = api_key_input
    st.success("✅ Key accepted! Now you can use the machine below.")
else:
    st.warning("Waiting for your API Key...")
    st.stop() # This stops the app until you enter the key

st.divider()

# 4. The Topic Box
st.info("📰 Step 2: What topic should I research today?")
topic = st.text_input("Enter a topic (e.g., AI News, Cooking, Tech):", "Artificial Intelligence")

# 5. The big "Go" button
if st.button("🚀 Generate My Posts"):
    with st.spinner("Searching for news and writing your posts..."):
        # First, find the news
        news = fetch_news(topic)
        
        # Second, write the posts
        drafts = generate_all_posts(news)
        
        # Show the final result
        st.subheader("📝 Your Social Media Drafts")
        st.write(drafts)
