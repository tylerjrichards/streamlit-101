import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

st.title("Interactive Random Number Generator")
n_rand = st.slider("Select Number of Random Numbers to Generate", min_value=5, value=50)
chart_data = pd.DataFrame(np.random.randn(n_rand, 3), columns=["a", "b", "c"])
line_chart = (
    alt.Chart(chart_data).mark_line().encode(x="a", y="b", color=alt.value("red"))
)
st.altair_chart(line_chart)

st.line_chart(chart_data)
