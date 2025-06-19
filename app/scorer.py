from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import joblib

# One-time load or can be trained in notebook and saved
vectorizer = TfidfVectorizer()

def score_resume(jd_text, resume_text):
    texts = [jd_text, resume_text]
    tfidf_matrix = vectorizer.fit_transform(texts)
    similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])
    return round(float(similarity[0][0]) * 100, 2)