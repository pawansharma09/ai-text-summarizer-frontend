
### Streamlit Frontend

# AI Text Summarizer - Streamlit Frontend

Beautiful Streamlit interface for the text summarization API.

## Features
- Clean, responsive UI with modern design
- Adjustable summary length controls
- Real-time API communication
- Error handling and loading states
- Mobile-friendly layout

## Requirements
- Python 3.8+
- Streamlit Cloud account (for deployment)
- Access to the FastAPI backend URL

## Installation

### Local Development
1. Clone the repository
2. Create virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
3. Install dependencies:
    ```bash
    pip install -r requirements.txt
4. Configure API URL:
    Create .streamlit/secrets.toml:
    ```bash
   [connections]
    api_url = "http://localhost:8000"
5. Run the app:
    ```bash
    streamlit run app.py
