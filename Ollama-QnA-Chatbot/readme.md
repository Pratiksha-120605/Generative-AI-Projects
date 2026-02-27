# 🤖 Simple Q&A Chatbot with Ollama (Streamlit + LangChain)

## 📌 Overview

This project is a simple Question & Answer chatbot built using:

- **Streamlit** (Frontend UI)
- **LangChain** (LLM orchestration)
- **Ollama** (Local LLMs)

The chatbot allows users to ask questions and get responses from locally running Large Language Models.

---

## 🚀 Features

- Local LLM integration using Ollama
- Clean Streamlit UI
- Model selection from sidebar
- Adjustable temperature
- LangChain prompt template usage
- Output parsing with StrOutputParser

---

## 🛠 Tech Stack

- Python  
- Streamlit  
- LangChain  
- Ollama  

---

## 📂 Project Structure
```
1-Ollama-Chatbot/
│
├── app.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Install Ollama

Download and install Ollama from:
https://ollama.com

Start Ollama: ``` Ollama serve ```

---

### 2️⃣ Pull Required Models

Example:
```
ollama run llama3.1
ollama run gemma2
ollama run phi3
```
---
## Check installed models:
``` ollama list ```

---
### 4️⃣ Create Virtual Environment
```
python -m venv venv
venv\Scripts\activate
```
----
### 5️⃣ Install Dependencies
```
pip install -r requirements.txt
```
----
### 6️⃣ Run the Application
```
python -m streamlit run app.py
```
----

---

## 🎯 How It Works

1. User enters a question  
2. Prompt template formats the message  
3. Selected Ollama model generates response  
4. LangChain parses output  
5. Streamlit displays result  

---

## 📌 Learning Objective

This project demonstrates:

- Integrating local LLMs using Ollama
- Building LLM apps with Streamlit
- Using LangChain prompt templates
- Creating interactive AI applications

---

## 👩‍💻 Author

Built as part of hands-on learning in Generative AI.

---

⭐ Feel free to fork and experiment!
