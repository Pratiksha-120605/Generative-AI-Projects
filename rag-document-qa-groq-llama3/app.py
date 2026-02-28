import streamlit as st
import os
import time
from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import ChatPromptTemplate


# -------------------- Load Environment -------------------- #
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

# -------------------- Streamlit UI -------------------- #
st.set_page_config(page_title="RAG Q&A with Groq", layout="wide")
st.title("📄 RAG Document Q&A using Groq + Llama3")

# -------------------- Load LLM -------------------- #
llm = ChatGroq(
    groq_api_key=groq_api_key,
    model_name="llama3-8b-8192"   # Correct Groq model
)

# -------------------- Prompt Template -------------------- #
prompt = ChatPromptTemplate.from_template("""
Answer the question based only on the context provided.
Provide the most accurate response.

<context>
{context}
</context>

Question: {question}
""")

# -------------------- Create Vector Store -------------------- #
def create_vector_embedding():
    if "vectors" not in st.session_state:

        # Embeddings (using local Ollama)
        embeddings = OllamaEmbeddings(model="nomic-embed-text")

        # Load PDFs from folder
        loader = PyPDFDirectoryLoader("research_papers")
        docs = loader.load()

        # Split documents
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200
        )
        final_docs = text_splitter.split_documents(docs)

        # Create FAISS vector store
        vectors = FAISS.from_documents(final_docs, embeddings)

        # Save in session
        st.session_state.vectors = vectors

        st.success("✅ Document embedding completed!")

# -------------------- Button to Embed -------------------- #
if st.button("Create Document Embeddings"):
    create_vector_embedding()

# -------------------- User Input -------------------- #
user_prompt = st.text_input("Ask a question from the research papers")

# -------------------- RAG Pipeline -------------------- #
if user_prompt:

    if "vectors" not in st.session_state:
        st.warning("⚠ Please create document embeddings first.")
        st.stop()

    document_chain = create_stuff_documents_chain(llm, prompt)
    retriever = st.session_state.vectors.as_retriever()

    retrieval_chain = create_retrieval_chain(retriever, document_chain)

    start = time.time()
    response = retrieval_chain.invoke({"question": user_prompt})
    end = time.time()

    st.write("### 🧠 Answer:")
    st.write(response["answer"])

    st.write(f"⏱ Response time: {round(end-start,2)} seconds")

    # Show retrieved chunks
    with st.expander("📚 Retrieved Document Chunks"):
        for i, doc in enumerate(response["context"]):
            st.write(f"**Chunk {i+1}:**")
            st.write(doc.page_content)
            st.write("-" * 80)