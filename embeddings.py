import numpy as np
from sentence_transformers import SentenceTransformer


class Embedder:
    """
    Local embeddings (free).
    Default is fast + decent.
    """

    def __init__(self, model_name="all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)

    def embed_texts(self, texts: list[str]) -> np.ndarray:
        vecs = self.model.encode(
            texts,
            convert_to_numpy=True,
            normalize_embeddings=True,
            show_progress_bar=False
        )
        return vecs.astype("float32")

    def embed_query(self, text: str) -> np.ndarray:
        vec = self.model.encode(
            [text],
            convert_to_numpy=True,
            normalize_embeddings=True,
            show_progress_bar=False
        )
        return vec.astype("float32")