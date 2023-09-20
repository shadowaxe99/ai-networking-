
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class SearchService:
    def __init__(self, data):
        self.data = data
        self.vectorizer = TfidfVectorizer()

    def search(self, query):
        tfidf_matrix = self.vectorizer.fit_transform(self.data)
        query_vector = self.vectorizer.transform([query])
        cosine_similarities = cosine_similarity(query_vector, tfidf_matrix).flatten()
        related_docs_indices = np.argsort(-cosine_similarities)
        return related_docs_indices
