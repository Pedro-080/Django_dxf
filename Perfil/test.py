# from Functions import  *
import ezdxf.math
import ezdxf
    



def encontrar_intersecoes(vertices, linha):
    intersecoes = []

    for poly in vertices:
        for i in range(len(poly) - 1):
            x1, y1 = poly[i]
            x2, y2 = poly[i + 1]

            if x1 == x2:  # interseção vertical
                if x1 <= linha[0][0] <= x2 or x2 <= linha[0][0] <= x1:
                    m = (y2 - y1) / (x2 - x1)
                    y = m * (linha[0][0] - x1) + y1
                    intersecoes.append((linha[0][0], y))

            if y1 == y2:  # interseção horizontal
                if y1 <= linha[0][1] <= y2 or y2 <= linha[0][1] <= y1:
                    m = (x2 - x1) / (y2 - y1)
                    x = m * (linha[0][1] - y1) + x1
                    intersecoes.append((x, linha[0][1]))

    return intersecoes


if __name__ == "__main__":

    # Exemplo de uso
    # vertices = [[(25,584),(25,10),(831,10),(831,584)],
    #         [(0.0, 594.0),(0.0, 0.0),(841.0, 0.0),(841.0, 594.0)],
    #         [(759.0186, 401.6029),(760.0186, 401.6029),(760.0186, 402.6029),(759.0186, 402.6029)],
    #         [(763.5416, 401.6029),(764.5416, 401.6029),(764.5416, 402.6029),(763.5416, 402.6029)]]
    
    vertices = [(25,584),(25,10),(831,10),(831,584)]
       
    poly_top = [(420.5,297),(420.5,594)]
    # poly_top = [(420.5,594),(420.5,297)]
    center = (420.5,297)
    intersection_top  = []
    
    
    vec2_top = [ezdxf.math.Vec2(point[0], point[1]) for point in poly_top]
    vec2_vertices = [ezdxf.math.Vec2(point[0], point[1]) for point in vertices]
    intersection_top = ezdxf.math.intersect_polylines_2d(vec2_vertices,vec2_top)
    
    # for poly in vertices:
    #     vec2_input = [ezdxf.math.Vec2(point[0], point[1]) for point in poly]
    #     intersection_top.append(ezdxf.math.intersect_polylines_2d(vec2_input, vec2_top))
    
    # intersection_top = encontrar_intersecoes(vertices, poly_top)
    
    # alvo_vec2 = ezdxf.math.Vec2(alvo[0], alvo[1])
    
    
    # closest = find_closest_point_vc2(vertices)
    print(intersection_top)

    # if closest:
    #     print(f"Ponto mais próximo de (0,0): ({closest.x}, {closest.y})")
    # else:
    #     print("A lista de pontos está vazia.")
    
    
