from prompts import build_prompt


def answer_question(question, embedder, store, llm, top_k=6, temperature=0.2):
    q_vec = embedder.embed_query(question)
    hits = store.search(q_vec, top_k=top_k)

    context_chunks = [h["text"] for h in hits]
    prompt = build_prompt(question, context_chunks)

    answer = llm.generate(prompt, temperature=temperature)

    return {"answer": answer, "context": hits}
