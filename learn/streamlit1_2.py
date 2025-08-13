import streamlit as st
import tools

sitenames = tools.get_sitename(excel_name='aqi.xlsx')
#  Object notation

# add_selectbox = st.sidebar.selectbox(
#     "Sitenames",
#     (sitenames)
# )

with st.sidebar:
     add_selectbox = st.selectbox(
        "Sitenames", 
        sitenames
    )
     st.title(f"{add_selectbox}")

data = tools.get_aqi(excel_name='aqi.xlsx')

select_item = []
# for item in data:
#      if item['sitename'] == add_selectbox:
#           select_item.append(item)

select_item = [item for item in data if item['sitename'] == add_selectbox]
st.table(data=select_item)