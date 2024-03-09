import vertexai
import streamlit as st
from vertexai.preview import generative_models
from vertexai.preview.generative_models import GenerativeModel, Part, Content, ChatSession

project = "sample-gemini"
vertexai.init( project = project)

config = generative_models.GenerationConfig( temperature=0.4 )

# load model with config
model = GenerativeModel(
    "gemini-pro", 
    generation_config = config
)
chat = model.start_chat()

def llm_function(chat, message):
    chat.send_message(message)

if len(st.session_state.messages) == 0:
    initial_prompt = "Introduce yourself as ReX, an assistant powered by Google Gemini. You use emojis to be interactive"
    llm_function(chat, initial_prompt)

    