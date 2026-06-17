import streamlit as st
import pandas as pd

st.set_page_config(page_title="AI Recruiter Ranker", layout="wide")

st.title("🤖 AI Recruiter Ranker")
st.subheader("Multi-Candidate Comparison Dashboard")

candidate_count = st.selectbox(
    "Number of Candidates",
    [2, 3, 4, 5],
    index=1
)

results = []

good_titles = [
    "ai engineer",
    "machine learning engineer",
    "ml engineer",
    "search engineer",
    "nlp engineer",
    "applied scientist",
    "recommendation engineer",
]

for i in range(candidate_count):

    st.markdown(f"## Candidate {i+1}")

    title = st.text_input(
        f"Current Title {i+1}",
        key=f"title_{i}"
    )

    experience = st.number_input(
        f"Years of Experience {i+1}",
        min_value=0.0,
        max_value=50.0,
        value=5.0,
        key=f"exp_{i}"
    )

    skills = st.text_area(
        f"Skills {i+1}",
        "Python, Machine Learning, NLP",
        key=f"skills_{i}"
    )

    score = 0

    if any(t in title.lower() for t in good_titles):
        score += 40

    if 5 <= experience <= 10:
        score += 30

    score += len(skills.split(",")) * 3

    results.append({
        "Candidate": f"Candidate {i+1}",
        "Title": title,
        "Experience": experience,
        "Score": score
    })

if st.button("🏆 Compare Candidates"):

    df = pd.DataFrame(results)

    df = df.sort_values(
        by="Score",
        ascending=False
    ).reset_index(drop=True)

    df["Rank"] = range(1, len(df) + 1)

    st.success("Ranking Complete")

    winner = df.iloc[0]

    st.metric(
        "🥇 Best Candidate",
        winner["Candidate"],
        f"Score {winner['Score']}"
    )

    st.dataframe(df, use_container_width=True)