def explain(nyaya_obj, result):
    return f"""
Nyaya Reasoning:

Paksha (Conclusion): {nyaya_obj['paksha']}
Hetu (Reason): {nyaya_obj['hetu']}
Vyapti (Rule): {nyaya_obj['vyapti']}

Final Result: {result}
"""