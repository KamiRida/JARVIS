import numpy as np
from sentence_transformers import SentenceTransformer
from rag import read_context
similarities = []
doc_embeddings_list = []
query = "How much money does Kamran want to make per year?"
context = read_context()
# Load the model
model = SentenceTransformer("Qwen/Qwen3-VL-Embedding-2B")
query_embeddings = model.encode(query)
for i in context:
        doc_embeddings = model.encode(i)
        doc_embeddings_list.append(doc_embeddings)

def embed():
    for i in range(len(doc_embeddings_list)):
        dot = np.dot(query_embeddings, doc_embeddings_list[i])
        abs = np.linalg.norm(query_embeddings) * np.linalg.norm(doc_embeddings_list[i])
        similarity = dot / abs
        similarities.append(similarity)

    max_sim = np.max(similarities)
    for i in range(len(similarities)):
        if max_sim == similarities[i]:
            doc_index = i

    print(context[doc_index])

embed()