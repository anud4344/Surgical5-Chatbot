# utilities/icon.py
import streamlit as st

def page_icon(emoji: str):
    st.markdown(f"<h1 style='display: none;'>{emoji}</h1>", unsafe_allow_html=True)