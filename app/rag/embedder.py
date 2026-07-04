from sentence_transformers import SentenceTransformer

class Embedder:
    def __init__(self, model_name="all-MiniLM-L6-v2"):
        print("Loading embedding model...")
        self.model = SentenceTransformer(model_name)
        print("Model loaded!")

    def encode(self, texts):
        return self.model.encode(
            texts,
            convert_to_numpy=True,
            show_progress_bar=True
        )