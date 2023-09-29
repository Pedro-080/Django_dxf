import pandas as pd 
import numpy as np
from Estrutura import Estrutura
from Biblioteca import *

class PosteDT(Estrutura):
    def __init__(self,altura,esforco):
        super().__init__()
        self.posicao = None
        self.Lado_a,self.Lado_b = [None]*2
        self.Lado_A,self.Lado_B = [None]*2
        self.altura  = altura
        self.esforco = esforco
        self.dimensoes_DT()
        self.engaste = altura*0.1+0.6
        self.h_util = altura-self.engaste
        self.h_normal = self.h_util-0.2
        self.h_cg_a = []
        self.h_cg_b = []
        self.area_cg_a = []
        self.area_cg_b = []
        pass

    def dimensoes_DT(self):
        a = 140 #Lado a da forma padrão, em mm 
        b = 110 #Lado b da forma padrão, em mm

        esf = [600,1000,1500,2000,2500,3000]
        h_esf = [0,1.5,3.0,4.5,6.0,7.5]
        altura_extra = dict(zip(esf,h_esf))

        self.Lado_a=self.calc_lado_A(a,altura_extra[self.esforco])
        self.Lado_b=self.calc_lado_B(b,altura_extra[self.esforco])
        self.Lado_A=self.calc_lado_A(self.Lado_a,self.altura)
        self.Lado_B=self.calc_lado_B(self.Lado_b,self.altura)

        pass
    
    def calc_lado_A(self,a,h): return a+28*h
    def calc_lado_B(self,b,h): return b+20*h
    def calc_Cg(self,a,A,h): return h/3*(2*a+A)/(a+A)
  
    def seccionamento(self,n=3):
        
        i=0
        lado_sup_a = [self.Lado_a]
        lado_sup_b = [self.Lado_b]
        lado_inf_a = []
        lado_inf_b = []
        cg_a = []
        cg_b = []

        lado_a_cg=[]
        lado_b_cg=[]

        seccao_div = self.h_util/n

        while i<n:
            
            lado_inf_a.append(self.calc_lado_A(lado_sup_a[-1],seccao_div))
            lado_inf_b.append(self.calc_lado_B(lado_sup_b[-1],seccao_div))

            cg_a.append(self.calc_Cg(lado_sup_a[-1],lado_inf_a[-1],seccao_div))
            cg_b.append(self.calc_Cg(lado_sup_b[-1],lado_inf_b[-1],seccao_div))

            lado_a_cg.append(self.calc_lado_A(lado_sup_a[-1],seccao_div-cg_a[-1]))
            lado_b_cg.append(self.calc_lado_B(lado_sup_b[-1],seccao_div-cg_b[-1]))

            self.area_cg_a.append(seccao_div*lado_a_cg[-1])
            self.area_cg_b.append(seccao_div*lado_b_cg[-1])

            if (i<n-1):
                lado_sup_a.append(lado_inf_a[-1])
                lado_sup_b.append(lado_inf_b[-1])
            self.h_cg_a.append(seccao_div*(n-1-i)+cg_a[i])
            self.h_cg_b.append(seccao_div*(n-1-i)+cg_b[i])
            i+=1

        self.area_cg_a = [num/1e3 for num in self.area_cg_a]
        self.area_cg_b = [num/1e3 for num in self.area_cg_b]
        # print("Div:%.2f"%seccao_div)
        # print("lado a")
        # print("sup ",arred(lado_sup_a,2))
        # print("inf ",arred(lado_inf_a,2))
        # print("cg: ",arred(lado_a_cg,2))
        # print("area",arred(self.area_cg_a,2))
        # print("lado b")
        # print("sup ",arred(lado_sup_b,2))
        # print("inf ",arred(lado_inf_b,2))
        # print("cg: ",arred(lado_b_cg,2))
        # print("area",arred(self.area_cg_b,2))

        return
        
    def normalizacao_vento(self,Atp,posi="Topo"):
        Atp_topo = []
        # cg = []
        # if posi == "Topo":
        #     cg=self.h_cg_b
        # elif posi == "Gaveta":
        #     cg=self.h_cg_a

        for i in range(len(Atp)):
                Atp_topo.append(self.normalizar(0,self.area_cg_a[i],Atp[i],self.h_normal))


        # print("H normal:",self.h_normal)
        # print("h_cg a:",self.h_cg_a)
        # print("h_cg b:",self.h_cg_b)
        # print("Atp:",Atp)
        # print("Atp topo:",Atp_topo)
        print("h_cg a:",arred(self.h_cg_a,2))
        print("h_cg b:",arred(self.h_cg_b,2))
        print("Atp:",arred(Atp,2))
        print("Atp topo:",arred(Atp_topo,2))
        return sum(Atp_topo)
        pass