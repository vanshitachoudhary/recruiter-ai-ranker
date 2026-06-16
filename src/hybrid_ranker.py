import json
import pandas as pd
from tqdm import tqdm

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
Learning to Rank
Recommendation Systems
Embeddings
Vector Search
RAG
LLMs
NLP
FAISS
Pinecone
Weaviate
Milvus
"""

jd_embedding = model.encode(JD_TEXT)

JD_KEYWORDS = [
    "retrieval",
    "ranking",
    "recommendation",
    "search",
    "embeddings",
    "vector",
    "faiss",
    "pinecone",
    "weaviate",
    "milvus",
    "rag",
    "llm",
    "nlp",
]

GOOD_TITLES = [
    "ai engineer",
    "machine learning engineer",
    "ml engineer",
    "search engineer",
    "relevance engineer",
    "recommendation engineer",
    "nlp engineer",
    "applied scientist",
]

results = []

print("Ranking candidates...")

with open("candidates.jsonl", "r", encoding="utf-8") as f:

    for line in tqdm(f):

        c = json.loads(line)

        profile = c["profile"]

        title = profile["current_title"]
        summary = profile["summary"]

        rule_score = 0

        exp = profile["years_of_experience"]

        if 5 <= exp <= 9:
            rule_score += 25

        if any(x in title.lower() for x in GOOD_TITLES):
            rule_score += 30

        for kw in JD_KEYWORDS:
            if kw in summary.lower():
                rule_score += 5

        skill_names = []

        for skill in c["skills"]:

            s = skill["name"]

            skill_names.append(s)

            if any(k in s.lower() for k in JD_KEYWORDS):
                rule_score += 4

            if skill["proficiency"] == "expert":
                rule_score += 2

        career_text = ""

        for job in c["career_history"]:

            desc = job["description"]

            career_text += " " + desc

            if "ranking" in desc.lower():
                rule_score += 10

            if "retrieval" in desc.lower():
                rule_score += 10

            if "search" in desc.lower():
                rule_score += 8

            if "recommendation" in desc.lower():
                rule_score += 8

        signals = c["redrob_signals"]

        if signals["open_to_work_flag"]:
            rule_score += 10

        rule_score += signals["github_activity_score"] * 0.15
        rule_score += signals["recruiter_response_rate"] * 20

        candidate_text = f"""
        {title}

        {summary}

        {' '.join(skill_names)}

        {career_text}
        """

        candidate_embedding = model.encode(candidate_text)

        semantic_score = cosine_similarity(
            [jd_embedding],
            [candidate_embedding]
        )[0][0]

        final_score = (
            rule_score * 0.7
            +
            semantic_score * 100 * 0.3
        )

        results.append({
    "candidate_id": c["candidate_id"],
    "title": title,
    "score": round(final_score, 4),
    "reasoning":
    (
        f"{round(exp,1)} yrs exp; "
        f"{title}; "
        f"Github={round(signals['github_activity_score'],1)}; "
        f"RespRate={round(signals['recruiter_response_rate'],2)}; "
        f"Semantic={round(semantic_score,3)}"
    )
})

df = pd.DataFrame(results)

df = df.sort_values(
    by=["score", "candidate_id"],
    ascending=[False, True]
).reset_index(drop=True)

top100 = df.head(100).copy()

top100["rank"] = range(1, 101)

submission = top100[
    [
        "candidate_id",
        "rank",
        "score",
        "reasoning"
    ]
]

submission.to_csv(
    "submission_hybrid.csv",
    index=False
)

print("\nSaved submission_hybrid.csv")
print(submission.head(10))