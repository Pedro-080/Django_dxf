# flake8: noqa
import ezdxf


def read_dxf_file(file_path):
    doc = ezdxf.readfile(file_path)
    modelspace = doc.modelspace()

    for entity in modelspace:
        print(f"Entity type: {entity.dxftype()}")
        print(f"Entity data: {entity.dxfattribs()}")
        print("-" * 30)



def get_lwpolyline_vertices(file_path,path_write):
    doc = ezdxf.readfile(file_path)  # Abre o arquivo DXF
    modelspace = doc.modelspace()  # Acessa o espaço de modelo do arquivo

    lwpolylines = [entity for entity in modelspace if entity.dxftype() == "LWPOLYLINE"]
    # Filtra todas as entidades no espaço de modelo e pega somente as do tipo "LWPOLYLINE"

    for lwpolyline in lwpolylines:
        print(f"LWPOLYLINE with {len(lwpolyline)} vertices:")
        # Imprime o número de vértices da polilinha leve

        with open(path_write,'w') as file:
            file.write("")  #Limpa o arquivo
        


        for vertex,num in zip(lwpolyline.vertices(),range(len(lwpolyline))):
            x, y = vertex  # Desempacota a tupla do vértice em coordenadas X e Y
            # write_txt(path_write,num,x,y)
            
            with open(path_write,"r") as file:
                linhas = file.readlines()
          
            with open(path_write,"w") as file:
                for linha in linhas:
                    file.write(linha)
                file.write(f"{num+1},{x:.4f},{y:.4f}\n")
            
        print("-" * 30)


def write_txt(path_file,num,x,y):
    with open(path_file,"r") as file:
        linhas = file.readlines()
        
    with open(path_file,"w") as file:
        for linha in linhas:
            file.write(linha)
            
        file.write(f"{num+1},{x:.4f},{y:.4f}\n")
    ...
    



if __name__ == "__main__":
    path_read = "data/perfil/ramalA.dxf"
    path_write = "data/perfil/ramalA.txt" 
    get_lwpolyline_vertices(path_read,path_write)
