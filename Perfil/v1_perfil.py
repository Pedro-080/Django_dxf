# flake8: noqa
# Estudo sobre tratamento de DXF
# VERSÃO - V1 perfil
# Empranchamento de perfil

from Functions import  *


if __name__ == "__main__":
    perfil_original = "data/layout/Perfil_0A.dxf"
    
    perfil_copia = "data/layout/Perfil_0A_copia.dxf"
    perfil_limpo = "data/layout/Perfil_0A_LIMPO.dxf"
   
    
    # doc_copia = ezdxf.readfile(perfil_copia)
    # doc_limpo = ezdxf.readfile(perfil_limpo)
    
    
    
    # inspecionar_bloco(doc_copia ,"Carimbo Babilonia")
    # inspecionar_bloco(doc_limpo,"Carimbo Babilonia")
    
    numero_layout = 3
    #===================FUNCIONANDO========================
    # positions = busca_texto(perfil_original)
    # grifar(perfil_original,perfil_copia,positions)
    
    doc = carregar(perfil_original)
    
    
    
    
    # Cria um conjunto de layouts na quantidade da variável numero_layout
    doc = criar_layouts(doc,numero_layout)
 
     #Lista todos os blocos nomeados do arquivo original
    # lista_blocos = listar_blocos(doc)   
    
    # Insere o carimbo "Carimbo Babilonia" em todos os layouts
    doc = inserir_carimbo(doc,"Carimbo Babilonia",numero_layout)
    
    
    # doc = definir_area_viewport(doc)
    
    inspecionar_bloco(doc,"Carimbo Babilonia")
    # doc = circular(doc,(0,0))
    # definir_area_viewport(doc)
    # inserir_viewport(doc,numero_layout)
    # 
    
    
    
    
    
    
    # salvar(doc,perfil_copia)
    # print(lista_blocos)
    
    #======================================================


    


    
    
    
    
    
    # for bloco in lista_blocos:
    #     if bloco == "Carimbo Babilonia":
    #         print("O bloco exite")
    
    
    # criar_layout(perfil_original,perfil_copia,"04")
    # criar_layout(perfil_original,perfil_copia,"05")
    
    

    
    # duplicate_layout(perfil_original,"01","02",perfil_copia)
    
    # all_layouts=listar_numero_layouts(perfil_original)

    # all_layouts = list_all_layouts(perfil_original)
    # num_layouts = listar_numero_layouts(perfil_original)
    
    # print(all_layouts)
    # all_layouts = listar_layouts_sem_model(perfil_original)
    
    
    
    
    # print(all_layouts)
    # print(num_layouts)
    
    
    # duplicar_layout(perfil_original,"01","02",perfil_copia)
    
    
    
    # for layout_name in all_layouts:
    #     print(layout_name)
    
    
    
    # catenaria_dxf = "data/perfil/catenaria_new.dxf" 
    # test_catenaria_dxf = "data/perfil/test_catenaria_new.dxf" 
  
            
    # ramalA_dxf = "data/perfil/ramalA.dxf"                       #Arquivo fonte do perfil    
    # ramalA_txt = "data/perfil/ramalA.txt"                       #Arquivo que receberá o txt do perfil
    
    # lwpolyline_dxf = "data/perfil/create_lwpolyline.dxf"        #Arquivo em que será salvo o perfil final
    
    # estacas_txt = "data/perfil/estacas.txt"
    
    # tam = 10                                                    #Altura util das estruturas
    # # vao = [0,100, 100, 100, 100, 100, 54.12,123.45]                           #Lista com o comprimento dos vaos 
    # # vao =[40,87.32,78.16,39.16,45.65,65.53,81.17,95,95,95,95,95,95,95,95,95,95,95,95,95,95,95,95,95,95,95,95,95,95,95,95,90,90,74,74,75.36,80,76,76.43,84.67]
    # vao =  [0,70,87.32,78.16,39.16,45.65,65.53,81.17,95,95,95,95,95,95,95,95,95,95,95,95,95,95,95,95,95,95,95,95,95,95,95,95,90,90,74,74,75.36,80,76,76.43]
    
    # estacas = [sum(vao[:i + 1]) for i in range(len(vao))]       #Converte a lista de vaos em estaqueamento 
    #                                                             #progressivo
    # print(f"estacas: {estacas}")
    # perfil = get_lwpolyline_vertices(ramalA_dxf, ramalA_txt)    #O perfil enviado e salva os vertices no txt
    # # print(f"N vertices antes {len(perfil)}")

    
    # perfil.add_estruturas(estacas)                              #Cria os vértices no perfil na posição de cada
    # # print(f"N vertices antes {len(perfil)}")                  #estaca
    
    # perfil.save_txt(estacas_txt)                                #Salva o novo perfil em um novo txt                              
    
    
    
    # limpar_arquivo(lwpolyline_dxf)
    
    # create_lwpolyline(lwpolyline_dxf, perfil.poins_tuple())     #Cria um novo arquivo dxf com os novos pontos de perfil





    # estruturas = create_pole(lwpolyline_dxf,perfil,estacas)                  #insere os postes no novo arquivo criado

    # # print(type(estruturas))
    # # print(estruturas)


    # # To = 1545 #kgf 
    # To = 400 #kgf
    # p= 0.7816  #kgf/m

    
    # vaos = []
    # create_vao(lwpolyline_dxf,estruturas,To,p)
    
    



