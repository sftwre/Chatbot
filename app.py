import numpy as np
import streamlit as st

st.header("Chat with AI!")
st.title("Echo Bot 🤖")

# initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message['role']):
        st.markdown(message['content'])

# react to user input
if prompt := st.chat_input("What is up?"):
     st.chat_message("user").markdown(prompt)
     st.session_state.messages.append({'role': 'user', 'content': prompt})

     response = f"Echo: {prompt}"
     # display assistant response in chat message container
     with st.chat_message('assistant'):
         st.markdown(response)
         
     # add assistant response to chat history
     st.session_state.messages.append({'role': 'assistant', 'content': response})