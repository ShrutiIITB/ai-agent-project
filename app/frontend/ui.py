import streamlit as st 
import requests  #used to send HTTP post requests

from app.config.settings import settings 
from app.utlis.logger import get_logger 
from app.utlis.common_exception import CustomException 
import traceback

logger = get_logger(__name__)

st.set_page_config(
    page_title='My AI Agent',
    layout = 'centered'
)

st.title("My AI Agent using OpenAI")

system_prompt = st.text_area("Define your Agent",
                             height=90,
                             placeholder="E.g., You are a helpful assistant that provides concise answers.")

selected_model = st.selectbox("Select Model",
                                options=settings.ALLOWED_MODEL_NAMES,
                                index=0)

user_query = st.text_area("Enter your query",
                          height=150,
                          placeholder="E.g., Explain the theory of relativity in simple terms.") 

allow_web_search = st.checkbox("Allow Web Search", value=False) 

API_URL = 'http://127.0.0.1:8080/chat' 

if st.button('Run Agent') and user_query.strip():
    
    payload =  {
        "model_name": selected_model,
        "system_prompt": system_prompt,
        "messages": [user_query],
        "allow_search": allow_web_search
    }

    try:
        logger.info("Sending request to AI Agent API")
        response = requests.post(API_URL, json=payload) 

        if response.status_code == 200:
            ai_response = response.json().get('response', '')
            st.subheader("AI Agent Response:")
            st.markdown(ai_response, unsafe_allow_html=True) 
            logger.info("Successfully received response from AI Agent API")
        else:
            logger.error(f"Error from AI Agent API Response - {response.status_code}: {response.text}")
            st.error(f"Error from AI Agent API - Status {response.status_code}: {response.text}")
    
    except Exception as e:
        logger.error(f"Exception while communicating with AI Agent API: {str(e)}")
        st.error(str(CustomException("Failed to communicate with AI Agent API", str(e))))


if __name__ == "__main__":

    payload =  {
        "model_name": 'gpt-4o-mini',
        "system_prompt": 'You are math teacher',
        "messages": ['What is 2+2?'],
        "allow_search": False
    }
    response = requests.post(API_URL, json=payload) 
    print(response.json())
