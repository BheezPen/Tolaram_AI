import streamlit as st
import streamlit.components.v1 as components

# Read HTML content from file
with open("index.html", "r", encoding="utf-8") as f:
    html_content = f.read()

# Render the HTML
components.html(html_content, height=600, scrolling=True)