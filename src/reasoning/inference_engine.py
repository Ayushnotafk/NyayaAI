def infer(nyaya_obj):
    hetu = nyaya_obj["hetu"].lower()
    paksha = nyaya_obj["paksha"].lower()
    vyapti = nyaya_obj["vyapti"].lower()

    # ❌ reverse reasoning check (keep this)
    if "fire" in hetu and "smoke" in paksha:
        return "Fallacy: Reverse reasoning"

    # ❌ missing relation
    if "unknown" in vyapti:
        return "Fallacy: No Vyapti (no relation found)"

    # ✅ VALID CASE (MAIN FIX)
    if vyapti and vyapti != "unknown relation":
        return "Valid Inference (Nyaya)"

    return "Uncertain inference"