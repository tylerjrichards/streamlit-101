import numpy as np
import pandas as pd
import streamlit as st

n_rand = st.slider("Select Number of Random Numbers to Generate", min_value=1)
chart_data = pd.DataFrame(np.random.randn(n_rand, 3), columns=["a", "b", "c"])
st.write(chart_data)
st.line_chart(chart_data)
