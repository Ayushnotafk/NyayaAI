import faiss
import numpy as np

index = faiss.IndexFlatL2(384)

documents = []

def add_doc(embedding, text):
    index.add(np.array([embedding]))
    documents.append(text)

def search(query_embedding):
    D, I = index.search(np.array([query_embedding]), k=1)
    return documents[I[0][0]]