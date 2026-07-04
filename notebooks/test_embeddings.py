import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.parser.pdf_reader import extract_text_from_pdf
from app.parser.text_chunker import split_text
from app.rag.embedder import Embedder

pdf_path = "data/raw/sample.pdf"

text = extract_text_from_pdf(pdf_path)
chunks = split_text(text)

embedder = Embedder()

embeddings = embedder.encode(chunks)

print(f"Number of chunks: {len(chunks)}")
print(f"Embedding shape: {embeddings.shape}")
print("First embedding (first 10 values):")
print(embeddings[0][:10])