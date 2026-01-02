SYSTEM_MSG = """You are PaperPilot, a local research paper assistant.
Rules:
- Answer ONLY using the provided PDF context.
- If it’s not in the context, say: "I couldn't find that in the PDF."
- Keep it clear and student-friendly.
"""


def build_prompt(question: str, context_chunks: list[str]) -> str:
    context = "\n\n---\n\n".join(context_chunks)

    return f"""{SYSTEM_MSG}

PDF Context:
{context}

Question:
{question}

Answer:
"""