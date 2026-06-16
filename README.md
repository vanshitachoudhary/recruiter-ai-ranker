# Intelligent Candidate Discovery & Ranking System

## Overview

This solution ranks candidates for the Redrob Senior AI Engineer role.

Instead of relying only on keyword matching, the ranking system attempts to understand the hiring intent behind the job description.

The model combines candidate skills, career history, recruiter signals, availability signals, and production AI experience to identify strong matches.

---

## Ranking Factors

### Experience Fit

Preferred range:

- 5 to 9 years experience
- Additional boost for 6 to 8 years

### Role Relevance

Preferred titles:

- AI Engineer
- Machine Learning Engineer
- Search Engineer
- Recommendation Engineer
- NLP Engineer
- Applied Scientist
- Applied ML Engineer

Negative titles:

- Marketing
- Sales
- Recruiter
- HR
- Designer

### Skills Match

The ranking rewards candidates with experience in:

- Retrieval
- Ranking
- Search
- Recommendation Systems
- Embeddings
- Vector Search
- Pinecone
- Weaviate
- Qdrant
- Milvus
- Elasticsearch
- OpenSearch
- LLMs
- RAG
- NLP

### Career History Evidence

Strong weight is given to actual work experience described in career history.

Examples:

- Ranking systems
- Retrieval systems
- Recommendation systems
- Search infrastructure
- Learning-to-Rank
- Embedding pipelines
- ML production systems

### Behavioral Signals

The following Redrob signals are incorporated:

- Open to Work
- Recruiter Response Rate
- GitHub Activity
- Saved by Recruiters
- Search Appearances
- Notice Period

---

## Key Design Choice

The challenge explicitly states that keyword matching alone is insufficient.

Therefore, the ranking system prioritizes evidence of real-world ownership of:

- Retrieval systems
- Ranking systems
- Search systems
- Recommendation systems

rather than simply counting AI-related keywords.

---

## Outputs

Generated files:

- outputs/top100.csv
- outputs/top10.csv

Candidates are sorted by descending relevance score.