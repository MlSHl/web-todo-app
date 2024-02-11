import streamlit as st
import functions

todos = functions.get_todos()
st.title("Mo-do App")


def add_todo():
    if st.session_state["new_todo"] != "":
        todo = st.session_state["new_todo"] + "\n"
        print(todo)
        todos.append(todo)
        functions.write_todos(todos)
        st.session_state["new_todo"] = ""


for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=f"{index} {todo}")
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[f"{index} {todo}"]
        st.session_state["new_todo"] = ""
        st.rerun()

st.text_input(label=" ", placeholder="Add new todo...",
              on_change=add_todo, key="new_todo")