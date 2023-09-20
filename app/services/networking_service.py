
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

class NetworkingService:
    def __init__(self, data):
        self.data = data
        self.scaler = StandardScaler()
        self.kmeans = KMeans(n_clusters=5)

    def preprocess_data(self):
        self.data = self.scaler.fit_transform(self.data)

    def cluster_executives(self):
        self.preprocess_data()
        self.kmeans.fit(self.data)

    def get_top_executives(self):
        top_executives = self.kmeans.cluster_centers_
        return top_executives
