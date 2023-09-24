import json
with open("database/feedbacks/stars_feedbacks.json", "r", encoding="utf-8") as f:
    old: list = json.load(f)
print(old)