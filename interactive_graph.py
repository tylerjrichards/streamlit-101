import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

st.title("Interactive Random Number Generator")
n_rand = st.slider("Select Number of Random Numbers to Generate", min_value=5, value=50)
dist_selection = st.selectbox(
    label="Select Your Distribution",
    options=["Normal Distribution", "Uniform Distribution"],
)
if dist_selection == "Normal Distribution":
    chart_data = pd.DataFrame(np.random.randn(n_rand, 3), columns=["a", "b", "c"])
else:
    chart_data = pd.DataFrame(np.random.rand(n_rand, 3), columns=["a", "b", "c"])

binned_data = pd.cut(chart_data["a"], bins=[-3, -2, -1, 0, 1, 2, 3])
st.write(chart_data["a"])
st.write(binned_data)
st.write(chart_data)
altair_chart = (
    alt.Chart(chart_data)
    .mark_bar()
    .encode(
        alt.X("a", bin=True),
        y="count()",
    )
)
st.altair_chart(altair_chart)
