from app.rag.embedder import Embedder
from app.database.faiss_store import FAISSStore


class SearchService:

    def __init__(self):
        self.embedder = Embedder()

        self.store = FAISSStore(dim=384)
        self.store.load()

    def search(self, question, k=5):

        query_embedding = self.embedder.encode([question])[0]

        results = self.store.search(query_embedding, k)

        return results