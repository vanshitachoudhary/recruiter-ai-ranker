import json
import pandas as pd
from tqdm import tqdm

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
    "qdrant",
    "milvus",
    "elasticsearch",
    "opensearch",
    "llm",
    "rag",
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
    "applied ml engineer",
]

BAD_TITLES = [
    "marketing",
    "sales",
    "hr",
    "recruiter",
    "designer",
]

results = []

print("Loading candidates...")

with open("candidates.jsonl", "r", encoding="utf-8") as f:

    for line in tqdm(f):

        c = json.loads(line)

        score = 0

        profile = c["profile"]

        title = profile["current_title"].lower()
        summary = profile["summary"].lower()

        exp = profile["years_of_experience"]

        # Experience
        if 5 <= exp <= 9:
            score += 20

        if 6 <= exp <= 8:
            score += 15

        # Current title
        if any(x in title for x in GOOD_TITLES):
            score += 25

        if any(x in title for x in BAD_TITLES):
            score -= 50

        # Summary keywords
        for kw in JD_KEYWORDS:
            if kw in summary:
                score += 4

        # Skills
        for skill in c["skills"]:

            s = skill["name"].lower()

            if any(k in s for k in JD_KEYWORDS):
                score += 3

            if skill["proficiency"] == "expert":
                score += 2

        # Career history
        for job in c["career_history"]:

            desc = job["description"].lower()
            jt = job["title"].lower()

            if "ranking" in desc:
                score += 12

            if "retrieval" in desc:
                score += 12

            if "recommendation" in desc:
                score += 10

            if "search" in desc:
                score += 10

            if "embedding" in desc:
                score += 10

            if "learning-to-rank" in desc:
                score += 15

            if "ml pipeline" in desc:
                score += 5

            if "recommendation" in jt:
                score += 8

            if "search engineer" in jt:
                score += 10

            if "ai engineer" in jt:
                score += 8

            if "machine learning" in jt:
                score += 8

        # Recruiter signals
        signals = c["redrob_signals"]

        if signals["open_to_work_flag"]:
            score += 10

        score += signals["github_activity_score"] * 0.15
        score += signals["recruiter_response_rate"] * 20
        score += signals["saved_by_recruiters_30d"] * 0.5
        score += signals["search_appearance_30d"] * 0.02

        if signals["notice_period_days"] <= 30:
            score += 5

        results.append(
            {
                "candidate_id": c["candidate_id"],
                "name": profile["anonymized_name"],
                "title": profile["current_title"],
                "score": round(score, 2),
            }
        )

df = pd.DataFrame(results)

df = df.sort_values(
    by=["score", "candidate_id"],
    ascending=[False, True]
).reset_index(drop=True)

# Top 100
top100 = df.head(100).copy()

top100["rank"] = range(1, 101)

top100["reasoning"] = (
    top100["title"]
    + " matched AI/ML search, retrieval, ranking and recruiter-signal criteria."
)

submission = top100[
    ["candidate_id", "rank", "score", "reasoning"]
]

submission.to_csv(
    "submission.csv",
    index=False
)

print("\nSaved submission.csv")
print(submission.head(10))