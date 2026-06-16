from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

print("Loading model...")

model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2",
    local_files_only=True
)

JD_TEXT = """
Senior AI Engineer
Search
Retrieval
Ranking
RAG
Embeddings
Vector Search
Recommendation Systems
LLMs
"""

jd_embedding = model.encode(JD_TEXT)

candidate_text = """
Senior Machine Learning Engineer
Built retrieval systems
RAG pipelines
Embeddings
Learning to Rank
"""

candidate_embedding = model.encode(candidate_text)

score = cosine_similarity(
    [jd_embedding],
    [candidate_embedding]
)[0][0]

print("Semantic Score:", round(float(score), 4))