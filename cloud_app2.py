import streamlit as st
import pandas as pd
import openai
# Set the page configuration immediately, before any other Streamlit commands
st.set_page_config(page_title="Care Kaki", layout="wide")
# Load the OpenAI API key from Streamlit secrets
openai.api_key = st.secrets["openai_key"]
# Load the CSV file (caching to avoid reloading)
@st.cache_data
def load_data():
    return pd.read_csv('data.csv')
df = load_data()
# Function to generate a response based on user input
def generate_response(question, df):
    if question in df['Question'].values:
        answer = df[df['Question'] == question]['Answer'].values[0]
    else:
        # If the question is not found in the CSV, use GPT-3.5 Turbo to generate a response
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful assistant focused on helping backpackers."},
                {"role": "user", "content": question}
            ]
        )
        answer = response['choices'][0]['message']['content']
    return answer
# Main function to run the app
def main():
    # Title and description
    st.title("GA Backpacker Chatbot")
    st.subheader("Your personal assistant for all things backpacking! Ask me anything about travel tips, destinations, and more.")
    # User input section
    st.write("### What would you like to know?")
    user_input = st.text_input("", placeholder="Enter your travel question here...")
    # If the user submits a question, generate a response
    if st.button("Submit"):
        if user_input.strip() == "":
            st.warning("Please enter a question before submitting.")
        else:
            with st.spinner("Preparing your travel tips..."):
                response = generate_response(user_input, df)
                st.write("### Response:")
                st.write(response)
    # Footer section
    st.markdown(
        """
        <style>
        .footer {
            position: fixed;
            left: 0;
            bottom: 0;
            width: 100%;
            background-color: #F1F1F1;
            color: black;
            text-align: center;
            padding: 10px;
        }
        </style>
        <div class="footer">
            <p>GA Backpacker Chatbot © 2024 | Powered by OpenAI GPT-3.5 Turbo</p>
        </div>
        """,
        unsafe_allow_html=True
    )
# Run the app
if __name__ == "__main__":
    main()

