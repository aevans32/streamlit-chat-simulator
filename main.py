import streamlit as st
import requests
import json


# Hugging Face API Info (from secrets.toml)
HF_API_URL = st.secrets["HF_API_URL"]
HF_API_TOKEN = st.secrets["HF_API_TOKEN"]


def query_llm(prompt):
    headers = {
        'Authorization': f'Bearer {HF_API_TOKEN}',
        'Content-Type': 'application/json'
    }

    payload = {
        'inputs': f'Answer briefly and clearly:\nQuestion: {prompt}\nAnswer:',
        'parameters': {
            'max_new_tokens': 100,
            'temperature': 0.7,
            'return_full_text': False
        }
    }

    try:
        response = requests.post(HF_API_URL, headers=headers, json=payload)
        if response.status_code == 200:
            result = response.json()
            if isinstance(result,list) and 'generated_text' in result[0]:
                return result[0]['generated_text']
            else:
                return json.dumps(result)
        else:
            st.error(f"Error: {response.status_code} - {response.text}")
            return "An error occurred while fetching your request."
    except Exception as e:
        st.error(f"Error querying LLM: {e}")
        return "An error occurred while processing your request."


# Streamlit Page Setup
st.set_page_config(page_title='Hugging Face Chatbot')
st.title('🤖 Hugging Face Chatbot')

# Initialize session state
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# Show message history
for msg in st.session_state.chat_history:
    with st.chat_message(msg['role']):
        st.markdown(msg['content'])

# Chat input
user_input = st.chat_input('Ask a question...')

if user_input:
    st.chat_message('user').markdown(user_input)
    # Show user message
    st.session_state.chat_history.append({'role': 'user', 'content': user_input})

    # Generate AI response
    with st.chat_message('assistant'):
        with st.spinner('Thinking...'):
            response = query_llm(user_input)
            st.markdown(response)
    st.session_state.chat_history.append({'role': 'assistant', 'content': response})
