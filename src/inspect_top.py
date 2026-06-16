import json

TARGET_ID = "CAND_0018499"

with open("candidates.jsonl", "r", encoding="utf-8") as f:

    for line in f:

        c = json.loads(line)

        if c["candidate_id"] == TARGET_ID:

            print("\nPROFILE\n")
            print(c["profile"])

            print("\nSKILLS\n")
            for s in c["skills"][:20]:
                print(s)

            print("\nCAREER HISTORY\n")
            for h in c["career_history"]:
                print(h)
                print()

            print("\nSIGNALS\n")
            print(c["redrob_signals"])

            break