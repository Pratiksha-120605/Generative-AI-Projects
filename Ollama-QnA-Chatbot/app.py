import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.llms import Ollama
from langchain_core.output_parsers import StrOutputParser
import os 
from dotenv import load_dotenv

load_dotenv()

## Langchain Tracking
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = "Simple Q&A Chatbot With OLLAMA"

## Promp Template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("user", "{question}"),
])

def generate_response(question,engine,temperature,max_tokens):
    llm = Ollama(model=engine)
    output_parser = StrOutputParser()
    chain = prompt | llm | output_parser
    answer=chain.invoke({"question": question})
    return answer

## Streamlit UI
engine = st.sidebar.selectbox("Select Engine", ["gemma2:latest", "llama3.1:latest","gemma:2b","gemma3:1b","gemma3:27b"])
temperature = st.sidebar.slider("Temperature", 0.0, 1.0, 0.7)
max_tokens = st.sidebar.slider("Max Tokens", 50, 300, 150)

#main interface for user phi3:latest
st.title("Simple Q&A Chatbot With OLLAMA")
st.write("Welcome to the Simple Q&A Chatbot With OLLAMA")
user_input=st.text_input("You: ")

if user_input:
    answer = generate_response(user_input,engine,temperature,max_tokens)
    st.write(answer)

else:
    st.write("Ask a question")