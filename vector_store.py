import faiss
import numpy as np


class FaissStore:
    """
    FAISS similarity store (cosine via normalized vectors).
    """

    def __init__(self, dim: int):
        self.index = faiss.IndexFlatIP(dim)
        self.texts: list[str] = []

    def add(self, vectors: np.ndarray, texts: list[str]):
        if vectors.dtype != np.float32:
            vectors = vectors.astype("float32")

        self.index.add(vectors)
        self.texts.extend(texts)

    def search(self, query_vec: np.ndarray, top_k: int = 6):
        if query_vec.dtype != np.float32:
            query_vec = query_vec.astype("float32")

        scores, idxs = self.index.search(query_vec, top_k)

        results = []
        for score, idx in zip(scores[0], idxs[0]):
            if idx == -1:
                continue
            results.append({"score": float(score), "text": self.texts[int(idx)]})
        return results
