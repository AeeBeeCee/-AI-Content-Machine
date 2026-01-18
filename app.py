import os
import streamlit as st
from writer_agent import generate_everything

# 1. Page Configuration
st.set_page_config(page_title="AI Content Machine Pro", layout="wide")

# 2. Premium Styling
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: #ffffff; }
    h1, h2, h3 { font-family: 'Inter', sans-serif; color: #ffd700 !important; }
    .report-card {
        background-color: #ffffff;
        color: #1c1e21;
        padding: 30px;
        border-radius: 20px;
        border-left: 8px solid #ffd700;
        box-shadow: 0 10px 25px rgba(0,0,0,0.3);
        margin-top: 25px;
        line-height: 1.6;
        white-space: pre-wrap;
    }
    .stButton>button {
        background-color: #ffd700 !important;
        color: #0e1117 !important;
        border-radius: 12px !important;
        font-weight: bold !important;
    }
    .stTextInput>div>div>input {
        background-color: #1c1e21 !important;
        color: white !important;
        border-radius: 10px !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Header Section
st.title("🛡️ AI Content Machine Pro")
st.markdown("#### *Elevate Your Professional Presence with AI-Powered Strategy*")
st.divider()

# 4. Step 1: Security Access
api_key_input = st.text_input("🔑 Step 1: Enter your Google API Key:", type="password")

if api_key_input:
    os.environ["GOOGLE_API_KEY"] = api_key_input
    st.markdown("---")
    
    # 5. Configuration
    col1, col2 = st.columns(2)
    with col1:
        topic = st.text_input("📰 Step 2: Research Topic", "Global Tech Trends")
    with col2:
        tone = st.selectbox("🎭 Step 3: Brand Voice", ["Professional", "Authoritative", "Humorous", "Naija Centric"])

    # 6. Action Button
    if st.button("🚀 GENERATE STRATEGY"):
        with st.spinner("Analyzing data..."):
            final_output = generate_everything(topic, tone)
            st.markdown("---")
            st.markdown("### 📝 Strategic Output")
            st.markdown(f'<div class="report-card">{final_output}</div>', unsafe_allow_html=True)
            st.balloons()
else:
    st.info("Please provide your API Key to unlock the premium dashboard.")
    st.stop()
