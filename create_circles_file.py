# flake8: noqa
# Estudo sobre criação de circulos em coordenadas
# VERSÃO - V01

from modules.Functions import *

def ler_arquivo_txt(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        linha = arquivo.readline()
        valores = linha.split(',')
        x = float(valores[0])
        y = float(valores[1])
        z = float(valores[2])
    return x, y, z


if __name__ == "__main__":

    pontos_txt = "data/txt/casas_impactadas.txt" 

    pontos_dxf = "data/txt/casas_impactadas.dxf"                #Arquivo em que será salvo o perfil final

    

    tam = 250                                                    #Raio dos circulos criados

    x,y,z = ler_arquivo_txt(pontos_txt)
    print(f"x {x}, y {y}, z {z}")


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
    
    

    
    


    # # deslocamento_y = 12
    # # vertices = [(10,40),(450,0)]
    # # limpar_arquivo(test_catenaria_dxf)
    # vertices = [(0,1456.4416),(100,1433.6451)]
    # create_catenaria(test_catenaria_dxf,vertices,p,To)
    


