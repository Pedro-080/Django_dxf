# flake8: noqa
import ezdxf

class Vertice:
    def __init__(self,num,x,y):
        self.num = num
        self.coordx = x
        self.coordy = y
        ...
        
    def __str__(self):
        return f"{self.num},{self.coordx:.4f},{self.coordy:.4f}"



def get_lwpolyline_vertices(file_path,path_write):
    doc = ezdxf.readfile(file_path)  # Abre o arquivo DXF
    modelspace = doc.modelspace()  # Acessa o espaço de modelo do arquivo

    lwpolylines = [entity for entity in modelspace if entity.dxftype() == "LWPOLYLINE"]
    # Filtra todas as entidades no espaço de modelo e pega somente as do tipo "LWPOLYLINE"

    points = [] #Lista vazia que guardará os objetos do tipo Verticev1_main.py

    for lwpolyline in lwpolylines:
        print(f"LWPOLYLINE with {len(lwpolyline)} vertices:")
        # Imprime o número de vértices da polilinha leve
      

        for vertex,num in zip(lwpolyline.vertices(),range(len(lwpolyline))):
            x, y = vertex  # Desempacota a tupla do vértice em coordenadas X e Y
            point = Vertice(num=num+1,x=x,y=y)
            points.append(point)
        
        
        # print(len(points))

        write_txt(path_write,points)
        print("-" * 30)


def write_txt(path_file,lista):
    with open(path_file,"w") as file:
        for obj in lista:
            file.write(str(obj) + "\n")    
    ...
    



if __name__ == "__main__":
    path_read = "data/perfil/ramalA.dxf"
    path_write = "data/perfil/ramalA.txt" 
    get_lwpolyline_vertices(path_read,path_write)
