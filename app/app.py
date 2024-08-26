import streamlit as st
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, StorageContext, load_index_from_storage
from llama_index.llms.openai import OpenAI
import time
from dotenv import load_dotenv
import os
from pathlib import Path
from typing import Generator

# Constants
STREAM_SPEED = 0.05  # Adjust this value to control the stream speed (in seconds)
DATA_DIR = "data"
PAGE_TITLE = "Genos Docs"
PAGE_HEADER = "Chat"
PAGE_SUBHEADER = "Ask me anything about Shakespeare's Sonnets!"
STORAGE_DIR = "./storage"  # Directory to store the index

@st.cache_resource
def load_environment_variables() -> None:
    current_dir = Path(__file__).resolve().parent
    dotenv_path = current_dir / '.env'
    load_dotenv(dotenv_path)
    
    required_vars = ['OPENAI_API_KEY']  # Add other required variables
    for var in required_vars:
        if not os.getenv(var):
            raise EnvironmentError(f"Missing required environment variable: {var}")

@st.cache_resource
def load_data_and_create_index() -> VectorStoreIndex:
    if os.path.exists(STORAGE_DIR):
        # Load the index if it already exists
        storage_context = StorageContext.from_defaults(persist_dir=STORAGE_DIR)
        index = load_index_from_storage(storage_context)
    else:
        # Create a new index if it doesn't exist
        documents = SimpleDirectoryReader(DATA_DIR).load_data()
        index = VectorStoreIndex.from_documents(documents)
        index.storage_context.persist(persist_dir=STORAGE_DIR)
    return index

@st.cache_resource
def setup_query_engine():
    llm = OpenAI(model="gpt-3.5-turbo", streaming=True)
    index = load_data_and_create_index()
    return index.as_query_engine(streaming=True, llm=llm)

def setup_streamlit_page() -> None:
    st.set_page_config(page_title=PAGE_TITLE, layout="wide")
    st.header(PAGE_HEADER)
    st.write(PAGE_SUBHEADER)

def init_chat_history() -> None:
    if "messages" not in st.session_state:
        st.session_state.messages = []

def display_chat_history() -> None:
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

def get_chat_history() -> str:
    return "\n".join([f"{msg['role']}: {msg['content']}" for msg in st.session_state.messages])

def stream_response(streaming_response: Generator, message_placeholder) -> str:
    full_response = ""
    for text in streaming_response.response_gen:
        full_response += text
        message_placeholder.markdown(full_response + "▌")
        time.sleep(STREAM_SPEED)
    message_placeholder.markdown(full_response)
    return full_response

def main() -> None:
    try:
        setup_streamlit_page()
        load_environment_variables()
         
        # Setup query engine (cached)
        query_engine = setup_query_engine()
        
        init_chat_history()
        display_chat_history()
        
        if prompt := st.chat_input("Ask me anything"):
            with st.chat_message("user"):
                st.markdown(prompt)
            st.session_state.messages.append({"role": "user", "content": prompt})
            
            with st.chat_message("assistant"):
                message_placeholder = st.empty()
                chat_history = get_chat_history()
                streaming_response = query_engine.query(f"Chat history:\n{chat_history}\n\nUser's latest question: {prompt}")
                full_response = stream_response(streaming_response, message_placeholder)
            
            st.session_state.messages.append({"role": "assistant", "content": full_response})
    
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()