from sentence_transformers import SentenceTransformer

print("Loading model...")

model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)

text = "Senior Machine Learning Engineer with RAG, Retrieval and Ranking experience"

embedding = model.encode(text)

print("Embedding length:", len(embedding))
print("Done.")