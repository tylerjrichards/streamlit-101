import streamlit as st

x = st.slider(label="User Inputa")
st.write(f"{x} squared is {x*x}")
