import pandas as pd 
import numpy as np
from Biblioteca import *

class Estrutura:
    def __init__(self) -> None:
        self.__nome = None
        self.__coordx = None
        self.__coordy = None
        pass
    
    def normalizar(self,ponto1,ponto2,T,H):#Normaliza a força, dado dois pontos e a força
        L=self.distancia(ponto1,ponto2)
        T_normal=L*T/H
        return T_normal
        pass   

    def distancia(self,p1,p2):#Retorna a distancia entre 2 pts, usa polimorfia
        if (is_iterable(p1) and is_iterable(p2)):                   
            if(len(p1)==len(p2)):                                      
                L=np.sqrt(sum([(x - y)**2 for x, y in zip(p1, p2)]))
            else:
                print("Os pontos precisam das mesmas dimensões")
                return None
        else:
            L=abs(p1-p2)
        return L

    def localizacao(self,coordx,coordy):
        self.__coordx=coordx
        self.__coordy=coordy
