def infer(nyaya_obj):
    hetu = nyaya_obj["hetu"].lower()
    paksha = nyaya_obj["paksha"].lower()
    vyapti = nyaya_obj["vyapti"].lower()

    # valid case
    if "smoke" in hetu and "fire" in paksha:
        return "Valid Inference (Nyaya)"

    if "cancer" in hetu and "harmful" in paksha:
        return "Valid Inference (Nyaya)"

    if "rain" in hetu and "wet" in paksha:
        return "Valid Inference (Nyaya)"

    # reverse reasoning
    if "fire" in hetu and "smoke" in paksha:
        return "Fallacy: Reverse reasoning"

    # missing relation
    if "unknown" in vyapti:
        return "Fallacy: No Vyapti (no relation found)"

    return "Uncertain inference"