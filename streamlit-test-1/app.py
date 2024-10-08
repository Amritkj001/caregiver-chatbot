import streamlit as st
from llama_index import VectorStoreIndex, ServiceContext, Document, StorageContext, load_index_from_storage
from llama_index.llms import OpenAI
import openai
from PIL import Image
import requests
import base64



st.set_page_config(page_title="Chat with Your .....", page_icon="👩🏻‍🏫", layout="centered", initial_sidebar_state="auto", menu_items=None)

#Context

# Set OpenAI API key
openai.api_key = st.secrets.openai_key


# URL of the image you want to display
image_url = "https://imageio.forbes.com/specials-images/imageserve/6117af8b679cc9098dd4eb2e/Adult-hands-holding-older-hands-showing-the-importance-of-caregiving-/960x0.jpg"

# Display the image in Streamlit using HTML and CSS
st.markdown(f"""
<style>
.shifted-image {{
    display: block;
    margin-left: auto;
    margin-right: auto;
    width: 600px;
    height: 360px; /* Adjust the height as needed */
    margin-top: 50px; /* Adjust this value to bring the image closer to the top */
}}
</style>
<img class="shifted-image" src="{image_url}" />
""", unsafe_allow_html=True)


# Display centered text
#st.markdown("<p style='text-align: center;'>Welcome to the AI!</p>", unsafe_allow_html=True)


@st.cache_resource(show_spinner=False)
def load_data():
    with st.spinner(text="This may take 1-2 minutes."):
        
        # Rebuild the storage context
        storage_context = StorageContext.from_defaults(persist_dir="./data/index.vecstore")

        # Load the index
        index = load_index_from_storage(storage_context)

        # Load the finetuned model 
        ft_model_name = "ft:gpt-3.5-turbo-1106:personal:fengshui:9IzbaIn8"
        ft_context = ServiceContext.from_defaults(llm=OpenAI(model=ft_model_name, temperature=0.3), 
        context_window=2048, 
        
        system_prompt="""
       You are an AI.
        """
        )           
        return index

index = load_data()
chat_engine = index.as_chat_engine(chat_mode="openai", verbose=True)

if "messages" not in st.session_state.keys(): # Initialize the chat messages history
    st.session_state.messages = [
        {"role": "assistant", "content": "Ask Me Questions 😊"}
    ]

if prompt := st.chat_input("Ask Me questions related to care giving"):
    # Save the original user question to the chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.session_state.new_question = True

    # Create a detailed prompt for the chat engine
    chat_history = ' '.join([message["content"] for message in st.session_state.messages])
    detailed_prompt = f"{chat_history} {prompt}"

if "new_question" in st.session_state.keys() and st.session_state.new_question:
   for message in st.session_state.messages: # Display the prior chat messages
       with st.chat_message(message["role"]):
           st.write(message["content"])
   st.session_state.new_question = False # Reset new_question to False

# If last message is not from assistant, generate a new response
if st.session_state.messages[-1]["role"] != "assistant":
   with st.chat_message("assistant"):
       with st.spinner("Calculating..."):
           response = chat_engine.chat(detailed_prompt)
           st.write(response.response)
           # Append the assistant's detailed response to the chat history
           st.session_state.messages.append({"role": "assistant", "content": response.response})
