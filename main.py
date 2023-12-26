import streamlit as st
import streamlit.components.v1 as components

with open('main.html', 'r', encoding='utf-8') as file:
    grid_content = file.read()

st.title("Custom Characters for LCD 16x2")

components.html(grid_content,
    height=600)