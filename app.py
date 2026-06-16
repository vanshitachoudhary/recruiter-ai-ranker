import streamlit as st

st.set_page_config(page_title="AI Recruiter Ranker")

st.title("🤖 AI Recruiter Ranker")
st.write("Hybrid Candidate Ranking Demo")

title = st.text_input("Current Title")

experience = st.number_input(
    "Years of Experience",
    min_value=0.0,
    max_value=50.0,
    value=5.0
)

skills = st.text_area(
    "Skills (comma separated)",
    "Python, Machine Learning, NLP"
)

if st.button("Rank Candidate"):

    score = 0

    good_titles = [
        "ai engineer",
        "machine learning engineer",
        "ml engineer",
        "search engineer",
        "nlp engineer",
        "applied scientist",
    ]

    if any(t in title.lower() for t in good_titles):
        score += 40

    if 5 <= experience <= 10:
        score += 30

    score += len(skills.split(",")) * 3

    st.success(f"Final Score: {score}")

    if score > 80:
        st.write("⭐ Strong Candidate")
    elif score > 50:
        st.write("✅ Good Candidate")
    else:
        st.write("⚠️ Average Candidate")