# 📄 RAG Document Q&A System using Groq + Llama3

A Retrieval-Augmented Generation (RAG) based Document Question-Answering System built using Groq API, Llama3, LangChain, FAISS, Ollama Embeddings, and Streamlit.

This project allows users to ask questions from research papers (PDFs) stored locally and generates accurate, context-aware responses using vector similarity search and large language models.

---

## 🚀 Features

- 📂 Load multiple PDF documents from a folder
- ✂️ Automatic document chunking
- 🔎 Vector similarity search using FAISS
- 🧠 Context-aware answering with Llama3 (Groq API)
- ⚡ High-speed inference using Groq
- 🎨 Clean and interactive Streamlit UI
- 📚 View retrieved document chunks for transparency
- 🧩 Modular and easy-to-extend architecture

---

## 🏗️ Architecture Flow

User Question  
→ Document Embedding  
→ FAISS Vector Store  
→ Similarity Search  
→ Context Retrieval  
→ Llama3 via Groq  
→ Final Answer  

---

## 🛠 Tech Stack

- Python
- Streamlit
- LangChain
- Groq API
- Llama3 (llama3-8b-8192)
- FAISS (Vector Database)
- Ollama Embeddings
- python-dotenv

---

## 📂 Project Structure
```
rag-document-qa-groq-llama3/
│
├── app.py
├── requirements.txt
├── .env
└── research_papers/
├── paper1.pdf
├── paper2.pdf
```

### 🧠 How It Works

- PDFs are loaded from the research_papers folder.

- Documents are split into smaller chunks.

- Each chunk is converted into embeddings using Ollama.

- Embeddings are stored in FAISS vector database.

- User asks a question.

- Relevant document chunks are retrieved using similarity search.

- Llama3 (via Groq API) generates an accurate answer using retrieved context.
-----------------------
## 📌 Key Concepts Demonstrated

- Retrieval-Augmented Generation (RAG)

- Vector Databases (FAISS)

- Local Embeddings with Ollama

- Groq API integration

- Prompt Engineering

- Streamlit-based AI Application Development

## 💡 Future Improvements

- PDF Upload feature from UI

- Chat history with memory

- Streaming responses

- Hybrid search (keyword + vector)

- Deployment on cloud (Render / AWS / GCP)

## 👩‍💻 Author

Built as part of hands-on Generative AI learning and experimentation.  
