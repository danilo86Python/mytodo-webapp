# http://localhost:8501/

import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] # + "\n"
    todos.append(todo)
    functions.write_todos(todos)


st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity.")


for todo in todos:
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        print(checkbox)

st.text_input(label="New item", placeholder="Add new todo...",
              on_change=add_todo, key='new_todo', label_visibility="collapsed")


print("Hello")

st.session_state