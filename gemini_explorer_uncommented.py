import vertexai
import streamlit as st
from vertexai.preview import generative_models
from vertexai.preview.generative_models import GenerativeModel, Part, Content, ChatSession

project = "gemini-explorer-415722"
vertexai.init( project = project )

config = generative_models.GenerationConfig( temperature=0.4 )

model = GenerativeModel(
    "gemini-pro", 
    generation_config = config
)
chat = model.start_chat()

if "messages" not in st.session_state:
    st.session_state.messages = []

def llm_function(chat: ChatSession, query):
    response = chat.send_message(query)
    output = response.candidates[0].content.parts[0].text

    with st.chat_message("model"):
        st.markdown(output)
    st.session_state.messages.append(
        {
            "role": "user",
            "content": query
        }
    )
    st.session_state.messages.append(
        {
            "role": "model",
            "content": output
        }
    )

st.title("Gemini Explorer")

for index, message in enumerate(st.session_state.messages):
    content = Content(
            role = message["role"],                           
            parts = [ Part.from_text(message["content"]) ]      
        )
    if index != 0:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    chat.history.append(content)

if len(st.session_state.messages) == 0:
    initial_prompt = "Hello! What can I do for you?"
    llm_function(chat, initial_prompt)

query = st.chat_input("Gemini Explorer")

if query:
    with st.chat_message("user"):
        st.markdown(query)
    llm_function(chat, query)

    