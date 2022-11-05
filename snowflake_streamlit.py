import snowflake.connector
import streamlit as st

st.title("Streamlit + Snowflake Example")
conn = snowflake.connector.connect(**st.secrets["snowflake"])
query = """
    select
        l_returnflag as "return_flag",
        sum(l_quantity) as "sum_qty"
    from
        snowflake_sample_data.tpch_sf1.lineitem
    where
        l_shipdate <= dateadd(day, -90, to_date('1998-12-01'))
    group by
        1
"""

with conn.cursor() as cur:
    cur.execute(query)
    tcph_df = cur.fetch_pandas_all()

st.dataframe(tcph_df)

st.write("Quantity by Return Flag Over Time")
st.bar_chart(data=tcph_df, x="return_flag", y="sum_qty")
