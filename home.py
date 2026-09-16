import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

st.title("Day 3 ")

if "bubble1" not in st.session_state:
    st.session_state.bubble1 = False

if "bubble2" not in st.session_state:
    st.session_state.bubble2 = False

if "bubble3" not in st.session_state:
    st.session_state.bubble3 = True

#if st.session_state.bubble1 is False and st.session_state.bubble2 is False and st.session_state.bubble3 is False:
#   st.write("All bubbles are False")

if st.session_state.bubble1 is False:
    st.write("Bubble 1 is False")

if st.session_state.bubble2 is False:
    st.write("And Bubble 2 is False")

if st.session_state.bubble3 is False:
    st.write("Bubble 3 is False")
    st.write("All bubbles are False")

else:
    st.write("Bubble 3 is True")

