from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer("all-MiniLM-L6-v2")

def calculate_match_score(resume_text: str, job_desc: str) -> float:
    resume_embedding = model.encode(resume_text)
    job_embedding = model.encode(job_desc)

    similarity = cosine_similarity(
        [resume_embedding],
        [job_embedding]
    )[0][0]

    match_score = round(float(similarity) * 100, 2)

    return match_score
