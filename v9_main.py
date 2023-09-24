# flake8: noqa
# Estudo sobre tratamento de DXF
# VERSÃO - V9
# Cálculo de catenaria

from modules.Functions import *

if __name__ == "__main__":
    catenaria_dxf = "data/perfil/catenaria_new.dxf" 
    test_catenaria_dxf = "data/perfil/test_catenaria_new.dxf" 
  
            
    ramalA_dxf = "data/perfil/ramalA.dxf"                       #Arquivo fonte do perfil    
    ramalA_txt = "data/perfil/ramalA.txt"                       #Arquivo que receberá o txt do perfil
    
    lwpolyline_dxf = "data/perfil/create_lwpolyline.dxf"        #Arquivo em que será salvo o perfil final
    
    estacas_txt = "data/perfil/estacas.txt"
    
    tam = 10                                                    #Altura util das estruturas
    vao = [0,100, 100, 100, 100, 100]                           #Lista com o comprimento dos vaos 
    
    
    
    estacas = [sum(vao[:i + 1]) for i in range(len(vao))]       #Converte a lista de vaos em estaqueamento 
                                                                #progressivo
    print(f"estacas: {estacas}")
    perfil = get_lwpolyline_vertices(ramalA_dxf, ramalA_txt)    #O perfil enviado e salva os vertices no txt
    # print(f"N vertices antes {len(perfil)}")

    
    perfil.add_estruturas(estacas)                              #Cria os vértices no perfil na posição de cada
    # print(f"N vertices antes {len(perfil)}")                  #estaca
    
    perfil.save_txt(estacas_txt)                                #Salva o novo perfil em um novo txt                              
    
    
    
    # limpar_arquivo(lwpolyline_dxf)
    
    create_lwpolyline(lwpolyline_dxf, perfil.poins_tuple())     #Cria um novo arquivo dxf com os novos pontos de perfil





    estruturas = create_pole(lwpolyline_dxf,perfil,estacas)                  #insere os postes no novo arquivo criado

    # print(type(estruturas))
    # print(estruturas)


    # To = 1545 #kgf 
    To = 600 #kgf
    p= 0.7816  #kgf/m

    
    vaos = []
    create_vao(lwpolyline_dxf,estruturas,To,p)
    
    

    
    


    # deslocamento_y = 12
    # vertices = [(10,40),(450,0)]
    # limpar_arquivo(test_catenaria_dxf)
    vertices = [(50,100),(450,40)]
    create_catenaria(test_catenaria_dxf,vertices,p,To)
    


