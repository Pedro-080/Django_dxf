from Functions import  *
import ezdxf.math


perfil_original = "data/layout/Perfil_0A.dxf"
doc = carregar(perfil_original)

msp = doc.modelspace()


# Definir os pontos das polilinhas
points1 = [ezdxf.math.Vec2(0, 0), ezdxf.math.Vec2(5, 0), ezdxf.math.Vec2(5, 5)]
points2 = [ezdxf.math.Vec2(2, 2), ezdxf.math.Vec2(2, 5), ezdxf.math.Vec2(6, 2)]

# Adicionar as polilinhas ao espaço do modelo
polyline1 = msp.add_lwpolyline([(p.x, p.y) for p in points1])
polyline2 = msp.add_lwpolyline([(p.x, p.y) for p in points2])

# Encontrar os pontos de interseção entre as polilinhas
intersections = ezdxf.math.intersect_polylines_2d(points1, points2)

# Imprimir os pontos de interseção
print("Pontos de interseção:")
print(f"Polilinha 1: {polyline1}")
print(f"Polilinha 2: {polyline2}")
print(f"Points 1: {points1}")

for intersection in intersections:
    print(intersection.x, intersection.y)