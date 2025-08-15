import streamlit as st
import tensorflow as tf
import numpy as np


def load_and_get_tflite_model(model_path):
    interpreter = tf.lite.Interpreter(model_path=model_path)
    interpreter.allocate_tensors()

    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()

    # inner function: closure
    # the memory will not be killed
    # the model is constructed at the first call
    def predict(x):
        interpreter.set_tensor(input_details[0]['index'], np.array([[x]], dtype=np.float32).reshape(input_details[0]['shape']))
        interpreter.invoke()
        return interpreter.get_tensor(output_details[0]['index'])   
    
    return predict


st.set_page_config(layout="centered")
st.title("TensorFlow Lite Demo")

prompt = st.chat_input("Please input x value:")
if prompt:
    input_value = float(prompt)
    tflite_model_path = 'linear_model.tflite'
    predict = load_and_get_tflite_model(tflite_model_path)
    st.write(predict(input_value))