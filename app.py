import streamlit as st
from openai import OpenAI

USER_EMOJI = '🧑‍🚀'
ASSISTANT_EMOJI = '🤖'

st.header(f"{ASSISTANT_EMOJI} ChatGPT clone")

client = OpenAI(api_key=st.secrets['OPENAI_API_KEY'])

# set default model
if 'openai_model' not in st.session_state:
    st.session_state['openai_model'] = 'gpt-3.5-turbo'

# initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message['role'], avatar=message['avatar']):
        st.markdown(message['content'])

# react to user input
if prompt := st.chat_input("What is up?"):
     st.session_state.messages.append({'role': 'user', 'content': prompt, 'avatar': f'{USER_EMOJI}'})
     st.chat_message('user', avatar=f'{USER_EMOJI}').markdown(prompt)

     # display GPT 3.5 response
     with st.chat_message('assistant', avatar=f'{ASSISTANT_EMOJI}'):
         
         stream = client.chat.completions.create(
             model=st.session_state['openai_model'],
             messages=[
                 {'role': m['role'], 'content': m['content']}
                 for m in st.session_state.messages
             ],
             stream=True
         )
         response = st.write_stream(stream)
         
     # add assistant response to chat history
     st.session_state.messages.append({'role': 'assistant', 'content': response, 'avatar': f'{ASSISTANT_EMOJI}'})