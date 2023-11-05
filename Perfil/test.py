from itertools import groupby


# Suponha que points seja o conjunto de pontos no formato (x, y)
points = [(3, 5), (7, 2), (2, 8), (9, 1), (60, 2), (70, 5), (130, 6), (200, 8)]

points.sort(key=lambda p: p[1])  # Ordenar os pontos pelo valor x

grouped_regions = []
current_group = [points[0]]

for prev_point, next_point in zip(points, points[:1]):
    if next_point[1] - prev_point[1] >= 50 :
        grouped_regions.append(current_group)
        current_group = []
    current_group.append(next_point)

grouped_regions.append(current_group)  # Adicionar o último grupo

print("Regiões agrupadas:")
for i, region in enumerate(grouped_regions, start=1):
    print(f"Região {i}: {region}")