import json

def load_data():
    with open("symptom_data.json", "r") as file:
        return json.load(file)

def match_symptoms(user_symptoms, data):
    matched = []
    for entry in data:
        entry_symptoms = [s.lower() for s in entry["symptoms"]]
        common = set(user_symptoms).intersection(set(entry_symptoms))
        if common:
            match_percent = len(common) / len(entry_symptoms)
            matched.append({
                "condition": entry["condition"],
                "advice": entry["advice"],
                "match_percent": round(match_percent * 100)
            })
    return sorted(matched, key=lambda x: -x["match_percent"])

