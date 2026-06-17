import streamlit as st
import pandas as pd
import re

st.set_page_config(
    page_title="AI Recruiter Ranker",
    layout="wide"
)

st.title("🤖 AI Recruiter Ranker")
st.subheader("AI-Powered Candidate Ranking Dashboard")

st.info(
    "Compare candidates against a Job Description and get AI-style ranking insights."
)

jd_text = st.text_area(
    "📋 Job Description",
    """RAG
NLP
Embeddings
Python
FAISS
Pinecone
Vector Search
Recommendation Systems""",
    height=180
)

candidate_count = st.selectbox(
    "👥 Number of Candidates",
    [2, 3, 4, 5],
    index=3
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

jd_keywords = []

for skill in re.split(r"[,\\n]", jd_text):

    skill = skill.strip().lower()

    if len(skill) < 2:
        continue

    jd_keywords.append(skill)

for i in range(candidate_count):

    st.markdown(f"## 👤 Candidate {i+1}")

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
        "Python, NLP",
        key=f"skills_{i}"
    )

    score = 0

    if any(x in title.lower() for x in good_titles):
        score += 40

    if 5 <= experience <= 10:
        score += 30

    candidate_skills = [
        x.strip().lower()
        for x in skills.split(",")
        if x.strip()
    ]

    matched_skills = list(
        set(candidate_skills) &
        set(jd_keywords)
    )

    missing_skills = list(
        set(jd_keywords) -
        set(candidate_skills)
    )

    if len(set(jd_keywords)) > 0:
        match_percent = (
            len(matched_skills)
            /
            len(set(jd_keywords))
        ) * 100
    else:
        match_percent = 0

    score += match_percent

    results.append({
        "Candidate": f"Candidate {i+1}",
        "Title": title,
        "Experience": experience,
        "Match %": round(match_percent, 1),
        "Score": round(score, 1),
        "Strengths": ", ".join(matched_skills),
        "Missing": ", ".join(missing_skills[:5])
    })

if st.button("🏆 Analyze Candidates"):

    df = pd.DataFrame(results)

    df = df.sort_values(
        by="Score",
        ascending=False
    ).reset_index(drop=True)

    df["Rank"] = range(
        1,
        len(df) + 1
    )

    winner = df.iloc[0]

    st.success("✅ Analysis Complete")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric(
            "🥇 Best Candidate",
            winner["Candidate"]
        )

    with c2:
        st.metric(
            "🎯 AI Match %",
            f"{winner['Match %']}%"
        )

    with c3:
        st.metric(
            "🏆 Final Score",
            winner["Score"]
        )

    st.subheader("📊 Leaderboard")

    st.dataframe(
        df[
            [
                "Rank",
                "Candidate",
                "Title",
                "Experience",
                "Match %",
                "Score"
            ]
        ],
        use_container_width=True
    )

    st.subheader("🔍 Candidate Insights")

    for _, row in df.iterrows():

        st.markdown(
            f"### {row['Candidate']} — {row['Title']}"
        )

        st.progress(
            int(min(row["Match %"], 100))
        )

        st.write(
            f"🎯 AI Match Score: {row['Match %']}%"
        )

        st.write(
            f"✅ Strengths: {row['Strengths']}"
        )

        st.write(
            f"❌ Missing Skills: {row['Missing']}"
        )

        if row["Match %"] >= 70:
            st.success("⭐ Strong Hire")

        elif row["Match %"] >= 40:
            st.warning("✅ Consider")

        else:
            st.error("❌ Reject")

        st.divider()