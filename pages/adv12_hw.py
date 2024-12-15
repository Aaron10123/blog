import streamlit as st
import os

image_folder = "image"
image_files = os.listdir(image_folder)

col1, col2 = st.columns([1, 2])

with col1:
    with st.expander("圖片元件"):
        fruit = st.selectbox("選擇圖片", ["apple.png", "banana.png", "strawberry.png"])
        width = st.slider(
            "輸入圖片寬度", min_value=100, max_value=500, value=100, step=100
        )


with col2:
    st.image(os.path.join(image_folder, fruit), width=width)
