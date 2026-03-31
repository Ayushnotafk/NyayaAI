from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "gpt2"

def load_model():
    model = AutoModelForCausalLM.from_pretrained(model_name)
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    return model, tokenizer