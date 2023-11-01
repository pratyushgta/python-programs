"""
This file contains methods for implementing K-means clustering Algorithm
AI-E10

Author: Pratyush Kumar (github.com/pratyushgta)
"""
import numpy as np
from sklearn.cluster import KMeans

clusters = np.array([2, 4, 10, 12, 3, 20, 30, 11, 25])
k = 2
clusters = clusters.reshape(-1, 1)

# Initialize the KMeans model with the desired number of clusters
kmeans = KMeans(n_clusters=k)
# Fit the model to the data
kmeans.fit(clusters)
cluster_centers = kmeans.cluster_centers_
labels = kmeans.labels_

print("Cluster Centers:")
for center in cluster_centers:
    print(center[0])

print("Cluster Labels:")
for label in labels:
    print(label)
