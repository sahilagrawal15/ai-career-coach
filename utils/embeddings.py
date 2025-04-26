from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')  # lightweight, fast

def generate_embedding(text):
    return model.encode([text])[0]
