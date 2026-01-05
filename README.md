<!-- ========================= -->
<!-- PaperPilot README (v2)    -->
<!-- ========================= -->

<h1 align="center">📄 PaperPilot — Local Research Paper Assistant (Ollama)</h1>

<p align="center">
  Upload a PDF → ask questions → get answers grounded in the PDF text (simple local RAG).
</p>

<p align="center">
  <img alt="Python" src="https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white" />
  <img alt="Streamlit" src="https://img.shields.io/badge/UI-Streamlit-FF4B4B?logo=streamlit&logoColor=white" />
  <img alt="Ollama" src="https://img.shields.io/badge/LLM-Ollama-000000?logo=ollama&logoColor=white" />
  <img alt="FAISS" src="https://img.shields.io/badge/Vector_Search-FAISS-6E56CF" />
  <img alt="Status" src="https://img.shields.io/badge/Status-Working%20Prototype-2EA043" />
</p>

<p align="center">
  <em>Runs fully on your machine. No cloud LLM calls.</em>
</p>

---

## 📌 What this project is

**PaperPilot** is a small Streamlit app that lets you:

- 📄 Upload **one PDF** (text-based PDFs work best)
- ❓ Ask questions in normal English
- ✅ Get answers **based on the PDF content** (not random guessing)

This was built mainly as a hands-on learning project to understand how a basic **Retrieval‑Augmented Generation (RAG)** pipeline works with a **local LLM**.

> **Note:** I’m not training my own LLM here — the app uses **Ollama** to run the model locally.

---

## 🧠 How it works (high level)

Think of it like a simple pipeline:

1. 📄 Load the PDF and extract text
2. ✂️ Split text into smaller chunks
3. 🔢 Turn chunks into embeddings (vectors)
4. 📚 Store/search those embeddings with **FAISS**
5. 🔎 Retrieve the most relevant chunks for your question
6. 🦙 Send only those chunks to **Ollama** to generate the answer

Result: answers stay **tied to the PDF**, and you’re not sending the full document to any external API.

---

## 🧩 Project structure (explained)

```text
paperpilot-ollama/
├─ app.py            # Streamlit UI + orchestrates the full flow
├─ pdf_loader.py     # Loads the PDF and extracts raw text
├─ chunking.py       # Splits text into smaller overlapping chunks
├─ embeddings.py     # Creates embeddings (vectors) for chunks
├─ vector_store.py   # FAISS index: add/search vectors + return top matches
├─ llm_client.py     # Talks to Ollama (generate answers from context)
├─ qa.py             # Retrieval + prompt + answer formatting (RAG glue)
├─ prompts.py        # Prompt templates (system + formatting)
├─ requirements.txt  # Python dependencies
└─ README.md         # Documentation
```

<details>
  <summary><b>How the files connect (big picture)</b> (click to expand)</summary>

<br>

- **`app.py`** is the entry point. It takes the PDF + question from the UI and calls the pipeline.
- **PDF flow:** `pdf_loader.py` → `chunking.py` → `embeddings.py` → `vector_store.py` (FAISS index)
- **Question flow:** question → `vector_store.py` similarity search → top chunks → `qa.py` → `llm_client.py` (Ollama)

A quick visual:

```text
PDF -> pdf_loader -> chunking -> embeddings -> FAISS (vector_store)
                                   ^
                                   |
Question -> similarity search ------+-> top chunks -> qa -> Ollama -> Answer
```

</details>

---

## ⚙️ Setup

### 1) Create a virtual environment (recommended)

```bash
python -m venv .venv
```

Activate:

**Windows (PowerShell):**
```powershell
.venv\Scripts\Activate.ps1
```

**macOS / Linux:**
```bash
source .venv/bin/activate
```

### 2) Install dependencies

```bash
pip install -r requirements.txt
```

### 3) Install + start Ollama

Install Ollama from the official site and start the server.

Typical commands:

```bash
ollama serve
```

Pull a model (example):
```bash
ollama pull llama3
```

> You can change the model name in the code/config if you’re using something else.

---

## 🚀 Run the app

```bash
streamlit run app.py
```

Then open the URL shown in the terminal (usually `http://localhost:8501`).

---

## 🎥 Demo video (add yours here)

https://github.com/user-attachments/assets/f8eec450-8cfe-47e7-b4e0-f50c5b7bdea9

```

---

## ✅ Notes / limitations (keeping it honest)

- This is a **learning-focused prototype**
- Works best with **text-based PDFs** (scanned image PDFs may not extract clean text)
- No authentication, user accounts, or persistence (everything is in-memory for a run)
- Performance depends on PDF size + your local model

---

## 🙌 Credits

- **Ollama** — local model runner (this project calls Ollama; it does not train an LLM)
- **FAISS** — similarity search / vector indexing
- **Streamlit** — UI framework

---

## 👤 Author

**Abinash Prasana Selvanathan**

⭐ If you found it useful, feel free to star the repo.
