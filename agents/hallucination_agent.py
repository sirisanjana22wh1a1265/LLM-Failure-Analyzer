from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer("all-MiniLM-L6-v2")

def detect_hallucination(context, answer):
    context_emb = model.encode(context, convert_to_tensor=True)
    answer_emb = model.encode(answer, convert_to_tensor=True)

    similarity = util.cos_sim(context_emb, answer_emb).item()

    return {
        "similarity": similarity,
        "hallucinated": similarity < 0.5
    }
