# flake8: noqa
# Estudo sobre tratamento de DXF
# VERSÃO - V5
# # Exportar pontos como polyline  

import ezdxf
from modules.Classes import Perfil
from modules.Functions import *

def create_lwpolyline(file_path, vertices, fechar=False): #Cria um arquivo dxf com os vertices de um txt
    try:
        doc = ezdxf.readfile(file_path)
        modelspace = doc.modelspace()
    except IOError:
        doc = ezdxf.new()
        modelspace = doc.modelspace()

    lwpolyline = modelspace.add_lwpolyline(points=vertices, close=fechar)
    
    doc.saveas(file_path)
    print("LWPOLYLINE inserida ou editada no arquivo:", file_path)


def create_pole(file_path,vertices, tam, vao):
    try:
        doc = ezdxf.readfile(file_path)
        modelspace = doc.modelspace()
    except IOError:
        doc = ezdxf.new()
        modelspace = doc.modelspace()

    lwpolyline = modelspace.add_lwpolyline(points=vertices)
    
    doc.saveas(file_path)
    print("LWPOLYLINE inserida ou editada no arquivo:", file_path)
    ...


def read_and_print_blocks(file_path): # Uso futuro...
    try:
        doc = ezdxf.readfile(file_path)

        for block in doc.blocks:
            print("Nome do bloco:", block.name)

            for entity in block:
                print("Tipo de entidade:", entity.dxftype())

            print()  # Linha em branco para separar os blocos

    except Exception as e:
        print("Erro:", str(e))
    finally:
        doc.close()





if __name__ == "__main__":
    ramalA_dxf = "data/perfil/ramalA.dxf"
    ramalA_txt = "data/perfil/ramalA.txt"
    lwpolyline_dxf = "data/perfil/create_lwpolyline.dxf"
    
    estacas_txt = "data/perfil/estacas.txt"
    
    tam = 10
    vao = [100,200,300,400,500]
    
    
    # tracado_dxf = "data/tracado/tracado.dxf"
    
    # path_write2 = "data/perfil/test_class.txt"
    
    
    
    perfil = get_lwpolyline_vertices(ramalA_dxf, ramalA_txt) #O perfil enviado e salva os vrtices no txt
    print(f"N vertices antes {len(perfil)}")
    # perfil.add_vertice(4000,200)
    
    # print(perfil)
    # print(len(perfil))
    # perfil._add_vertice_x(100)
    perfil.add_estruturas(vao)
    print(f"N vertices antes {len(perfil)}")
    perfil.save_txt(estacas_txt)
    # perfil._sort_num()
    # print(perfil)
    # print(vert)
    # print(type(vert))
    # create_lwpolyline(lwpolyline_dxf, vert)


    # read_and_print_blocks(tracado_dxf)

