# flake8: noqa
# Estudo sobre tratamento de DXF
# VERSÃO - V7
# Cálculo de catenaria

from modules.Functions import *


if __name__ == "__main__":
    ramalA_dxf = "data/perfil/ramalA.dxf"
    ramalA_txt = "data/perfil/ramalA.txt"
    
    lwpolyline_dxf = "data/perfil/create_lwpolyline.dxf"
    
    estacas_txt = "data/perfil/estacas.txt"
    
    tam = 10
    vao = [0,100, 100, 100, 100, 100]
    
    estacas = [sum(vao[:i + 1]) for i in range(len(vao))]
    
    print(f"estacas: {estacas}")
    perfil = get_lwpolyline_vertices(ramalA_dxf, ramalA_txt) #O perfil enviado e salva os vrtices no txt
    # print(f"N vertices antes {len(perfil)}")

    
    perfil.add_estruturas(estacas)
    # print(f"N vertices antes {len(perfil)}")
    perfil.save_txt(estacas_txt)
    
    create_lwpolyline(lwpolyline_dxf, perfil.poins_tuple())

    create_pole(lwpolyline_dxf,perfil,estacas)

