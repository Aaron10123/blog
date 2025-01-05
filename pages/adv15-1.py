import streamlit as st
from utils import init_page
from openai import OpenAI
import os
from dotenv import load_dotenv

# 新增變數，包含所有 pages 資料夾中的 .py 檔案名稱
pages_files = []
for f in os.listdir("pages"):
    if f.endswith(".py"):
        pages_files.append(f)

# 載入環境變數
load_dotenv()

# 初始化 OpenAI 客戶端
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# 初始化頁面
init_page()
st.title("AI 聊天室")

assistant_response = "None"
# 取得使用者輸入的訊息
if message := st.chat_input("請輸入訊息"):
    # 顯示使用者的訊息
    with st.chat_message("user"):
        st.write(message)

    # 取得 AI 回覆
    try:
        completion = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "system",
                    "content": f"""
你是一個只能說出檔案名稱的小幫手。 
根據 {pages_files} 和使用者詢問的內容，
只能提供一個適合前往的檔案名稱。 如果看不懂使用者想前往哪裡，
可以回傳 None。
                    """,
                },
                {"role": "user", "content": message},
            ],
        )
        assistant_response = completion.choices[0].message.content

        # 顯示助手回覆
        with st.chat_message("assistant"):
            # 檢查並移除回覆中的引號
            if assistant_response.startswith("'") and assistant_response.endswith("'"):
                assistant_response = assistant_response[1:-1]
            if assistant_response in pages_files:
                st.write(f"pages/{assistant_response}")
            else:
                st.write("無效的檔案名稱")

    except Exception as e:
        st.error(f"發生錯誤: {str(e)}")

# 新增按鈕，讓使用者可以點選並跳轉頁面
if assistant_response != "None":
    st.switch_page(f"pages/{assistant_response}")
