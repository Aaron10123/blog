import streamlit as st
from .menu import menu


def init_page():
    st.set_page_config(
        page_title="電子工程學習筆記",
        page_icon="📚",
        layout="wide",
        initial_sidebar_state="expanded",
    )
    menu()
