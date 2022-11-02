import pandas as pd
import snowflake.connector
import streamlit as st

st.image("cloud.png")
st.title("Weather Analysis")


conn = snowflake.connector.connect(
    **st.secrets["snowflake"], client_session_keep_alive=True
)

query = """
    select
        l_returnflag,
        l_linestatus,
        sum(l_quantity) as sum_qty,
        sum(l_extendedprice) as sum_base_price
    from
        snowflake_sample_data.tpch_sf1.lineitem
    where
        l_shipdate <= dateadd(day, -90, to_date('1998-12-01'))
    group by
        1, 2
"""

with conn.cursor() as cur:
    cur.execute(query)
    tcph_df = cur.fetch_pandas_all()

st.dataframe(tcph_df)


st.stop()

weather_sql_query = """
    SELECT TRIM(V['city']['name'], '"') as "name",
        V['city']['coord']['lat'] as "lat",
        V['city']['coord']['lon'] as "lon",
        V['data'][0]['humidity'] as "humidity",
        T as "time_recorded"
    FROM snowflake_sample_data.weather.daily_14_total
    WHERE V['city']['name'] LIKE '%z%'
    LIMIT 1000
    """
weather_data = run_query(weather_sql_query)
st.dataframe(weather_data, height=200)
st.map(weather_data)
