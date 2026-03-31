import json
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
import joblib

# load data
with open("data/train_data.json") as f:
    data = json.load(f)

texts = [d["text"] for d in data]

# simple labels: 1 = has reasoning
labels = [d["label"] for d in data]
# vectorize text
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)

# train model
model = LogisticRegression()
model.fit(X, labels)

# save model
joblib.dump(model, "models/model.pkl")
joblib.dump(vectorizer, "models/vectorizer.pkl")

print("Model trained and saved!")