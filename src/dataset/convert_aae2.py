import os
import json

DATA_DIR = "data/aae2"
OUTPUT_FILE = "data/processed_aae2.json"

dataset = []

for file in os.listdir(DATA_DIR):
    if file.endswith(".ann"):
        ann_path = os.path.join(DATA_DIR, file)
        txt_path = ann_path.replace(".ann", ".txt")
        # read text file
        with open(txt_path, encoding="utf-8") as f:
            text = f.read()

        # read annotations
        with open(ann_path, encoding="utf-8") as f:
            lines = f.readlines()

        for line in lines:
            if line.startswith("T"):
                parts = line.strip().split("\t")

                tag_info = parts[1].split()
                label = tag_info[0]

                start = int(tag_info[1])
                end = int(tag_info[2])

                span_text = text[start:end]

                if label in ["Claim", "Premise"]:
                    dataset.append({
                        "text": span_text.strip(),
                        "label": label
                    })

# save dataset
with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    json.dump(dataset, f, indent=2)

print("✅ Dataset ready! Total samples:", len(dataset))