import faiss
import numpy as np
import os
import pickle

class FAISSStore:
    def __init__(self, dim=384):
        self.dim = dim
        self.index = faiss.IndexFlatL2(dim)
        self.text_chunks = []

    def add(self, embeddings, chunks):
        """
        embeddings: numpy array (n, dim)
        chunks: list of text
        """
        self.index.add(np.array(embeddings).astype("float32"))
        self.text_chunks.extend(chunks)

    def search(self, query_embedding, k=5):
        """
        Returns top-k similar chunks
        """
        D, I = self.index.search(
            np.array([query_embedding]).astype("float32"),
            k
        )

        results = []
        for idx in I[0]:
            results.append(self.text_chunks[idx])

        return results

    def save(self, path="data/vector_db/faiss.index"):
        faiss.write_index(self.index, path)

        with open(path + ".pkl", "wb") as f:
            pickle.dump(self.text_chunks, f)

    def load(self, path="data/vector_db/faiss.index"):
        self.index = faiss.read_index(path)

        with open(path + ".pkl", "rb") as f:
            self.text_chunks = pickle.load(f)