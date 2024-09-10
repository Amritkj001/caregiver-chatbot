import streamlit as st
import openai
import pandas as pd
import requests

# Set the page configuration immediately, before any other Streamlit commands
st.set_page_config(page_title="Care Kaki", layout="wide")

# Load the OpenAI API key from Streamlit secrets
openai.api_key = st.secrets["openai_key"]

# Function to load dataset from GitHub
@st.cache
def load_data(url):
    data = pd.read_csv(url)
    return data

# Load your dataset from GitHub
DATA_URL = "https://raw.githubusercontent.com/Amritkj001/caregiver-chatbot/main/data/data.csv"  # Replace with the actual GitHub URL
data = load_data(DATA_URL)

# GPT-4 chatbot function
def generate_gpt4_response(user_input):
    response = openai.Completion.create(
        engine="gpt-4",
        prompt=user_input,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0  # Set temperature to 0 for deterministic responses
    )
    return response.choices[0].text.strip()

# Streamlit app layout
def main():
    st.title("Caregiver Chatbot using GPT-4")
    st.write("This chatbot uses GPT-4 to answer your questions based on the dataset and general knowledge.")

    # User input for the chatbot
    user_input = st.text_input("Enter your question here:")
    
    if user_input:
        # Generate response
        response = generate_gpt4_response(user_input)
        
        # Display response
        st.write("Chatbot Response:")
        st.write(response)

if __name__ == "__main__":
    main()


