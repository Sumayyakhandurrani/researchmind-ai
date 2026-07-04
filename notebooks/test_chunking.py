import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.parser.pdf_reader import extract_text_from_pdf
from app.parser.text_chunker import split_text

pdf_path = "data/raw/sample.pdf"

text = extract_text_from_pdf(pdf_path)
chunks = split_text(text)

print(f"Total chunks: {len(chunks)}")

print("\nFirst chunk:\n")
print(chunks[0])