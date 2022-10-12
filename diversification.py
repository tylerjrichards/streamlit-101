import numpy as np
import pandas as pd
import streamlit as st

st.title("Interactive Random Number Generator")
n_rand = st.slider("Select Number of Random Numbers to Generate", min_value=5, value=50)
dist_selection = st.radio(
    label="Select Your Distribution",
    options=["Normal Distribution", "Uniform Distribution"],
)
third_col_name = st.text_input("Name one of the lines!")
if dist_selection == "Normal Distribution":
    chart_data = pd.DataFrame(
        np.random.randn(n_rand, 3), columns=["a", "b", third_col_name]
    )
else:
    chart_data = pd.DataFrame(
        np.random.rand(n_rand, 3), columns=["a", "b", third_col_name]
    )
st.line_chart(chart_data)


checkbox_result = st.checkbox("Check for balloons")
if checkbox_result:
    st.balloons()

button_result = st.button("Click for balloons")
if button_result:
    st.balloons()
