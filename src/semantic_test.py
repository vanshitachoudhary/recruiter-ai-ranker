from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)

jd = """
Senior AI Engineer
Search
Retrieval
Ranking
RAG
Embeddings
LLMs
"""

candidate1 = """
Senior Machine Learning Engineer
Built retrieval systems
RAG pipelines
Embeddings
Learning to Rank
"""

candidate2 = """
Marketing Manager
SEO
Content Writing
Brand Growth
"""

jd_emb = model.encode(jd)

c1_emb = model.encode(candidate1)
c2_emb = model.encode(candidate2)

sim1 = cosine_similarity(
    [jd_emb],
    [c1_emb]
)[0][0]

sim2 = cosine_similarity(
    [jd_emb],
    [c2_emb]
)[0][0]

print("AI Candidate:", sim1)
print("Marketing Candidate:", sim2)