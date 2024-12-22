import streamlit as st
import os
from utils import init_page

init_page()

st.title("聊天室示範")

demo_message = [
    {"role": "assistant", "content": "你是一個聊天機器人"},
    {"role": "user", "content": "你好"},
]

for message in demo_message:
    with st.chat_message(message["role"]):
        st.write(message["content"])

if message := st.chat_input("輸入訊息"):
    with st.chat_message("user"):
        st.write(message)

    with st.chat_message("assistant"):
        st.write(f"你說了：{message}")
