from ezdxf.layouts import Paperspace
from ezdxf.document import Drawing
import numpy as np

from Functions_debug import grifar,add_retangulo
from itertools import groupby
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import DBSCAN

def busca_texto(doc: Drawing):
    msp = doc.modelspace()

    texts = [entity for entity in msp if entity.dxftype() == 'MTEXT' or entity.dxftype() == 'TEXT']
    
    positions = []
    
    
    for text in texts:
        try:
            # Tenta converter o valor do texto encontrado para inteiro, caso consiga, insere no fim da lista positions
            text.dxf.text = int(text.dxf.text)
            positions.append((np.round(text.dxf.insert[0],4),
                              np.round(text.dxf.insert[1],4)))
            
            # print(f'Texto: {text.dxf.text},Typo: {type(text.dxf.text)} , Posição: ({text.dxf.insert[0]},{text.dxf.insert[1]})') 
        except:
            None
    
    
    
    # print(positions)
    pontos_agrupados = agrupar_pontos(positions)
    print(f"Existem : {len(pontos_agrupados)/2} Perfis")
    
    

    for region in pontos_agrupados:
        add_retangulo(doc,region)
    
    # grifar(doc,positions)
    
    
    
    return positions





def agrupar_pontos(pontos,intervalo_maximo_y=200):
    
    # print(f"Existem: {len(pontos)} pontos")
    
    # Ordena os pontos em ordem crescente da coordenada x 
    pontos_ordenados = sorted(pontos, key=lambda p:p[0])
    
    # Agrupa os pontos que possuem valor igual para x
    pontos_agrupados = [list(v) for k, v in groupby(pontos_ordenados, lambda p: p[0])]

    # Ordena os pontos de cada grupo de acordo com o valor de y
    novo_pontos_ordenados = [sorted(lista, key=lambda ponto: ponto[1]) for lista in pontos_agrupados ]
    
   
    result=[]
    lista = []
       
    
    # Separa os pontos que possuem mesmo valor de x em grupos afastados mais que o intervalo_maximo_y
    for grupo in novo_pontos_ordenados:
        for ponto_anterior, proximo_ponto in zip(grupo, grupo[1:]):
            lista.append(ponto_anterior) 

            if proximo_ponto[1] - ponto_anterior[1] >= intervalo_maximo_y :
                
                result.append(lista)
                lista=[]
 
            if ponto_anterior == grupo[-2]:
                lista.append(grupo.pop())
                
        result.append(lista)
        lista=[]   
                        
    return result

