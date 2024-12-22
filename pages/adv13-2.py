import streamlit as st
import os
from utils import init_page

init_page()

st.title("聊天室示範")


if "message" not in st.session_state:
    st.session_state.message = []

for message in st.session_state.message:
    with st.chat_message(message["role"]):
        st.write(message["content"])

if message := st.chat_input("輸入訊息"):
    with st.chat_message("user"):
        st.write(message)
    st.session_state.message.append({"role": "user", "content": message})
    assistant_reponse = f"你說了：{message}"
    with st.chat_message("assistant"):
        st.write(assistant_reponse)
    st.session_state.message.append({"role": "assistant", "content": assistant_reponse})
