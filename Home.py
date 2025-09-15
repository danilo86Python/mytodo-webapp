import streamlit as st
import functions

todos = functions.get_todos()

st.set_page_config(layout="wide")

def add_todo():
    todo = st.session_state["new_todo"].strip()
    if todo:
        todos.append(todo)
        functions.write_todos(todos)

st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your <b>productivity</b>.",
         unsafe_allow_html=True)

st.text_input(label="New item", placeholder="Add new todo...",
              on_change=add_todo, key="new_todo", label_visibility="collapsed")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=f"{index}_{todo}")
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[f"{index}_{todo}"]
        st.rerun()