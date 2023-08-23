# flake8: noqa
# Estudo sobre tratamento de DXF
# VERSÃO - V3
# Exportar pontos como polyline  

import ezdxf

class Vertice:
    def __init__(self,num,x,y):
        self.num = num
        self.coord_x = x
        self.coord_y = y
        ...
        
    def __str__(self):
        return f"{self.num},{self.coord_x:.4f},{self.coord_y:.4f}"

    def tupla(self):
        return (round(self.coord_x,4),round(self.coord_y,4))
    
class Perfil:
    def __init__(self):
        self.vertices = []
        ...

    def add_vertice(self, num, coord_x, coord_y):
        vertice = Vertice(num, coord_x, coord_y)
        self.vertices.append(vertice)
        ...

    def exibir_vertices(self):
        for vertice in self.vertices:
            print(vertice)

    def poins_tuple(self):
        list_tuplas = []
        for vertice in self.vertices:
            list_tuplas.append(vertice.tupla())
        return list_tuplas
        ...

    def save_txt(self, path_file):
        save_vertices = []
        for vertice in self.vertices:
            # print(vertice)
            save_vertices.append(vertice)
            
        with open(path_file,"w") as file:
            for obj in save_vertices:
                file.write(str(obj) + "\n")  
        ...

def get_lwpolyline_vertices(file_path,path_write):
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
            profile.add_vertice(num=num+1,coord_x=x,coord_y=y)  #adiciona objetos da classe Vertice como objetos da classe Perfil

        profile.save_txt(path_write) #salva os pontos adicionados na instancia profile da classe Perfil em um txt
        print("-" * 30)

        return profile.poins_tuple()  
           
        

def create_lwpolyline(file_path, vertices, fechar=False):
    try:
        doc = ezdxf.readfile(file_path)
        modelspace = doc.modelspace()
    except IOError:
        doc = ezdxf.new()
        modelspace = doc.modelspace()

    lwpolyline = modelspace.add_lwpolyline(points=vertices, close=fechar)
    
    doc.saveas(file_path)
    print("LWPOLYLINE inserida ou editada no arquivo:", file_path)



if __name__ == "__main__":
    ramalA_dxf = "data/perfil/ramalA.dxf"
    ramalA_txt = "data/perfil/ramalA.txt"
    
    path_write2 = "data/perfil/test_class.txt"
    
    lwpolyline_dxf = "data/perfil/create_lwpolyline.dxf"
    
    # vert = [(0, 0), (5, 0), (5, 5), (0, 5)]
    
    
    # vertice = Vertice(1,2,3)
    # print(type(vertice.tupla()))
    
    vert = get_lwpolyline_vertices(ramalA_dxf,ramalA_txt)
    print(vert)
    create_lwpolyline(lwpolyline_dxf,vert)
    
