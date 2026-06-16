import json
from pprint import pprint

with open("candidates.jsonl", "r", encoding="utf-8") as f:
    candidate = json.loads(f.readline())

print("\n===== PROFILE =====")
pprint(candidate["profile"])

print("\n===== FIRST 5 SKILLS =====")
pprint(candidate["skills"][:5])

print("\n===== FIRST 2 CAREER ENTRIES =====")
pprint(candidate["career_history"][:2])

print("\n===== REDROB SIGNALS =====")
pprint(candidate["redrob_signals"])