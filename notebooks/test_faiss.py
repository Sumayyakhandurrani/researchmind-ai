import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.parser.pdf_reader import extract_text_from_pdf
from app.parser.text_chunker import split_text
from app.rag.embedder import Embedder
from app.database.faiss_store import FAISSStore

# Load PDF
pdf_path = "data/raw/sample.pdf"
text = extract_text_from_pdf(pdf_path)

# Chunk
chunks = split_text(text)

# Embeddings
embedder = Embedder()
embeddings = embedder.encode(chunks)

# FAISS store
store = FAISSStore(dim=384)
store.add(embeddings, chunks)

# Save index
store.save()

print("FAISS index created successfully!")