# Import necessary libraries
import streamlit as st
import json
import os
import requests
import socket


# Function to make an inference request to the FastAPI server
def inference(input_text):
    # Construct the request URL with the input text as a query parameter
    req = "http://localhost:8085/api/v1/inference"
    # Make the GET request to the FastAPI server
    response = requests.get(req, params={'input_text': input_text})
    # Display the 'Output' heading in the Streamlit app
    st.markdown(f'## Output')
    # Parse the JSON response from the server and display it in the Streamlit app
    st.write(response.json())


# Display the title of the Streamlit app
st.title('FastAPI Demo')
# Create a text input field for users to enter text
input_text = st.text_input(label="Write something", autocomplete="off", value="text")
# Call the inference function with the user's input text
inference(input_text)

