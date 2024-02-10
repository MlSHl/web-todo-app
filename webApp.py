import streamlit as st
import functions

todos = functions.get_todos()
st.title("My To-do App")
st.subheader("This is my todo app.")
st.write("This is to write lists.")


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)


for todo in todos:
    st.checkbox(todo)

st.text_input(label=" ", placeholder="Add new todo...",
              on_change=add_todo, key="new_todo")

st.session_state