# K-Means Clustering Implementation
# https://www.kaggle.com/code/egazakharenko/clustering-algorithms-from-scratch-using-python#K-Means

import numpy as np
from scipy.spatial.distance import cdist
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.metrics import adjusted_rand_score

class KMeansClustering:
    def __init__(self, n_clusters=8, max_iter=300, tol=0.0001, random_state=0):
        self.n_clusters = n_clusters
        self.max_iter = max_iter
        self.tol = tol
        self.random_state = random_state

    def _greedy_kmeans_plus_plus(self, X):
        np.random.seed(self.random_state)
        n_samples, n_features = X.shape
        n_local_trials = 2 + int(np.log(self.n_clusters))

        indices = np.arange(n_samples)
        first_index = np.random.choice(indices)
        centers = np.zeros((self.n_clusters, n_features))

        centers[0] = X[first_index]
        first_center = centers[0].reshape(1, -1)
        sq_distances = cdist(X, first_center, metric='sqeuclidean').ravel()

        for i in range(1, self.n_clusters):
            min_cost = np.inf
            min_new_sq_distances = []
            best_candidate_index = None

            for _ in range(n_local_trials):
                candidates_probas = sq_distances / np.sum(sq_distances)
                candidate_index = np.random.choice(indices, p=candidates_probas)
                candidate = X[candidate_index].reshape(1, -1)

                new_sq_distances = cdist(X, candidate, metric='sqeuclidean').ravel()
                new_cost = np.sum(np.minimum(sq_distances, new_sq_distances))

                if new_cost < min_cost:
                    best_candidate_index = candidate_index
                    min_new_sq_distances = new_sq_distances
                    min_cost = new_cost

            centers[i] = X[best_candidate_index]   # Choose the new center
            sq_distances = np.minimum(sq_distances, min_new_sq_distances)

        return centers

    def fit(self, X):
        n_samples, n_features = X.shape
        self.inertia_ = np.inf
        self.cluster_centers_ = self._greedy_kmeans_plus_plus(X)

        # Lloyd's algorithm
        for _ in range(self.max_iter):
            distances = cdist(X, self.cluster_centers_, metric='sqeuclidean')
            labels = np.argmin(distances, axis=1)
            new_inertia = np.sum(np.min(distances, axis=1))
            new_centers = np.zeros((self.n_clusters, n_features))

            for k in range(self.n_clusters):
                new_centers[k] = np.mean(X[labels == k], axis=0)

            if np.abs(new_inertia - self.inertia_) < self.tol:
                break

            self.inertia_ = new_inertia
            self.cluster_centers_ = new_centers

    def predict(self, X):
        distances = cdist(X, self.cluster_centers_, metric='sqeuclidean')
        predicted_labels = np.argmin(distances, axis=1)

        return predicted_labels

# test    
X1, y1 = make_blobs(n_samples=250, n_features=2, centers=8, random_state=0)
print(y1)

kmeans = KMeansClustering(n_clusters=8, random_state=0)
kmeans.fit(X1)
kmeans_pred_res = kmeans.predict(X1)
kmeans_ari = adjusted_rand_score(y1, kmeans_pred_res)
kmeans_centroinds = kmeans.cluster_centers_
print(f'Adjusted Rand Score for KMeans: {kmeans_ari}', '', sep='\n')
print('centroids', kmeans_centroinds, '', sep='\n')
print('prediction', kmeans_pred_res, sep='\n')