# flake8: noqa
import ezdxf
from .Perfil import Perfil
from .Estrutura import Estrutura
from .Catenaria import Catenaria
from .Vao import Vao   

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
    estruturas = []
    try:
        doc = ezdxf.readfile(file_path)
        modelspace = doc.modelspace()
    except IOError:
        doc = ezdxf.new()
        modelspace = doc.modelspace()


    counter = 1
    for vao in estacas:

        estrutura = Estrutura(counter,tam)
        
        estrutura.set_p_base(perfil.find_point(vao))
        
        # print(f"perfil.find_point(vao): {perfil.find_point(vao)}")
        
        modelspace.add_lwpolyline([estrutura.coord_base,estrutura.coord_topo])

        # print(f"estrutura.coord_topo: {estrutura.coord_topo}")
        estruturas.append(estrutura)
        # print(estruturas)
        counter +=1
        ...
    
    # print(estruturas)
    
    doc.saveas(file_path)
    print("LWPOLYLINE inserida ou editada no arquivo:", file_path)
    
    return estruturas
    ...

def create_vao(file_path, estruturas,T,p):
    try:
        doc = ezdxf.readfile(file_path)
        modelspace = doc.modelspace()
    except IOError:
        doc = ezdxf.new()
        modelspace = doc.modelspace()     
 
 
    vaos = []
    
    
    
    
    for i in range(len(estruturas)-1):
        # subset = [estruturas[i],estruturas[i+1]]
        vao = Vao(estruturas[i],estruturas[i+1])    
        # vao = create_vao(lwpolyline_dxf, estruturas[i],estruturas[i+1],To,p)
        
        vertices=vao.create_cat_nivel1(T, p)
        # print(vertices)
        
        cater_color = 10
        cater_color = 0.3
        cater = modelspace.add_lwpolyline(points=vertices)
        cater.dxf.color = 10
        cater.dxf.const_width = 0.3 
        vaos.append(vao)

    doc.saveas(file_path)
    print("Catenarias inseridas no arquivo:", file_path)       


    
    # print(type(estrutura_final))
   
    
    
    

    # print(vao.comprimento)
    pass

# def create_vao(file_path, estrutura_inicial,estrutura_final,T,p):
#     # print(type(estrutura_final))
#     vao = Vao(estrutura_inicial,estrutura_final)
#     vao.create_cat_nivel1(T, p)
    
    
    
    
    
    
    
    
#     print(vao.comprimento)
#     pass




def create_catenaria(file_path,vertices,p,To):
    
    cat = Catenaria(vertices,p,To)
    print(f"Ae: {cat.Ae:.4f}") 
    print(f"vao: {cat.vao}")
    # print(f"Ae_1:{cat.Ae_1}") 
    # print(f"Ae_2:{cat.Ae_2}") 
    cat.get_pontos()
    print(f"x min:{cat.x_min}")
    # print(f"x max:{cat.x_max}")
    # print(f"y min:{cat.y_min}")
    # print(f"y max:{cat.y_max}") 
    # print(f"C1: {cat.C1:.4f}") 
    # print(f"fo: {cat.fo:.4f}")
    x,fx = cat._calc()
    vertices = list(zip(x,fx))
    # print(f"vertices: {vertices}")
    # create_lwpolyline(file_path,vertices)
    
    # print(x)
    # print(fx)
    # print(f'min{min(fx)}')
    # print(list(zip(x,fx)))
    
    try:
        doc = ezdxf.readfile(file_path)
        modelspace = doc.modelspace()
    except IOError:
        doc = ezdxf.new()
        modelspace = doc.modelspace()    

    modelspace.add_lwpolyline(points=vertices, close=False)
    doc.saveas(file_path)
    print("LWPOLYLINE inserida ou editada no arquivo:", file_path)
    
    
    ...

def limpar_arquivo(file_path):
    
    try:
        doc = ezdxf.readfile(file_path)
        msp = doc.modelspace()
        msp.delete_all_entities()
        doc.save()        
        
    except IOError:
        print("O arquivo nao existe, nada para limpar")




    
