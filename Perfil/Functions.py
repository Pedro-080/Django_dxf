import ezdxf
from ezdxf.layouts import Paperspace
from ezdxf.document import Drawing
import ezdxf.math

# print(ezdxf.__version__)
# from ezdxf.acc import Vec2

#Carrega o arquivo 
def carregar(file_path):
    try:
        doc = ezdxf.readfile(file_path)
        return doc        
    except:
        print(f"Não foi possível carregar {file_path}")
        
#Salva no arquivo de destino
def salvar(doc: Drawing, save_path):
    try:
        doc.saveas(save_path)
    except:
        print("O arquivo não pode ser salvo")

# Cria um conjunto de layouts a partir da variavel num_layouts
def criar_layouts(doc: Drawing, num_layouts):

    list_layouts = list(range(1,num_layouts+1))
 
    for aba in list_layouts:     
        doc.page_setup(str(aba), "ISO A1", landscape=True)

    return doc

# Insere o carimbo em todos os layouts criados
def inserir_carimbo(doc:Drawing,nome_carimbo,numero_layout):
        
    list_layouts = list(range(1,numero_layout+1))        
    
    for numero in list_layouts:
        msp = doc.layouts.get(str(numero))   
        msp.add_blockref(nome_carimbo,insert=(0,0))
    
    return doc

#Lista todos os blocos nomeados 
def listar_blocos(doc:Drawing):
    lista_blocos = []
    for block in doc.blocks:
        if not block.name[0] == "*":
            # print(f"block: {block.name} ")
            lista_blocos.append(block.name)
    
    return lista_blocos

# Usado para inspecionar blocos
def inspecionar_bloco(doc:Drawing,nome_bloco):
    msp = doc.modelspace()

    pontos = []
    
    # print(f"n de entidades: {len(msp)}")
    
    count = 0
    try:
        block = doc.blocks.get(nome_bloco)
        if block is not None:
            for e in block:
                if e.dxftype() == "LWPOLYLINE" :
                    count+=1
        
                    vertice_poly = []
                    # print(f"{e} type: {type(e)} len: {len(e)} handle:{e.points()}")
                    # print(f"points: {e.points()}")
                    
                    
                    for point in e.get_points():
                        ...
                        vertice_poly.append((point[0],point[1]))
                        # print(f"X: {point[0]}, Y: {point[1]}")
                        # circular(doc,(point[0],point[1]))
                        
                    buscar_intersecao(doc,vertice_poly)
                    # print("\n")  # Separador para a próxima polilinha                        
                    
                    
                    # # ===============OURO================
                    # for key, value in e.dxfattribs().items():
                    #     # e.dxfattribs().
                    #     print(f"{key}: {value}")
                    # print("\n")  # Separador para a próxima polilinha  
                        
                                         
                    # for point in e.points():
                    #     # print(f"Coordenada: {point[0]}, {point[1]}")
                    #     print(f"points: {point}")
                 
                elif e.dxftype() == "LINE" and False : 
                    print(f"start: {e.dxf.start}, end {e.dxf.end}")
                    ...
                    
    except Exception as e:
        print(f"{str(e)}")
    
    # processar_pontos(doc,pontos)
    # print(len(pontos))
    # buscar_intersecao(pontos)
    # print(f"count polylines: {count}")


def buscar_intersecao(doc:Drawing,vertices):
    layout = doc.layouts.get("1")
        
    width = layout.dxf.paper_width
    height = layout.dxf.paper_height
    center =(width/2,height/2) 
    left = (0,height/2)
    
    polilinha1=[center,left]
    polilinha2=vertices

    count = 0
    vec2_points1 = [ezdxf.math.Vec2(point[0], point[1]) for point in polilinha1]
    vec2_points2 = [ezdxf.math.Vec2(point[0], point[1]) for point in polilinha2]
    
    intersections = ezdxf.math.intersect_polylines_2d(vec2_points1, vec2_points2)
    

    if intersections:
        for intersection in intersections:
            print(intersection)
            # print(intersection.x, intersection.y)
            circular(doc,(intersection.x, intersection.y))
    # print(vertices)
    # # for points in vertices:
    # #     count+=1
    # #     print(points)


    # print(f"Num vertices: {count}\n")





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
    
    # print("center x:", x_center)
    # print("center y:", y_center)
    # print("Valor anterior a x:", x_anterior)
    # print("Valor posterior a x:", x_proximo)
    # print("Valor anterior a y:", y_anterior)
    # print("Valor posterior a y:", y_proximo)
    ...


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
        
    width = layout.dxf.paper_width
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
 

def circular(doc:Drawing,coordenada):
    layout = doc.layouts.get("1")
    width = layout.dxf.paper_width
    height = layout.dxf.paper_height
    # coordenada =(width/2,height/2) 
    # center = (0,0)
    
    try:
        doc.layers.new('marker',dxfattribs={'color':6})
    except Exception as e:
        print(f"{str(e)}")

    layout.add_circle(coordenada,radius=5,dxfattribs={'layer': 'marker'})   
    
    # salvar(doc)
    return doc
    ...


        
 
    

