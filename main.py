import streamlit as st
import streamlit.components.v1 as components

st.title("Custom Characters for LCD 16x2")

st.markdown('This generator is for LCD16x2 presented on the [Github LCD](https://github.com/the-raspberry-pi-guy/lcd?tab=readme-ov-file#custom-characters)', unsafe_allow_html=True)
st.markdown('Original implementation of custom characters by Juvus: [Custom Characters](https://github.com/juvus/lcd)', unsafe_allow_html=True)
st.markdown('Source code of this Streamlit app by Julien Minniti: [Streamlit Custom Characters LCD Generator](https://github.com/Jumitti/lcd_custom_characters)', unsafe_allow_html=True)

with open('main.html', 'r', encoding='utf-8') as file:
    grid_content = file.read()
    file.close()

components.html(grid_content, height=600)
