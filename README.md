
# 📄 PaperPilot — Local Research Paper Assistant (Ollama)

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Streamlit](https://img.shields.io/badge/UI-Streamlit-red)
![LLM](https://img.shields.io/badge/LLM-Ollama-yellowgreen)
![Vector DB](https://img.shields.io/badge/VectorStore-FAISS-blueviolet)
![Status](https://img.shields.io/badge/Status-Working%20Prototype-brightgreen)

---

## 📌 What this project is

**PaperPilot** is a simple, local research paper assistant that lets you:

- Upload a **single PDF document**
- Ask questions in **natural language**
- Get answers **strictly grounded in the uploaded document**

The goal of this project is to understand how **local LLMs** and a **basic Retrieval‑Augmented Generation (RAG)** pipeline work together — without using any cloud APIs.

👉 No OpenAI, no external services, and **no data leaves your machine**.

---

## 🧠 How it works (high level)

Think of the system as a small pipeline:

1. 📄 PDF is loaded and text is extracted  
2. ✂️ Text is split into chunks  
3. 🔢 Embeddings are generated for each chunk  
4. 📚 FAISS stores embeddings for fast similarity search  
5. 🔍 Relevant chunks are retrieved for a question  
6. 🤖 Ollama LLM answers using only those chunks  

This keeps answers **fact‑based** and tied to the document.

---

## 🧩 Project structure (explained)

```
paperpilot-ollama/
│
├── app.py            # Streamlit UI (entry point)
├── pdf_loader.py     # Loads PDF and extracts raw text
├── chunking.py       # Splits text into smaller chunks
├── embeddings.py     # Converts chunks into vector embeddings
├── vector_store.py   # Stores & searches embeddings using FAISS
├── llm_client.py     # Communicates with local Ollama LLM
├── qa.py             # Retrieval + answer generation logic
├── prompts.py        # Prompt templates
├── requirements.txt  # Python dependencies
└── README.md         # Documentation
```

---

## 🔗 How everything connects

- `app.py` controls the flow and UI
- PDF → chunking → embeddings → FAISS index
- User question → similarity search → retrieved chunks
- Chunks + prompt → Ollama → final answer

Each module has **one responsibility**, making the code easy to read and extend.

---

## 🛠️ Technologies used

- Python 3.10+
- Streamlit
- Ollama (local LLM)
- FAISS (vector search)
- Retrieval‑Augmented Generation (RAG)

---

## ⚙️ Setup

### Create virtual environment

```bash
python -m venv .venv
```

Activate:

- Windows:
```bash
.venv\Scripts\Activate.ps1
```

- macOS / Linux:
```bash
source .venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Start Ollama

```bash
ollama serve
ollama pull llama2
```

---

## 🚀 Run the app

```bash
streamlit run app.py
```

Open `http://localhost:8501` in your browser.

---

## 📝 Notes / limitations

- This is a **learning‑focused prototype**
- Best for text‑based PDFs
- No user authentication or persistence
- Performance depends on document size

---

## 👤 Author

**Abinash Prasana Selvanathan**

---

⭐ If you found this useful, consider starring the repo.
