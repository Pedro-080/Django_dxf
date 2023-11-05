import math
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np

# Função para calcular a distância entre dois pontos
def distancia(ponto1, ponto2):
    return math.sqrt((ponto1[0] - ponto2[0]) ** 2 + (ponto1[1] - ponto2[1]) ** 2)

# Lista de pontos gerados aleatoriamente
# pontos_aleatorios = [(5, 10), (30, 15), (20, 5), (40, 30), (12, 8), (25, 35), (8, 40), (18, 20), (2, 35), (50, 25)]
pontos = [(-126.1517, 7800.0), (-126.1517, 7850.0), (-126.1517, 7900.0), (-126.1517, 7950.0), (-126.1517, 8000.0), (-126.1517, 8050.0), (-126.1517, 8100.0), (-126.1517, 8150.0), (-126.1517, 8200.0), (-126.1517, 8250.0), (-126.1517, 8300.0), (-126.1517, 8350.0), (-126.1517, 8400.0), (-126.1517, 8450.0), (-126.1517, 8500.0), (-126.1517, 8550.0), (-126.1517, 8600.0), (-126.1517, 8650.0), (-126.1517, 8700.0), (-126.1517, 8750.0), (-126.1517, 8800.0), (-126.1517, 8850.0), (-126.1517, 8900.0), (-126.1517, 8950.0), (-126.1517, 9000.0), (-126.1517, 9050.0), (-126.1517, 9100.0), (-126.1517, 9150.0), (-126.1517, 9200.0), (-126.1517, 7750.0), (-126.1517, 9250.0), (-126.1517, 4989.469), (-126.1517, 5039.469), (-126.1517, 5089.469), (-126.1517, 5139.469), (-126.1517, 5189.469), (-126.1517, 5239.469), (-126.1517, 5289.469), (-126.1517, 5339.469), (-126.1517, 5389.469), (-126.1517, 5439.469), (-126.1517, 5489.469), (-126.1517, 5539.469), (-126.1517, 5589.469), (-126.1517, 5639.469), (-126.1517, 5689.469), (-126.1517, 5739.469), (-126.1517, 5789.469), (-126.1517, 5839.469), (-126.1517, 5889.469), (-126.1517, 5939.469), (-126.1517, 5989.469), (-126.1517, 6039.469), (-126.1517, 2953.187), (-126.1517, 2903.187), (-126.1517, 2853.187), (-126.1517, 2803.187), (-126.1517, 2753.187), (-126.1517, 2703.187), (-126.1517, 2653.187), (-126.1517, 2603.187), (-126.1517, 2553.187), (-126.1517, 2503.187), (-126.1517, 2453.187), (-126.1517, 2403.187), (-126.1517, 2353.187), (-126.1517, 2303.187), (479.8754, 2953.187), (479.8754, 2903.187), (479.8754, 2853.187), (479.8754, 2803.187), (479.8754, 2753.187), (479.8754, 2703.187), (479.8754, 2653.187), (479.8754, 2603.187), (479.8754, 2553.187), (479.8754, 2503.187), (479.8754, 2453.187), (479.8754, 2403.187), (479.8754, 2353.187), (479.8754, 2303.187), (3966.2287, 4989.469), (3966.2287, 5039.469), (3966.2287, 5089.469), (3966.2287, 5139.469), (3966.2287, 5189.469), (3966.2287, 5239.469), (3966.2287, 5289.469), (3966.2287, 5339.469), (3966.2287, 5389.469), (3966.2287, 5439.469), (3966.2287, 5489.469), (3966.2287, 5539.469), (3966.2287, 5589.469), (3966.2287, 5639.469), (3966.2287, 5689.469), (3966.2287, 5739.469), (3966.2287, 5789.469), (3966.2287, 5839.469), (3966.2287, 5889.469), (3966.2287, 5939.469), (3966.2287, 5989.469), (3966.2287, 6039.469), (6883.5594, 7800.0), (6883.5594, 7850.0), (6883.5594, 7900.0), (6883.5594, 7950.0), (6883.5594, 8000.0), (6883.5594, 8050.0), (6883.5594, 8100.0), (6883.5594, 8150.0), (6883.5594, 8200.0), (6883.5594, 8250.0), (6883.5594, 8300.0), (6883.5594, 8350.0), (6883.5594, 8400.0), (6883.5594, 8450.0), (6883.5594, 8500.0), (6883.5594, 8550.0), (6883.5594, 8600.0), (6883.5594, 8650.0), (6883.5594, 8700.0), (6883.5594, 8750.0), (6883.5594, 8800.0), (6883.5594, 8850.0), (6883.5594, 8900.0), (6883.5594, 8950.0), (6883.5594, 9000.0), (6883.5594, 9050.0), (6883.5594, 9100.0), (6883.5594, 9150.0), (6883.5594, 9200.0), (6883.5594, 7750.0), (6883.5594, 9250.0)]

pontos = np.array(pontos)
numero_clusters = 6


# Aplicando o algoritmo KMeans
kmeans = KMeans(n_clusters=numero_clusters, random_state=0).fit(pontos)

# Obtendo as labels dos clusters
labels = kmeans.labels_

# Criando dicionário para armazenar os pontos em diferentes clusters
grupos = {}
for i in range(numero_clusters):
    grupos[i] = []

# Adicionando os pontos aos clusters correspondentes
for i in range(len(pontos)):
    grupos[labels[i]].append(pontos[i])

# Imprimindo os grupos de pontos
for key, value in grupos.items():
    print(f"Grupo {key}: {value}")
    
    
    
# Visualização dos clusters
plt.scatter(pontos[:,0],pontos[:,1], c=kmeans.labels_,cmap='rainbow')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], color='black')
plt.show()    
    
    
    
    
    
# variancia_explicada = []
# for i in range(1, 11):
#     kmeans = KMeans(n_clusters=i, random_state=0)
#     kmeans.fit(pontos)
#     variancia_explicada.append(kmeans.inertia_)

# # Plotando o gráfico do método do cotovelo
# plt.plot(range(1, 11), variancia_explicada, marker='o')
# plt.title('Método do Cotovelo')
# plt.xlabel('Número de clusters')
# plt.ylabel('Variação explicada')
# plt.show()