import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.services.search_service import SearchService

search = SearchService()

question = input("Ask a question: ")

results = search.search(question)

print("\nTop Relevant Chunks\n")

for i, chunk in enumerate(results):

    print("=" * 80)

    print(f"Chunk {i+1}")

    print(chunk[:600])

    print()