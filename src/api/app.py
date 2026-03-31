from fastapi import FastAPI
from src.reasoning.argument_miner import extract_argument
from src.reasoning.nyaya_mapper import map_to_nyaya
from src.reasoning.inference_engine import infer
from src.reasoning.fallacy_detector import detect_fallacy
from src.reasoning.explainer import explain

app = FastAPI()

@app.post("/analyze")
def analyze(text: str):
    arg = extract_argument(text)
    nyaya = map_to_nyaya(arg)
    result = infer(nyaya)
    fallacy = detect_fallacy(arg["claim"], arg["premise"])
    explanation = explain(nyaya, result)

    return {
    "argument": arg,
    "nyaya": nyaya,
    "inference": result,
    "fallacy": fallacy,
    "explanation": explanation
}