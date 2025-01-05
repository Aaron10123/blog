from openai import OpenAI
import streamlit as st
import os
from utils import init_page
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

init_page()
st.title("AI 小助手")

if "message" not in st.session_state:
    st.session_state.message = []

for message in st.session_state.message:
    with st.chat_message(message["role"]):
        st.write(message["content"])


pages_files_path = os.listdir("pages")
pages_files_path = [page for page in pages_files_path if "adv" in page]
st.write(pages_files_path)

if message := st.chat_input("輸入訊息"):
    with st.chat_message("user"):
        st.write(message)
    st.session_state.message.append({"role": "user", "content": message})
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "system",
                "content": f"以下是目前的分頁{pages_files_path}, 請根據使用者的訊息在分頁中選擇課程,只給我課程名稱",
            },
            {"role": "user", "content": message},
        ],
    )
    assistant_reponse = completion.choices[0].message.content
    with st.chat_message("assistant"):
        st.write(assistant_reponse)
    if assistant_reponse in pages_files_path:
        # 去除.py
        assistant_reponse = assistant_reponse.replace(".py", "")
        st.link_button(f"{assistant_reponse}", url=f"{assistant_reponse}")
    st.session_state.message.append({"role": "assistant", "content": assistant_reponse})
