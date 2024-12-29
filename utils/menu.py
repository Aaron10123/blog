import streamlit as st
import os


def menu():
    st.sidebar.title("Menu")
    st.sidebar.page_link(page="main.py", label="首頁", icon="🏠")
    st.sidebar.markdown("---")
    st.sidebar.title("課程")
    st.sidebar.page_link(page="pages/adv11.py", label="課程11", icon="📚")
    st.sidebar.page_link(page="pages/adv12.py", label="課程12", icon="📚")
    st.sidebar.page_link(page="pages/adv12_hw.py", label="課程12 hw", icon="📚")
    st.sidebar.page_link(page="pages/adv13-1.py", label="課程13", icon="📚")
    st.sidebar.markdown("---")

    pages_files_path = os.listdir("pages")
    pages_files_path = [page for page in pages_files_path if "adv" in page]
    page_path = st.sidebar.selectbox("選擇課程", pages_files_path)
    if st.sidebar.button("切換課程", key="change_page"):
        st.switch_page(f"pages/{page_path}")
    st.sidebar.markdown("---")
