import os
import streamlit as st
import pandas as pd
from llama_index import Document, GPTVectorStoreIndex, ServiceContext, VectorStoreIndex
from llama_index.llms import OpenAI
import openai
import speech_recognition as sr  # For voice-to-text functionality

# Set app layout
st.set_page_config(page_title="Elderly Caregiver Support", layout="wide")

# Load the OpenAI API key from Streamlit secrets
openai.api_key = st.secrets["openai_key"]

# GitHub raw URL for the CSV file
csv_url = "https://raw.githubusercontent.com/Amritkj001/caregiver-chatbot/main/data/data.csv"

# Load the CSV file from the GitHub URL into a pandas DataFrame
try:
    df = pd.read_csv(csv_url)
except Exception as e:
    st.error(f"Error loading data: {e}")

# Convert the pandas DataFrame into documents for the GPTVectorStoreIndex
docs = [Document(text=row.to_string()) for _, row in df.iterrows()]

# Set up the OpenAI service context with higher max_tokens and slightly higher temperature
service_context = ServiceContext.from_defaults(
    llm=OpenAI(model="gpt-4", temperature=0.7, max_tokens=1000)
)

# Create the index
index = GPTVectorStoreIndex.from_documents(documents=docs, service_context=service_context)

# Increase similarity_top_k to get more documents
query_engine = index.as_query_engine(similarity_top_k=5)

# ---- Streamlit interface starts here ----

# Sidebar with font size scale, logo, and description
with st.sidebar:
    # Placeholder for app logo
    st.image("https://via.placeholder.com/150", caption="Care Kaki Logo", use_column_width=True)

    # App description
    st.write("**Care Kaki**")
    st.write("This app is designed to help caregivers of the elderly find resources, services, and support.")
    st.write("Use the tabs to navigate through features like the chatbot for advice, maps to locate care services, and a forum to connect with others.")

    # Font size scale
    font_size = st.slider("Adjust Font Size", min_value=12, max_value=36, value=16)

# Apply dynamic font size for content, but exclude the header and subheader
st.markdown(f"""
    <style>
    .dynamic-content {{
        font-size: {font_size}px !important;
    }}
    .short-select-box {{
        width: 200px !important;
    }}
    .microphone-icon {{
        vertical-align: middle;
        margin-left: 10px;
    }}
    </style>
""", unsafe_allow_html=True)

# Header and Subheader with fixed font sizes
st.markdown("""
    <h1 style='text-align: center; color: #4CAF50; font-size: 48px;'>Care Kaki</h1>
    <h2 style='text-align: center; color: #6D6D6D; font-size: 24px;'>One-stop platform for support and resources for caregivers of the elderly</h2>
""", unsafe_allow_html=True)

# Horizontal Navigation Bar using buttons
st.markdown("""
    <style>
    .nav-tabs {
        display: flex;
        justify-content: center;
        border-bottom: 1px solid #ddd;
        background-color: #f8f9fa;
        padding: 10px 0;
    }
    .nav-tabs button {
        font-size: 16px;
        padding: 10px 20px;
        margin-right: 10px;
        background-color: #4CAF50;
        color: white;
        border: none;
        cursor: pointer;
    }
    .nav-tabs button:hover {
        background-color: #45a049;
    }
    </style>
""", unsafe_allow_html=True)

# Store the selected page in session state
if "page" not in st.session_state:
    st.session_state.page = "Chatbot"  # Default page

# Navigation buttons
col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("Chatbot"):
        st.session_state.page = "Chatbot"
with col2:
    if st.button("Maps"):
        st.session_state.page = "Maps"
with col3:
    if st.button("Forum"):
        st.session_state.page = "Forum"
with col4:
    if st.button("Useful Links"):
        st.session_state.page = "Links"

# Function to convert voice to text
def recognize_speech_from_microphone():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    with microphone as source:
        st.write("Listening...")
        audio = recognizer.listen(source)

    try:
        response = recognizer.recognize_google(audio)
        return response
    except sr.RequestError:
        return "API request error."
    except sr.UnknownValueError:
        return "Unable to recognize speech."

# Page content with dynamic font size
with st.container():
    st.markdown(f"<div class='dynamic-content'>", unsafe_allow_html=True)

    if st.session_state.page == "Chatbot":
        st.subheader("Caregiver Chatbot")

        # Shortened language selector and microphone icon beside it
        col1, col2 = st.columns([0.7, 0.1])
        with col1:
            language = st.selectbox("Select your language:", ["English", "Mandarin", "Malay", "Tamil"], key="language", help="Select a language for the chatbot.")
        with col2:
            if st.button("🎤 Voice Input"):
                voice_text = recognize_speech_from_microphone()
                st.session_state.user_input = voice_text  # Store the voice text

        # Text input for the user's question
        user_input = st.text_input("Ask me anything (Text or Voice):", st.session_state.get("user_input", ""))

        # Process the input and generate an answer
        if st.button("Submit"):
            if user_input:
                # Query the engine with the user's question
                response = query_engine.query(user_input)

                # Extract and display the answer
                answer = str(response)
                st.write("Answer:", answer)

    elif st.session_state.page == "Maps":
        st.subheader("Caregiver Support Services Map")

        # Dropdown filter with "Nursing Home" and "Senior Day Care Centre"
        selected_service = st.selectbox("Filter by service type:", ["Nursing Home", "Senior Day Care Centre"])

        st.write(f"Showing results for: {selected_service}")
        # Placeholder for maps integration
        st.map()  # Replace with actual map data integration

    elif st.session_state.page == "Forum":
        st.subheader("Caregiver Forum")

        # Forum categories
        st.write("**Categories**")
        categories = ["General Caregiving", "Elderly Health", "Mental Health Support", "Legal Issues", "Financial Assistance"]
        selected_category = st.selectbox("Choose a category:", categories)

        # User name input
        st.write("**Your Information**")
        user_name = st.text_input("Enter your name:")

        # User post input
        st.write("**Post Your Thoughts**")
        user_post = st.text_area("Share your thoughts or ask a question:")

        # Submit button
        if st.button("Post"):
            if user_name and user_post:
                st.success(f"Thank you {user_name}, your post has been submitted under {selected_category}.")
                # Here you can add functionality to save the post in a database or storage
            else:
                st.error("Please enter both your name and your thoughts before posting.")

        # Display recent posts (This is a placeholder for actual post data)
        st.write("**Recent Posts in this Category**")
        st.write("1. User: JohnDoe - 'How can I manage stress while caregiving?'")
        st.write("2. User: JaneSmith - 'What are some tips for maintaining elderly health?'")

        # Comments section
        st.write("**Comments on Post 1**")
        comment_1 = st.text_input("Leave a comment on this post:")
        if st.button("Submit Comment on Post 1"):
            if comment_1:
                st.success("Your comment has been added.")
            else:
                st.error("Please enter a comment before submitting.")

    elif st.session_state.page == "Links":
        st.subheader("Useful Resources for Caregivers")
        # List of links (you can add actual URLs here)
        st.write("- [Government Caregiver Schemes](https://example.com)")
        st.write("- [Elderly Care Centers](https://example.com)")
        st.write("- [Mental Health Support](https://example.com)")

