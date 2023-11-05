import ezdxf
from ezdxf.layouts import Paperspace
from ezdxf.document import Drawing
import ezdxf.math
import numpy as np
import traceback

from Functions_debug import circular,polyline


#Busca os limites da área para desenho através das interseções com as bordas
#Finds the limits to create a viewport through intersections with edges
def buscar_intersecao(doc:Drawing,vertices):

    # define o primeiro layout como modelo
    #Defines the first layout with model
    layout = doc.layouts.get(0)

    width = layout.dxf.paper_width
    height = layout.dxf.paper_height
    
    center =(width/2,height/2)
    left = (0,height/2) 
    right = (width,height/2)     
    
    top= (width/2,height)    
    botton  = (width/2,0)
 

    #Cria um "+" entre o centro e os limites da página
    #Create a "+" between center and edges at layout
    poly_left = [center,left]
    poly_right = [center,right]
    poly_top = [center,top]
    poly_botton = [center,botton]

    
    # Transforma os vértices determinados em objetos do tipo ezdxf.math.Vec2
    # Constructs a Vec2 object with previously determined vertices
    vec2_left = [ezdxf.math.Vec2(point[0], point[1]) for point in poly_left]
    vec2_right = [ezdxf.math.Vec2(point[0], point[1]) for point in poly_right]
    vec2_top = [ezdxf.math.Vec2(point[0], point[1]) for point in poly_top]
    vec2_botton = [ezdxf.math.Vec2(point[0], point[1]) for point in poly_botton]

    intersection_left = []
    intersection_right = []
    intersection_top  = []
    intersection_botton = []   

    for poly in vertices:
        # Para cada polylinha percorre todos os vértices e salva como objeto Vec2
        # For each polyline it traversses all vertices and saves it as a Vec2 object
        vec2_input = [ezdxf.math.Vec2(point[0], point[1]) for point in poly]
        
        # Busca por interseções entre o '+' e os vértices 
        # search for intersections between '+' and vertices
        intersection_left.append(ezdxf.math.intersect_polylines_2d(vec2_input, vec2_left))
        intersection_right.append(ezdxf.math.intersect_polylines_2d(vec2_input, vec2_right))
        intersection_top.append(ezdxf.math.intersect_polylines_2d(vec2_input, vec2_top))
        intersection_botton.append(ezdxf.math.intersect_polylines_2d(vec2_input, vec2_botton))    
  
    
    # Remove as respostas vazias do resultado
    # Remove empty answers from the result
    intersection_left = [item for sublist in intersection_left for item in sublist if isinstance(sublist, list)]
    intersection_right = [item for sublist in intersection_right for item in sublist if isinstance(sublist, list)]
    intersection_top = [item for sublist in intersection_top for item in sublist if isinstance(sublist, list)]
    intersection_botton = [item for sublist in intersection_botton for item in sublist if isinstance(sublist, list)]
   
    
    
    try:
        left_closest_point = find_closest_point_vc2(intersection_left,center)
        left_edge = left_closest_point[0]
        # print(f"left_edge: {left_edge}")
        circular(doc,left_closest_point,1)
        
        right_closest_point = find_closest_point_vc2(intersection_right,center)
        right_edge = right_closest_point[0]
        circular(doc,right_closest_point,2)

        top_closest_point = find_closest_point_vc2(intersection_top,center)
        top_edge = top_closest_point[1]
        circular(doc,top_closest_point,3)

        botton_closest_point = find_closest_point_vc2(intersection_botton,center)
        botton_edge = botton_closest_point[1]
        circular(doc,botton_closest_point,4)
    
        find_closest_point_vc2(intersection_left,center)
        
        
        x_range = (left_edge,right_edge)
        y_range = (botton_edge,top_edge)
        
    except Exception as e:
        print(f"Erro: {e}\nTraceback: {traceback.format_exc()}")
        
# Retorna o ponto mais próximo do alvo entre os pontos recebidos
# Returns the more nearst point from the target between the input points
def find_closest_point_vc2(points,alvo):
    if not points:
        return None
    
    alvo_vec2 = ezdxf.math.Vec2(alvo[0], alvo[1])
    
    min_distance = float('inf')
    closest_point = None

    for point in points:
        distance = point.distance(alvo_vec2)
        if distance < min_distance:
            min_distance = distance
            closest_point = point

    # print(f'closest_point: {closest_point}')
    return closest_point
