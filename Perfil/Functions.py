import ezdxf
from ezdxf.layouts import Paperspace
from ezdxf.document import Drawing
import ezdxf.math
import numpy as np


# print(ezdxf.__version__)

# from ezdxf.acc import Vec2

from Find_edge import buscar_intersecao


def empranchar_perfil(doc:Drawing):
    
    
    ...













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





def add_viewport(doc:Drawing,layout_number,corner1,corner2):
    layout = doc.layouts.get(str(layout_number))
    # viewport = layout.add_viewport(center=(400,400),
    #                                size=(100,100),
    #                                view_center_point=(0,0),
    #                                viewport=10)
    
    x_min = corner1[0]
    x_max = corner2[0]
    y_min = corner1[1]
    y_max = corner2[1]   
    
    x_center = (x_max + x_min)/2
    y_center = (y_max + y_min)/2
    
    layout.add_viewport(
    center=(x_center, y_center),
    size=(abs(x_max-x_min), abs(y_max-y_min)),
    view_center_point=(7.5, 7.5),
    view_height=10,

    )
    # viewport.dxt.status = 1
    return doc
    ...




#Usado para inspecionar o conteudo do bloco "nome_bloco" 
#Used to inspect all entitys in the bloco named "nome_bloco"
def inspecionar_bloco(doc:Drawing,nome_bloco):

    pontos = []
    
    try:
        block = doc.blocks.get(nome_bloco)
        if block is not None:
            for e in block:
                
                # Caso a entidade seja uma polyline extrai seus vertices
                # If the entity is Polyline, extracts there vertices 
                if e.dxftype() == "LWPOLYLINE":

                    vertice_poly = []

                    for point in e.get_points():
                        vertice_poly.append((np.round(point[0],4),np.round(point[1],4)))

                    # Muito importante, caso a polylinha seja fechada, o último ponto não é gerado, 
                    # corrigido repetindo o primeiro ponto como último.
                    # Very important, if the entity is a closed polyline, the last point is suppressed, 
                    # so to fix this the first point must be repeated at the last position
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





   


