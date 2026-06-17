# 🤖 AI Recruiter Ranker

An AI-powered candidate ranking system that automatically evaluates and ranks candidates against a target job description using a hybrid scoring approach.

## 🚀 Live Demo

https://recruiter-ai-ranker-blqtzxpczw457kup8ifko8.streamlit.app/

## 📂 GitHub Repository

https://github.com/vanshitachoudhary/recruiter-ai-ranker

---

## 📌 Overview

Recruiters often need to evaluate thousands of candidates for a single role. This project automates candidate ranking by combining:

* Rule-Based Candidate Scoring
* Job Description Skill Matching
* Recruiter Signal Analysis
* Candidate Comparison Dashboard

The system generates ranked candidate recommendations and provides transparent reasoning for hiring decisions.

---

## ✨ Features

### Candidate Ranking

* Automatic candidate scoring
* Multi-candidate comparison
* Rank generation

### Job Description Matching

* Skill extraction from job descriptions
* Candidate skill matching
* Missing skill identification

### Recruiter Dashboard

* Interactive Streamlit interface
* Candidate leaderboard
* Match score visualization
* Hiring recommendations

### Explainability

* Strength analysis
* Missing skill analysis
* Transparent scoring

---

## 🛠 Tech Stack

* Python
* Pandas
* Streamlit
* Scikit-Learn
* Sentence Transformers
* Machine Learning

---

## 📊 Scoring Logic

The ranking engine combines multiple signals:

1. Candidate Title Relevance
2. Years of Experience
3. Skill Match Percentage
4. Job Description Alignment
5. Recruiter Signals

Final candidates are ranked according to their overall score.

---

## 📁 Project Structure

```text
recruiter-ai-ranker/
│
├── app.py
├── requirements.txt
├── submission_hybrid.csv
├── README.md
│
├── src/
│   ├── hybrid_ranker.py
│   ├── semantic_ranker.py
│   └── rank_candidates.py
│
└── outputs/
```

---

## ▶️ Run Locally

Clone the repository:

```bash
git clone https://github.com/vanshitachoudhary/recruiter-ai-ranker.git
cd recruiter-ai-ranker
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

---

## 🎯 Use Cases

* Recruiter Productivity
* Talent Acquisition
* Resume Screening
* Candidate Shortlisting
* AI-Assisted Hiring

---

## 📈 Future Improvements

* Resume Upload Support
* Semantic Candidate Matching
* Embedding-Based Ranking
* LLM-Powered Candidate Insights
* Advanced Recruiter Analytics

---

## 👨‍💻 Author

Vanshita Choudhary

Built as an AI-powered recruiter ranking project for hackathon and portfolio showcase purposes.
