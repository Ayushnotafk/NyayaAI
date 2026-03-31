import joblib

model = joblib.load("models/model.pkl")
vectorizer = joblib.load("models/vectorizer.pkl")

def classify_argument(text):
    X = vectorizer.transform([text])
    pred = model.predict(X)[0]

    # If model says it's not an argument
    if pred == 0:
        return {
            "claim": text,
            "premise": ""
        }

    # If it's an argument → extract
    if "because" in text:
        parts = text.split("because")
        return {
            "claim": parts[0].strip(),
            "premise": parts[1].strip()
        }

    if "since" in text:
        parts = text.split("since")
        return {
            "claim": parts[0].strip(),
            "premise": parts[1].strip()
        }

    return {
        "claim": text,
        "premise": ""
    }