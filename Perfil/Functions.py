import ezdxf
from ezdxf.layouts import Paperspace
from ezdxf.document import Drawing
import ezdxf.math
import numpy as np
import traceback

# print(ezdxf.__version__)

# from ezdxf.acc import Vec2


#Carrega o arquivo 
#Upload the file from file_path
def carregar(file_path):
    try:
        doc = ezdxf.readfile(file_path)
        return doc        
    except:
        print(f"Não foi possível carregar {file_path}")
        
#Salva no arquivo de destino
#Save the doc at save_path
def salvar(doc: Drawing, save_path):
    try:
        doc.saveas(save_path)
    except:
        print("O arquivo não pode ser salvo")

#Constrói layouts vazios com a quantidade da variavel num_layouts
#Builds empty layouts with the quantity of the num_layouts variable
def criar_layouts(doc: Drawing, num_layouts,format="ISO A1"):
    #build list with number os all layouts
    list_layouts = list(range(1,num_layouts+1))
 
    for aba in list_layouts:     
        #Create new layouts named by list_layouts
        doc.page_setup(str(aba), format, landscape=True)

    return doc

#Insere o carimbo em todos os layouts criados
#Insert sheet model in all layouts 
def inserir_carimbo(doc:Drawing,nome_carimbo,numero_layout):
        
    list_layouts = list(range(1,numero_layout+1))        
    
    for numero in list_layouts:
        msp = doc.layouts.get(str(numero))   
        msp.add_blockref(nome_carimbo,insert=(0,0))
    
    return doc


#Lista todos os blocos nomeados 
#List all named blocks
def listar_blocos(doc:Drawing):
    lista_blocos = []
    for block in doc.blocks:
        if not block.name[0] == "*":
            # print(f"block: {block.name} ")
            lista_blocos.append(block.name)
    
    return lista_blocos


#Usado para inspecionar o conteudo do bloco "nome_bloco" 
#Used to inspect all entitys in the bloco named "nome_bloco"
def inspecionar_bloco(doc:Drawing,nome_bloco):

    pontos = []
    
    try:
        block = doc.blocks.get(nome_bloco)
        if block is not None:
            for e in block:
                if e.dxftype() == "LWPOLYLINE":

                    vertice_poly = []

                    for point in e.get_points():
                        vertice_poly.append((np.round(point[0],4),np.round(point[1],4)))
                
                    if e.close:
                        vertice_poly.append(vertice_poly[0])                    
         
                    pontos.append(vertice_poly)     

 
                elif e.dxftype() == "LINE": 
                    vertice_line = []
                    vertice_line.append((np.round(e.dxf.start[0],4),np.round(e.dxf.start[1],4)))    
                    vertice_line.append((np.round(e.dxf.end[0],4),np.round(e.dxf.end[1],4)))                

                    pontos.append(vertice_line)  
                    ...
                    
    except Exception as e:
        print(f"{str(e)}")
        
    buscar_intersecao(doc,pontos)
    
    return doc

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
    
    
    # polyline(doc,poly_left,1)
    # polyline(doc,poly_right,2)
    # polyline(doc,poly_top,3)
    # polyline(doc,poly_botton,4)
    
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
    
    # circular(doc,center,7)
    # circular(doc,left,1)
    # circular(doc,right,2)
    # circular(doc,top,3)
    # circular(doc,botton,4)
    

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
        circular(doc,left_closest_point,1)
        
        right_closest_point = find_closest_point_vc2(intersection_right,center)
        circular(doc,right_closest_point,2)

        top_closest_point = find_closest_point_vc2(intersection_top,center)
        circular(doc,top_closest_point,3)

        botton_closest_point = find_closest_point_vc2(intersection_botton,center)
        circular(doc,botton_closest_point,4)
    
        find_closest_point_vc2(intersection_left,center)        
    except Exception as e:
        print(f"Erro: {e}\nTraceback: {traceback.format_exc()}")

    

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

    print(f'closest_point: {closest_point}')
    return closest_point




def processar_pontos(doc:Drawing,pontos):
    layout = doc.layouts.get("1")
    width = layout.dxf.paper_width
    height = layout.dxf.paper_height
    
    x_center = width/2
    y_center = height/2
    
    
    x_values = [x for x, y in pontos]
    y_values = [y for x, y in pontos]
    
    
    x_values.sort()
    y_values.sort()
    
    x_anterior, x_proximo = buscar_proximos(x_values,x_center)
    y_anterior, y_proximo = buscar_proximos(y_values,y_center)
    

    circular(doc,(x_center,y_center))
    
    circular(doc,(x_anterior,y_anterior))
    circular(doc,(x_anterior,y_proximo))
    
    circular(doc,(x_proximo,y_anterior))
    
    circular(doc,(x_proximo,y_proximo))


def buscar_proximos(valores,alvo):

    for valor in valores:
        if valor < alvo:
            anterior = valor
        elif valor > alvo:
            proximo = valor
            break
    return anterior,proximo
    ...


    




# Define a área de criação da viewport
def definir_area_viewport(doc:Drawing):
    layout = doc.layouts.get("1")
        
    width= layout.dxf.paper_width
    height = layout.dxf.paper_height
    center =(width/2,height/2) 
    left = (0,height/2)
    
    points = [center, left]

    polilinha=layout.add_lwpolyline(points,format='xy')    #LWPOLYLINE(#94D0F)

    print(f"polilinha: {polilinha}")
    return doc

def buscar_viewport(layout: Paperspace):
    width = layout.dxf.paper_width
    height = layout.dxf.paper_height 
    print(f"width: {width}")
    print(f"height: {height}")
 

def circular(doc:Drawing,coordenada,cor=10):
    layout = doc.layouts.get("1")
    width = layout.dxf.paper_width
    height = layout.dxf.paper_height
    # coordenada =(width/2,height/2) 
    # center = (0,0)
    
    try:
        doc.layers.new('marker_circle',dxfattribs={'color':cor})
    except Exception as e:
        # print(f"{str(e)}")
        ...

    layout.add_circle(coordenada,radius=5,dxfattribs={'layer': 'marker_polyline','color':cor})   
    
    return doc
    ...
    
def polyline(doc:Drawing,coordenada,cor=10):
    layout = doc.layouts.get("1")
    
    try:
        doc.layers.new('marker_polyline',dxfattribs={'color':cor})
    except Exception as e:
        ...

    layout.add_lwpolyline(coordenada,format='xy',dxfattribs={'layer': 'marker_polyline','color':cor}) 


        
 
def salvar_txt(lista):
    path_txt = "data/layout/output.txt"
    with open(path_txt, 'w') as arquivo:
        for linha in lista:
            linha_formatada = ' '.join([str(elemento) for elemento in linha])
            arquivo.write(linha_formatada + '\n')
            arquivo.write('\n')


