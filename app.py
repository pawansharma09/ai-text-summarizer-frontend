import streamlit as st
import requests
import time

# API Configuration
API_URL = "https://your-render-api-url.onrender.com/summarize"  # Replace with your Render URL

# Page config
st.set_page_config(
    page_title="AI Text Summarizer",
    page_icon="📝",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: 700;
        color: #4F46E5;
        text-align: center;
        margin-bottom: 2rem;
    }
    .summary-box {
        background-color: #f0f9ff;
        border-radius: 10px;
        padding: 1.5rem;
        border-left: 4px solid #4F46E5;
        margin-top: 1rem;
    }
    .stButton>button {
        background-color: #4F46E5;
        color: white;
        border-radius: 8px;
        padding: 0.5rem 1.5rem;
        font-weight: 600;
    }
    .stButton>button:hover {
        background-color: #4338CA;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown('<div class="main-header">📝 AI Text Summarizer</div>', unsafe_allow_html=True)
st.markdown("### Powered by DistilBART CNN model")

# Input section
col1, col2 = st.columns([3, 1])
with col2:
    st.markdown("#### Settings")
    max_len = st.slider("Max Length", 50, 500, 130)
    min_len = st.slider("Min Length", 20, 200, 30)
    if min_len >= max_len:
        st.warning("Min length should be less than max length")

with col1:
    input_text = st.text_area(
        "Enter your text to summarize:",
        height=250,
        placeholder="Paste your article, document, or any text here..."
    )

# Summarize button
if st.button("✨ Generate Summary", use_container_width=True):
    if not input_text.strip():
        st.error("Please enter some text to summarize!")
    elif min_len >= max_len:
        st.error("Min length must be less than max length")
    else:
        with st.spinner("Generating summary..."):
            try:
                response = requests.post(
                    API_URL,
                    json={
                        "text": input_text,
                        "max_length": max_len,
                        "min_length": min_len
                    },
                    timeout=30
                )
                response.raise_for_status()
                summary = response.json()["summary"]
                
                # Display result
                st.markdown("### Summary")
                st.markdown(f'<div class="summary-box">{summary}</div>', unsafe_allow_html=True)
                
                # Add copy button
                st.code(summary, language="")  # Makes text selectable
                
            except requests.exceptions.RequestException as e:
                st.error(f"API Error: {str(e)}")
            except KeyError:
                st.error("Unexpected response format from API")
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")

# Footer
st.markdown("---")
st.markdown(
    "Built with ❤️ using [DistilBART](https://huggingface.co/sshleifer/distilbart-cnn-12-6) | "
    "Deployed on [Render](https://render.com) & [Streamlit Cloud](https://streamlit.io/cloud)"
)