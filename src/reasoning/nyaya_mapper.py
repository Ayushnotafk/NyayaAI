import json

def load_rules():
    with open("data/nyaya_rules.json") as f:
        return json.load(f)

rules = load_rules()

def map_to_nyaya(arg):
    premise = arg["premise"].lower()

    for rule in rules:
        if rule["hetu"] in premise:
            return {
                "paksha": arg["claim"],
                "hetu": arg["premise"],
                "vyapti": rule["vyapti"]
            }

    return {
        "paksha": arg["claim"],
        "hetu": arg["premise"],
        "vyapti": "Unknown relation"
    }