import random
import json

objects = ["hill", "forest", "room"]
causes = ["smoke", "heat", "light"]

def generate_sample():
    obj = random.choice(objects)
    cause = random.choice(causes)

    return {
        "paksha": f"There is fire on the {obj}",
        "hetu": f"There is {cause}",
        "vyapti": f"Where there is {cause}, there is fire",
        "valid": True
    }

def generate_dataset(n=1000, path="data/synthetic/nyaya.json"):
    data = [generate_sample() for _ in range(n)]
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

if __name__ == "__main__":
    generate_dataset()