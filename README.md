# 📄 PaperPilot — Local Research Paper Assistant (Ollama)

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![Streamlit](https://img.shields.io/badge/UI-Streamlit-red?logo=streamlit)
![Ollama](https://img.shields.io/badge/LLM-Ollama-green)
![FAISS](https://img.shields.io/badge/Vector%20Store-FAISS-orange)
![Status](https://img.shields.io/badge/Status-Working%20Prototype-brightgreen)

---

## 📌 What this project is

**PaperPilot** is a simple **local research paper assistant** that lets you:

- Upload **one PDF document**
- Ask questions in natural language
- Get answers **strictly grounded in the uploaded document**

It uses a lightweight **Retrieval-Augmented Generation (RAG)** pipeline with a **local LLM (Ollama)**.  
No cloud APIs, no data leaving your machine.

This project was built as a **student learning project** to understand how document-based QA systems work in practice.

---

## 🎯 Why this is useful

- 📖 Quickly explore long research papers  
- 🔍 Ask focused questions instead of scrolling PDFs  
- 🧠 Learn how RAG pipelines work (end-to-end)  
- 🖥️ Runs fully **offline** using local models  

---

## ✨ Features

- 📄 Upload a single PDF (research paper, report, notes)
- ✂️ Chunking of document text
- 🧮 Vector embeddings + similarity search
- 🤖 Local LLM answering using retrieved chunks
- 🧠 Answers stay **within document context**
- 🖥️ Clean Streamlit UI

---

## 🧠 How it works (high level)

1. PDF text extraction  
2. Text chunking with overlap  
3. Embedding generation  
4. FAISS similarity search  
5. LLM answers from retrieved chunks  

---

## 🗂️ Project structure

```text
paperpilot-ollama/
├── app.py
├── pdf_loader.py
├── chunking.py
├── embeddings.py
├── vector_store.py
├── llm_client.py
├── qa.py
├── prompts.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup

```bash
python -m venv .venv
```

```bash
pip install -r requirements.txt
```

Make sure Ollama is installed and running.

---

## 🚀 Run

```bash
streamlit run app.py
```

---

## 🧪 Notes

- Prototype meant for learning
- Single-document focus
- Simple, readable design

---

## 👤 Author

**Abinash Prasana Selvanathan**

⭐ Star the repo if you find it useful.
