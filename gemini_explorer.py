import vertexai
import streamlit as st
from vertexai.preview import generative_models
from vertexai.preview.generative_models import GenerativeModel, Part, Content, ChatSession

project = "gemini-explorer-415722"
vertexai.init( project = project )

config = generative_models.GenerationConfig( temperature=0.4 )

# load model with config
model = GenerativeModel(
    "gemini-pro", 
    generation_config = config
)
chat = model.start_chat()

# initialize chat history - set the messages into an empty array
if "messages" not in st.session_state:
    st.session_state.messages = []

# llm_function: display and send streamlit messages
def llm_function(chat: ChatSession, query):
    response = chat.send_message(query) # define response that sending 'query' over to the ChatSession
    output = response.candidates[0].content.parts[0].text

    with st.chat_message("model"):
        # tell streamlit to create an 'output' text and then applying that to the ChatSession
        st.markdown(output)
    st.session_state.messages.append(
        {
            # append into the session memory that the user has made a query
            "role": "user",
            "content": query
        }
    )
    st.session_state.messages.append(
        {
            # append the model output
            "role": "model",
            "content": output
        }
    )

# make a title
st.title("Gemini Explorer")

# display and load to chat history
for index, message in enumerate(st.session_state.messages):
    # create a variable holding Content class with two parameters "role" and "parts", corresponding to "role" and "content" in 'session_state'
    content = Content(
            role = message["role"],                             # store as a string
            parts = [ Part.from_text(message["content"]) ]      # store multiple things as an array
        )
    if index != 0:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    chat.history.append(content)  # append to make it a multiturned conversation with a 'user' role followed by a 'model' role [gcloud flavor]

# initial message startup
if len(st.session_state.messages) == 0:
    initial_prompt = "Introduce yourself as ReX, an assistant powered by Google Gemini. You use emojis to be interactive"
    llm_function(chat, initial_prompt)

# capture user input
query = st.chat_input("Gemini Explorer")

if query:
    # case: an input is coming

    # add role and add the actual session and then call llm_function to append to the chat model
    with st.chat_message("user"):
        st.markdown(query)
    llm_function(chat, query)

    