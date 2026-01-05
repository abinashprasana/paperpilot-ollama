import time
import streamlit as st

from pdf_loader import extract_text_from_pdf
from chunking import chunk_text
from embeddings import Embedder
from vector_store import FaissStore
from llm_client import OllamaLLM
from qa import answer_question


def reset_pdf_state():
    keys = ["pdf_ready", "pdf_text", "chunks", "store"]
    for k in keys:
        st.session_state.pop(k, None)


st.set_page_config(page_title="PaperPilot (Ollama)", layout="wide")
st.title("📄 PaperPilot — Local Research Paper Assistant (Ollama)")
st.caption("Upload a PDF, ask questions, get answers grounded in the PDF content (local + free).")


# ---------------------------
# Sidebar settings
# ---------------------------
with st.sidebar:
    st.header("⚙️ Settings")

    ollama_url = st.text_input("Ollama URL", value=st.session_state.get("ollama_url", "http://localhost:11434"))
    st.session_state["ollama_url"] = ollama_url

    # probe client to load models
    probe = OllamaLLM(base_url=ollama_url, model="")

    model_list = []
    model_fetch_error = None
    try:
        model_list = probe.list_models()
    except Exception as e:
        model_fetch_error = str(e)

    if model_list:
        model_name = st.selectbox("Ollama model", options=model_list, index=0)
        st.caption("✅ Loaded from your local Ollama models")
    else:
        model_name = st.text_input("Ollama model", value="gemma3:4b")
        st.caption("⚠️ Couldn’t fetch models. You can type one manually.")

    embed_model = st.text_input("Embedding model", value=st.session_state.get("embed_model", "all-MiniLM-L6-v2"))
    st.session_state["embed_model"] = embed_model

    chunk_size = st.slider("Chunk size", 400, 2000, st.session_state.get("chunk_size", 1200), step=50)
    overlap = st.slider("Overlap", 0, 400, st.session_state.get("overlap", 150), step=10)
    top_k = st.slider("Top chunks", 2, 12, st.session_state.get("top_k", 6))
    temperature = st.slider("Temperature", 0.0, 1.0, float(st.session_state.get("temperature", 0.2)), step=0.05)

    st.session_state["chunk_size"] = chunk_size
    st.session_state["overlap"] = overlap
    st.session_state["top_k"] = top_k
    st.session_state["temperature"] = temperature

    if st.button("🧹 Reset PDF", use_container_width=True):
        reset_pdf_state()
        st.success("Cleared PDF from session. Upload again.")
        st.rerun()


# ---------------------------
# Ollama status badge (auto)
# ---------------------------
llm = OllamaLLM(base_url=ollama_url, model=model_name)

if "ollama_status" not in st.session_state:
    ok, msg = llm.health_check()
    st.session_state["ollama_status"] = (ok, msg)

ok, msg = st.session_state["ollama_status"]

if ok:
    st.success(f"🟢 Ollama Connected — {msg}")
else:
    st.error(f"🔴 Ollama Not Ready — {msg}")


# ---------------------------
# Top "Check Ollama" button (above the explanation)
# ---------------------------
c1, c2, c3 = st.columns([1, 2, 3])
with c1:
    if st.button("🧪 Check Ollama", use_container_width=True):
        ok2, msg2 = llm.health_check()
        st.session_state["ollama_status"] = (ok2, msg2)
        st.rerun()

with c2:
    if model_fetch_error:
        st.caption("Couldn’t load model list (still fine if you type model manually).")
    else:
        st.caption("Model list loaded from Ollama ✅")

st.divider()


# ---------------------------
# What this app does
# ---------------------------
st.markdown("### ✅ What this app is doing")
st.markdown(
    """
- Reads the PDF text  
- Splits it into chunks  
- Creates embeddings (vectors) locally  
- Searches relevant chunks using FAISS  
- Sends only those chunks to Ollama to answer  

So the answer is based on your PDF, not random guessing.
""".strip()
)

st.divider()


# ---------------------------
# Upload PDF
# ---------------------------
st.subheader("📎 Upload a PDF")
uploaded = st.file_uploader("Drop your PDF here", type=["pdf"])

if not uploaded:
    st.info("Upload a PDF to start.")
    st.stop()

pdf_bytes = uploaded.getvalue()  # important: safe, doesn't get consumed

# Build pipeline once per session (simple + clean)
if not st.session_state.get("pdf_ready"):
    t0 = time.time()
    progress = st.progress(0, text="Reading PDF text...")

    text = extract_text_from_pdf(pdf_bytes)
    progress.progress(20, text="Checking extracted text...")

    MIN_TEXT_CHARS = 400
    if not text or len(text.strip()) < MIN_TEXT_CHARS:
        st.warning(
            "⚠️ This PDF has very little selectable text (maybe scanned). "
            "Try a text-based PDF or OCR it and re-upload."
        )
        st.stop()

    st.session_state["pdf_text"] = text

    progress.progress(35, text="Chunking text...")
    chunks = chunk_text(text, chunk_size=chunk_size, overlap=overlap)
    st.session_state["chunks"] = chunks

    progress.progress(55, text="Loading embedding model...")
    embedder = Embedder(model_name=embed_model)

    progress.progress(70, text="Creating embeddings...")
    vectors = embedder.embed_texts(chunks)

    progress.progress(90, text="Building FAISS index...")
    store = FaissStore(dim=vectors.shape[1])
    store.add(vectors, chunks)

    st.session_state["store"] = store
    st.session_state["pdf_ready"] = True

    progress.progress(100, text="Done ✅")
    st.caption(f"Build finished in **{time.time() - t0:.2f}s**")


# Preview
with st.expander("🔎 Preview extracted text (first ~1200 chars)", expanded=False):
    st.code(st.session_state["pdf_text"][:1200], language="text")

st.success(f"PDF ready ✅  Chunks: **{len(st.session_state['chunks'])}**")

st.divider()


# ---------------------------
# Ask Q
# ---------------------------
st.subheader("💬 Ask your question")
question = st.text_input("Type your question", placeholder="e.g., What is the main objective of this paper?")

if st.button("Ask PaperPilot", type="primary"):
    if not question.strip():
        st.warning("Type a question first 🙂")
        st.stop()

    ok3, msg3 = llm.health_check()
    st.session_state["ollama_status"] = (ok3, msg3)

    if not ok3:
        st.error(f"Ollama not ready ❌ — {msg3}")
        st.stop()

    embedder = Embedder(model_name=embed_model)
    store = st.session_state["store"]

    with st.spinner("Thinking..."):
        result = answer_question(
            question=question.strip(),
            embedder=embedder,
            store=store,
            llm=llm,
            top_k=top_k,
            temperature=temperature
        )

    st.markdown("## ✅ Answer")
    st.write(result["answer"])

    with st.expander("🧩 Context used (transparency)", expanded=False):
        for i, item in enumerate(result["context"], start=1):
            st.markdown(f"**Chunk {i}** (score: `{item['score']:.3f}`)")
            st.write(item["text"])
            st.divider()