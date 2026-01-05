# 📄 PaperPilot — Local Research Paper Assistant (Ollama)

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Streamlit](https://img.shields.io/badge/UI-Streamlit-red)
![Ollama](https://img.shields.io/badge/LLM-Ollama-green)
![FAISS](https://img.shields.io/badge/VectorStore-FAISS-orange)
![Status](https://img.shields.io/badge/Status-Working%20Prototype-success)

---

PaperPilot is a **local research paper assistant** that allows you to upload a PDF and ask questions directly based on its content.  
All responses are generated using only the uploaded document, following a simple and transparent Retrieval-Augmented Generation (RAG) approach.

This project was built as a hands-on learning exercise while exploring local LLMs and document-based question answering.

---

## 🔍 What this project does

- Uploads a research paper (PDF)
- Extracts and cleans text from the document
- Splits text into smaller chunks
- Converts chunks into vector embeddings
- Retrieves the most relevant chunks for each question
- Uses a local Ollama model to generate grounded answers
- Shows both the answer and the supporting document context

---

## 🧠 Why PaperPilot

Reading and navigating long academic papers can be time-consuming.  
PaperPilot helps by surfacing relevant information quickly while ensuring answers remain grounded in the original document.

Everything runs locally, keeping your documents private.

---

## 🏗️ How it works

1. PDF Loader extracts text  
2. Chunking splits text into manageable parts  
3. Embeddings convert text to vectors  
4. FAISS retrieves relevant chunks  
5. Ollama generates answers using retrieved context  
6. Streamlit provides the user interface  

---

## 🗂️ Project structure

```
paperpilot-ollama/
├─ app.py
├─ pdf_loader.py
├─ chunking.py
├─ embeddings.py
├─ vector_store.py
├─ llm_client.py
├─ qa.py
├─ prompts.py
├─ requirements.txt
└─ README.md
```

---

## ⚙️ Setup & run

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
ollama pull gemma:2b
streamlit run app.py
```

Open in browser:
```
http://localhost:8501
```

---

## 🔌 Ollama connection check

The app includes a button to verify whether Ollama is running and reachable before sending questions.

---

## 👤 Author

Abinash Prasana Selvanathan

---

## ⭐ Notes

This project focuses on clarity and practical learning rather than unnecessary complexity, making it a solid foundation for future improvements.
