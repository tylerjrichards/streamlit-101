import numpy as np
import pandas as pd
import streamlit as st

st.set_page_config(layout="wide")

st.title("Interactive Random Number Generator")
n_rand = st.slider("Select Number of Random Numbers to Generate", min_value=5, value=50)

# get both chart data
chart_data_normal = chart_data = pd.DataFrame(
    np.random.randn(n_rand, 3), columns=["a", "b", "c"]
)
chart_data_uniform = pd.DataFrame(np.random.rand(n_rand, 3), columns=["a", "b", "c"])
col_a, col_b = st.columns(2)

with col_a:
    st.write("Normal Distribution Graph")
    st.line_chart(chart_data_normal)

with col_b:
    st.write("Uniform Distribution Graph")
    st.line_chart(chart_data_uniform)
