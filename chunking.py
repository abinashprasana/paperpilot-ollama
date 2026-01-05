from typing import List


def chunk_text(text: str, chunk_size: int = 1200, overlap: int = 150) -> List[str]:
    """
    Simple safe chunking with overlap.
    - chunk_size/overlap are in characters (not tokens).
    """
    text = (text or "").replace("\r", "").strip()
    if not text:
        return []

    if overlap >= chunk_size:
        overlap = max(0, chunk_size // 4)

    chunks = []
    start = 0
    n = len(text)

    while start < n:
        end = min(start + chunk_size, n)
        chunk = text[start:end].strip()
        if chunk:
            chunks.append(chunk)

        if end == n:
            break

        start = max(0, end - overlap)

    return chunks