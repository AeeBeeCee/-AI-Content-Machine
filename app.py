import os
import streamlit as st
from writer_agent import generate_everything

st.set_page_config(page_title="AI Content Machine Pro v2", layout="wide")

# This new title will help us see if the update worked!
st.title("🤖 AI Content Machine Pro v2.0")
st.subheader("Your Personal Digital Ghostwriter with Reliability Check")

st.divider()
st.info("🔑 Step 1: Enter your Google API Key.")
api_key_input = st.text_input("Paste your Google API Key here:", type="password")

if api_key_input:
    os.environ["GOOGLE_API_KEY"] = api_key_input
    st.success("✅ Key accepted!")
    
    st.divider()
    
    col1, col2 = st.columns(2)
    with col1:
        st.info("📰 Step 2: What is the topic?")
        topic = st.text_input("Enter a topic:", "Artificial Intelligence")
    with col2:
        st.info("🎭 Step 3: Choose your Tone")
        tone = st.selectbox("Select a Tone of Voice:", 
                            ["Professional", "Humorous", "Authoritative", "Naija Centric"])

    if st.button("🚀 Generate My Content"):
        with st.spinner("Researching, Fact-Checking, and Writing..."):
            # This calls the new brain in writer_agent.py
            final_output = generate_everything(topic, tone)
            
            st.subheader("📝 Your Social Media Drafts & Reliability Report")
            st.write(final_output)
else:
    st.warning("Waiting for your API Key...")
    st.stop()
