import os
import streamlit as st
from dotenv import load_dotenv
from groq import Groq

# Load environment variables from .env file
load_dotenv()

# Get the GROQ API Key from the environment
api_key = os.getenv("GROQ_API_KEY")

# If the API key is not found, show an error in the app
if not api_key:
    st.error("Please set the GROQ_API_KEY in the .env file.")
    st.stop()

# Initialize the Groq client with the API key
client = Groq(api_key=api_key)

# Streamlit app UI
st.title("GROQ API with Llama-3.3 Integration")
st.write("This app uses GROQ API to interact with Llama-3.3 for generating responses based on the user input.")

# User input section
user_input = st.text_area("Ask me anything about fast language models:")

if st.button("Generate Response"):
    if user_input:
        # Make API call to GROQ
        chat_completion = client.chat.completions.create(
            messages=[{"role": "user", "content": user_input}],
            model="llama-3.3-70b-versatile",
        )
        # Display the response from the model
        st.write(chat_completion.choices[0].message.content)
    else:
        st.error("Please enter a question.")
