# Author: RockMan
# CreateTime: 2024/11/26
# FileName: hello
# Description: simple introduction of the code

import streamlit as st

st.write('hello')

conn = st.connection('upsrod', type='sql', ttl=600, max_entries=40)

sql = 'select distinct cc.portfoliono from upsrod.core_carrybondholds cc '
raw = conn.query(sql)

st.dataframe(raw)
