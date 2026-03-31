# 🧠 Nyaya AI Reasoning System

A Generative AI + Indian Knowledge System (IKS) based project that performs logical reasoning using **Nyāya philosophy principles**.

This system analyzes arguments, extracts logical structure, maps them to Nyāya components, and determines whether the reasoning is valid or fallacious.

---

## 🚀 Features

### 🔍 Argument Analysis

* Extracts **Claim (Paksha)** and **Premise (Hetu)** from input text
* Uses **hybrid approach (Rule + ML model)**

### 🧠 Nyaya Reasoning

* Maps arguments into:

  * **Paksha (Conclusion)**
  * **Hetu (Reason)**
  * **Vyapti (Universal Rule)**

### ⚖️ Logical Inference

* Determines:

  * ✅ Valid Inference
  * ❌ Fallacy (No Vyapti / weak reasoning)

### 📖 Explainable AI (XAI)

* Provides human-readable explanation of reasoning

### 🤖 Machine Learning Integration

* Trained on **AAE2 (Argument Annotated Essays)** dataset
* Classifies:

  * Claim vs Premise

---

## 🏗️ Project Architecture

```text
Input Text
   ↓
Argument Extraction (Rule + ML)
   ↓
Nyaya Mapping (Paksha, Hetu)
   ↓
Knowledge Base (Vyapti)
   ↓
Inference Engine
   ↓
Explanation Generator
```

---

## 📂 Folder Structure

```text
NyayaAI/
│
├── data/
│   ├── aae2/                  # Raw dataset (AAE2)
│   └── processed_aae2.json   # Clean dataset
│
├── models/                   # Saved ML models
│
├── src/
│   ├── api/                  # FastAPI backend
│   ├── frontend/             # Streamlit UI
│   ├── dataset/              # Dataset processing
│   ├── reasoning/            # Nyaya logic + ML
│   ├── training/             # Model training
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

### 2️⃣ Run Backend (FastAPI)

```bash
python -m uvicorn src.api.app:app --reload
```

👉 Runs at: http://127.0.0.1:8000

---

### 3️⃣ Run Frontend (Streamlit)

```bash
python -m streamlit run src/frontend/app.py
```

---

## 📊 Dataset

* Dataset used: **AAE2 (Argument Annotated Essays)**
* Contains:

  * Claims
  * Premises
  * Argument relations

### Conversion

```bash
python src/dataset/convert_aae2.py
```

---

## 🤖 Model Training

```bash
python src/training/train_model.py
```

Model:

* Logistic Regression
* TF-IDF Vectorizer

---

## 🧪 Example

### Input:

```
Smoking is harmful because it causes cancer
```

### Output:

```text
Paksha: Smoking is harmful
Hetu: it causes cancer
Vyapti: Causing cancer implies harmful effect

Inference: Valid Inference (Nyaya)
```

---

## ⚠️ Limitations

* Rule-based dependency on words like **"because", "since"**
* ML model only classifies **Claim vs Premise**, not full structure
* Knowledge base (Vyapti) is limited

---

## 🔥 Future Improvements

* 🚀 BERT / Transformer-based argument extraction
* 🧠 Multi-step reasoning chains
* 📊 Graph visualization of arguments
* ⚖️ Advanced fallacy detection
* 🌐 Larger knowledge base (automatic learning)

---

## 📚 Technologies Used

* Python
* FastAPI
* Streamlit
* Scikit-learn
* HuggingFace (optional)
* NLP (TF-IDF)

---

## 🎯 Project Objective

To combine:

* 🧠 **Nyāya Philosophy (IKS)**
* 🤖 **Modern AI (NLP & ML)**

into a system capable of:

* Logical reasoning
* Argument analysis
* Explainable AI

---

## 👨‍💻 Author

Ayush Thakur
B.Tech (IIITDM Jabalpur)

---

## ⭐ Final Note

This project demonstrates how ancient Indian logical systems like **Nyāya** can be integrated with modern AI to build interpretable and reasoning-based systems.

---
