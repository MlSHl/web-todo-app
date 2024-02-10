import streamlit as st
import functions

todos = functions.get_todos()
st.title("My To-do App")
st.subheader("This is my todo app.")
st.write("This is to write lists.")

st.checkbox("Sleep")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="", placeholder="Add new todo...")