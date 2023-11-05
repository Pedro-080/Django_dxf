from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt

# Lista de pontos de exemplo
pontos = [(1, 2), (1, 4), (1, 0), (4, 2), (4, 4), (4, 0)]



print(pontos[-2])

# for ponto_anterior, proximo_ponto in zip(pontos, pontos[1:]):
#     print(f"proximo_ponto: {proximo_ponto}")
# # Converter a lista de pontos em uma matriz numpy
# X = np.array(pontos)

# # Agrupamento com K-means
# kmeans = KMeans(n_clusters=2)
# kmeans.fit(X)

# # Visualização dos clusters
# plt.scatter(X[:,0],X[:,1], c=kmeans.labels_,cmap='rainbow')
# plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], color='black')
# plt.show()
