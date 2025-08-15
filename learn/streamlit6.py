import streamlit as st
import numpy as np
import pandas as pd

st.set_page_config(layout="wide") # Use the full page width

st.title("Arranging Charts with Streamlit Layouts")

# --- Create some sample data ---
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

# --- 1. Using st.columns to place charts side-by-side ---
st.header("1. Side-by-side with `st.columns`")
st.write("You can specify column widths. Here, the second column is twice as wide as the first (`[1, 2]`).")

col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("Chart in Column 1")
    st.bar_chart(chart_data)

with col2:
    st.subheader("Chart in Column 2")
    st.line_chart(chart_data)

st.write("---")

# --- 2. Using st.tabs to organize charts ---
st.header("2. Organizing with `st.tabs`")
st.write("Place charts in different tabs to keep the interface clean.")

tab1, tab2, tab3 = st.tabs(["Bar Chart", "Line Chart", "Area Chart"])

with tab1:
    st.subheader("A Bar Chart")
    st.bar_chart(chart_data)

with tab2:
    st.subheader("A Line Chart")
    st.line_chart(chart_data)

with tab3:
    st.subheader("An Area Chart")
    st.area_chart(chart_data)

st.write("---")

# --- 3. Using st.expander to show/hide charts ---
st.header("3. Hiding charts with `st.expander`")
st.write("Use an expander if a chart is not always needed.")

with st.expander("Click to see the chart"):
    st.subheader("Chart inside an expander")
    st.bar_chart(chart_data)
