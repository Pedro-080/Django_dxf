# flake8: noqa
import ezdxf
from .Perfil import Perfil
from .Estrutura import Estrutura

def get_lwpolyline_vertices(file_path,path_write): #Lê um arquivo dxf e salva os vértices em um txt
    doc = ezdxf.readfile(file_path)  # Abre o arquivo DXF
    modelspace = doc.modelspace()  # Acessa o espaço de modelo do arquivo

    lwpolylines = [entity for entity in modelspace if entity.dxftype() == "LWPOLYLINE"]
    # Filtra todas as entidades no espaço de modelo e pega somente as do tipo "LWPOLYLINE"

    points = [] #Lista vazia que guardará os objetos do tipo Vertice

    for lwpolyline in lwpolylines:
        print(f"LWPOLYLINE with {len(lwpolyline)} vertices:")
        # Imprime o número de vértices da polilinha leve

        profile = Perfil()

        for vertex,num in zip(lwpolyline.vertices(),range(len(lwpolyline))):
            x, y = vertex   # Desempacota a tupla do vértice em coordenadas X e Y
            profile.add_vertice(coord_x=x,coord_y=y)  #adiciona objetos da classe Vertice como objetos da classe Perfil
            # profile.add_vertice(num=num+1,coord_x=x,coord_y=y)
        profile.save_txt(path_write) #salva os pontos adicionados na instancia profile da classe Perfil em um txt
        print("-" * 30)

        # return profile.poins_tuple()
        return profile

def create_lwpolyline(file_path, vertices, fechar=False): #Cria um arquivo dxf com os vertices de um txt
    try:
        doc = ezdxf.readfile(file_path)
        modelspace = doc.modelspace()
    except IOError:
        doc = ezdxf.new()
        modelspace = doc.modelspace()

    # lwpolyline = modelspace.add_lwpolyline(points=vertices, close=fechar)
    modelspace.add_lwpolyline(points=vertices, close=fechar)
    doc.saveas(file_path)
    print("LWPOLYLINE inserida ou editada no arquivo:", file_path)


def create_pole(file_path,perfil, estacas):
    tam = 10

    try:
        doc = ezdxf.readfile(file_path)
        modelspace = doc.modelspace()
    except IOError:
        doc = ezdxf.new()
        modelspace = doc.modelspace()

    for vao in estacas:

        estrutura = Estrutura(tam)
        
        estrutura.set_p_base(perfil.find_point(vao))

        modelspace.add_lwpolyline([estrutura.coord_base,estrutura.coord_topo])

        ...

    doc.saveas(file_path)
    print("LWPOLYLINE inserida ou editada no arquivo:", file_path)
    ...

