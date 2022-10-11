import streamlit as st

st.write("hey")

if "app2_state" not in st.session_state:
    st.session_state["app2_state"] = True


st.write(st.session_state)
