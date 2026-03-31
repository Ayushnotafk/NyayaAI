from transformers import pipeline

# simple NLP pipeline
classifier = pipeline("text-classification")

def classify_argument(text):
    result = classifier(text)[0]

    # fake mapping (starter level)
    if "because" in text or "since" in text:
        parts = text.split("because") if "because" in text else text.split("since")
        return {
            "claim": parts[0].strip(),
            "premise": parts[1].strip()
        }

    return {
        "claim": text,
        "premise": ""
    }