def extract_argument(text):
    if "because" in text:
        parts = text.split("because")

        part1 = parts[0].strip()
        part2 = parts[1].strip()

        # Rule-based priority (strong logic)
        return {
            "claim": part1,
            "premise": part2
        }

    if "since" in text:
        parts = text.split("since")

        return {
            "claim": parts[0].strip(),
            "premise": parts[1].strip()
        }

    # fallback ML
    X = vectorizer.transform([text])
    pred = model.predict(X)[0]

    if pred == 1:
        return {"claim": text, "premise": ""}
    else:
        return {"claim": "", "premise": text}   