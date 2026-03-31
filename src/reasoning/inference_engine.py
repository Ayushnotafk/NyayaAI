def infer(nyaya_obj):
    hetu = nyaya_obj["hetu"].lower()
    paksha = nyaya_obj["paksha"].lower()

    # Correct Nyaya rule
    if "smoke" in hetu and "fire" in paksha:
        return "Valid Nyaya Inference"

    # Reverse logic (wrong inference)
    if "fire" in hetu and "smoke" in paksha:
        return "Invalid (Reverse Reasoning Fallacy)"

    return "Uncertain inference"