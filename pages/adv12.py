import streamlit as st
import os
from utils import init_page

init_page()


col1, col2 = st.columns([1, 2])
with col1:
    if st.button("按鈕1", key="btn1"):
        st.balloons()
    st.write("這是按鈕1")
with col2:
    st.button("按鈕2", key="btn2")
    st.write("這是按鈕2")

col_num = st.number_input("輸入欄數", step=1, min_value=1, max_value=10, value=2)
cols = st.columns(col_num)
for i in range(len(cols)):
    with cols[i]:
        st.button("按鈕" + str(i + 1), key=str(i + 1))

col1, col2 = st.columns(2)
with col1:
    st.button("按鈕1", key="button1")
    st.button("按鈕2", key="button2")
    st.button("按鈕3", key="button3")
with col2:
    st.write("這是col2")
    st.write("這是col2")
    st.write("這是col2")
st.markdown("---")
for i in range(3):
    col1, col2 = st.columns(2)
    with col1:
        st.button(f"按鈕{i+1}", key=str(i + 10))
    with col2:
        st.button(f"這是col_{i+2}")

ans = 1
if st.button("按下去+1", key="ans1"):
    ans += 1
st.write(f"答案是{ans}")

if "ans" not in st.session_state:
    st.session_state.ans = 1

if st.button("按下去+1", key="ans2"):
    st.session_state.ans += 1
st.write(f"ans={st.session_state.ans}")

image_folder = "image"
image_files = os.listdir(image_folder)
st.write(image_files)

st.title("圖片元件")
st.image("image/apple.png", width=100)
fruit = st.selectbox("選擇水果", ["蘋果", "草莓", "香蕉"])
st.write(f"你選擇的水果是 {fruit}")
