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


pages_files_path = os.listdir("pages")
pages_files_path = [page for page in pages_files_path if "adv" in page]
# st.write(pages_files_path)

if message := st.chat_input("輸入訊息"):
    with st.chat_message("us er"):
        st.write(message)
    st.session_state.message.append({"role": "user", "content": message})
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "system",
                "content": f"以下是目前的分頁{pages_files_path}, 請根據使用者的訊息在分頁中選擇課程,只給我課程名稱,如果有很多個請全部列出來,用list的形式",
            },
            {"role": "user", "content": message},
        ],
    )
    assistant_reponse = completion.choices[0].message.content
    assistant_reponse_list = eval(assistant_reponse)
    with st.chat_message("assistant"):
        st.write(assistant_reponse)
    for i in range(len(assistant_reponse_list)):
        if assistant_reponse_list[i] in pages_files_path:
            # 去除.py
            assistant_reponse = assistant_reponse_list[i].replace(".py", "")
            # st.write(assistant_reponse)
            st.link_button(f"{assistant_reponse}", url=f"{assistant_reponse}")
    st.session_state.message.append({"role": "assistant", "content": assistant_reponse})
