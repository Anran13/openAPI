from tools import taipei
import streamlit as st

@st.dialog("Message:")
def vote(error):
    st.write(error)

try:
    youbikes = taipei.get_youbikes()
except Exception as error:
    vote(error)
    st.write("Try later!")
    st.stop()

st.dataframe(youbikes)
