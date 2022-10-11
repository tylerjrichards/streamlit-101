import streamlit as st

st.write("hey")

if "app1_state" not in st.session_state:
    st.session_state["app1_state"] = True

st.write(st.session_state)
