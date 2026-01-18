import os
import streamlit as st
from writer_agent import generate_everything

# 1. Page Configuration & Styling
st.set_page_config(page_title="AI Content Machine Pro v2", layout="wide")

# This part adds custom "paint" to your website
st.markdown("""
    <style>
    .main {
        background-color: #f5f7f9;
    }
    .stButton>button {
        width: 100%;
        border-radius: 10px;
        height: 3em;
        background-color: #007bff;
        color: white;
        font-weight: bold;
    }
    .stTextInput>div>div>input {
        border-radius: 10px;
    }
    .report-card {
        background-color: white;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_stdio=True)

# 2. Header Section
with st.container():
    st.title("🤖 AI Content Machine Pro v2.0")
    st.markdown("### *Your Personal Digital Ghostwriter & Strategic Partner*")
    st.divider()

# 3. Step 1: API Key (The Security Gate)
with st.expander("🔑 Step 1: Security Access", expanded=True):
    api_key_input = st.text_input("Paste your Google API Key here to unlock the machine:", type="password")

if api_key_input:
    os.environ["GOOGLE_API_KEY"] = api_key_input
    
    # 4. Step 2 & 3: Configuration
    st.markdown("---")
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### 📰 Step 2: Research Topic")
        topic = st.text_input("What should I research today?", "Artificial Intelligence")
        
    with col2:
        st.markdown("#### 🎭 Step 3: Brand Voice")
        tone = st.selectbox("Select your preferred tone:", 
                            ["Professional", "Humorous", "Authoritative", "Naija Centric"])

    st.markdown("###") # Adds some space
    
    # 5. The Action Button
    if st.button("🚀 GENERATE MY CONTENT STRATEGY"):
        with st.spinner("🧠 Machine is thinking... researching, fact-checking, and writing."):
            final_output = generate_everything(topic, tone)
            
            st.markdown("---")
            st.markdown("### 📝 Your Strategy & Drafts")
            # We put the output in a nice "card"
            st.markdown(f'<div class="report-card">{final_output}</div>', unsafe_allow_html=True)
            
            st.balloons() # A little celebration!
else:
    st.warning("Please enter your API Key above to begin.")
    st.stop()
