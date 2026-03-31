def detect_fallacy(claim, premise):
    if claim == premise:
        return "Circular reasoning"

    if premise == "":
        return "Missing premise"

    return "No fallacy"