import streamlit as st

# cookies
st.title("counter example")

# initialize
if 'count' not in st.session_state: # dictionary
    # st.session_state['count'] = 0
    st.session_state.counter = 0

increament = st.button('add 1')
if increament:
    st.session_state['count'] += 1
    
st.write('count = ', st.session_state['count'])


