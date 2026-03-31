def map_to_nyaya(arg):
    return {
        "paksha": arg["claim"],
        "hetu": arg["premise"],
        "vyapti": "learned relation from knowledge base"
    }