# def extract_argument(text):
#     if "because" in text:
#         parts = text.split("because")
#         claim = parts[0].strip()
#         premise = parts[1].strip()
#     else:
#         claim = text
#         premise = ""

#     return {
#         "claim": claim,
#         "premise": premise
#     }
from src.reasoning.ml_model import classify_argument

def extract_argument(text):
    return classify_argument(text)