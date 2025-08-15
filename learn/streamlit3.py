import streamlit as st

# cookies
st.title("counter example")

# initialize
if 'counter' not in st.session_state: # dictionary
    # st.session_state['count'] = 0
    st.session_state.counter = 1

# *args
# def increament_counter(*args): # tuple
#     st.session_state.counter += args[0]
#     st.session_state.counter -= args[1]

# st.header(f"Execution times: {st.session_state.counter}")

# button_status = st.button('Rerun', 
#                           key="reset", 
#                           help="counter", 
#                           on_click=increament_counter, 
#                           args=(5,3)) # on_click: automatically construct reset_key


# **kwargs
def increament_counter(**kwargs): # dictionary
    st.session_state.counter += kwargs['first']
    st.session_state.counter -= kwargs['second']

st.header(f"Execution times: {st.session_state.counter}")

button_status = st.button('Rerun', 
                          key="reset", 
                          help="counter", 
                          on_click=increament_counter, 
                          kwargs={'first':5, 'second':3}) 
# on_click: automatically construct reset_key
