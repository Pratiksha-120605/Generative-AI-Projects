import os
from dotenv import load_dotenv
load_dotenv()

import streamlit as st
from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

## LangSmith tracking (optional)
os.environ['LANGCHAIN_API_KEY'] = os.getenv('LANGCHAIN_API_KEY')
os.environ["LANGCHAIN_TRACKING_V2"] = "true"
os.environ['LANGCHAIN_PROJECT'] = os.getenv('LANGCHAIN_PROJECT')

## Prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please respond to the question asked."),
        ("human", "Question: {question}")
    ]
)

## Streamlit UI
st.title("LangChain Demo with Llama 3.1")
input_text = st.text_input("What question do you have in mind?")

## Ollama model
llm = Ollama(model="llama3.1")
output_parser = StrOutputParser()

chain = prompt | llm | output_parser

if input_text:
    st.write(chain.invoke({"question": input_text}))
