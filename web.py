import streamlit as st
import functions

todos = functions.get_todos()

st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity")


for index, todo in enumerate(todos):
    st.checkbox(todo, key=f"todo_{index}")

st.text_input(label="Enter a todo:", placeholder="Add new todo....")