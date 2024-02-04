import streamlit as st  # For creating the web app interface
import os  # For interacting with environment variables
from dotenv import load_dotenv  # For loading variables from .env file
import requests  # For making HTTP requests

# Load environment variables (e.g., API keys)
load_dotenv()

# Set page title and display logo
st.set_page_config(page_title="Atomic: Query Engine")  # Set page title
st.image("./logo.png", width=300)  # Display logo
st.title("AI: Query Engine")  # Set page header

# Clear chat history button
if st.button("Clear Chat"):  # Clear chat history if button is clicked
    st.session_state.messages = []

# Initial greeting from the assistant
with st.chat_message("assistant"):  # Display message as the assistant
    st.markdown("Hi, How may I help you?")

# Load chat history from session state (if any)
if "messages" not in st.session_state:  # Initialize chat history if needed
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:  # Iterate through chat history
    with st.chat_message(message["role"]):  # Display messages with appropriate roles
        st.markdown(message["content"])

# User input box
if prompt := st.chat_input("What is up?"):  # Get user input
    st.session_state.messages.append({"role": "user", "content": prompt})  # Add user message to history
    with st.chat_message("user"):  # Display user's message
        st.markdown(prompt)

    # Generate assistant's response using a separate endpoint
    with st.chat_message("assistant"):  # Display response as the assistant
        url = os.getenv('URL')  # Load API endpoint URL from environment variable
        data = {"prompt": f"{prompt}"}  # Prepare data for request
        response = requests.post(url, json=data)  # Send request to endpoint
        answer = response.text  # Extract response text
        st.markdown(answer)  # Display the response

    st.session_state.messages.append({"role": "assistant", "content": response.text})  # Add response to history
