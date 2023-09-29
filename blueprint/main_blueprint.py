import pandas as pd
import numpy as np
from .Estrutura import Estrutura



class Vento(Estrutura):
    def __init__(self,Tmin,Teds,Tcoin,Alt,H_med,Vb):
        super().__init__()
        self.Tmin  = Tmin
        self.Teds  = Teds
        self.Tcoin = Tcoin
        self.Alt   = Alt
        self.H_med = H_med
        self.Vb    = Vb
        pass

    def massa_ar(self):
        ro = (1.293/(1+0.00367*self.Tcoin))*(\
             (16000+64*self.Tcoin-self.Alt)/\
             (16000+64*self.Tcoin+self.Alt))

        return ro

    def velocidade_vento(self):
        Kr = 1
        Kd_30s= 1.21
        Kd_2s = 1.41
        n_30s = 11
        n_2s  = 12 
        Vp_30s = Kr*Kd_30s*(self.H_med/10)**(1/n_30s)*self.Vb
        Vp_2s  = Kr*Kd_2s*(self.H_med/10)**(1/n_2s)*self.Vb

        return Vp_30s,Vp_2s

    def pressao_vento(self,N_m=0):

        Pv_30s = 0.5*self.massa_ar()*self.velocidade_vento()[0]**2
        Pv_2s = 0.5*self.massa_ar()*self.velocidade_vento()[1]**2

        if N_m == 0:
            Pv_30s = Pv_30s * 0.101972
            Pv_2s = Pv_2s * 0.101972

        return Pv_30s,Pv_2s
    
    # def vento_cabo(self,cabo,Vao,N=0):
    #     Cxi = 1
    #     a = 0.92
    #     cordoalha = Cabo(cabo)
    #     Ac_30s = self.pressao_vento(N)[0]*Cxi*a*cordoalha.d/1000*Vao
    #     Ac_2s = self.pressao_vento(N)[1]*Cxi*a*cordoalha.d/1000*Vao
    #     # Ac = self.pressao_vento()
    #     return Ac_30s,Ac_2s

    # def vento_isolador(self,isolador,N=0):
    #     Cxi = 1.2
    #     Ai_30s = self.pressao_vento(N)[0]*Cxi*isolador.area_isolador()
    #     Ai_2s = self.pressao_vento(N)[1]*Cxi*isolador.area_isolador()
    #     return Ai_30s,Ai_2s

    def vento_estrutura(self,poste):
        # h_normal=poste.h_util-0.2
        Cxtp = 2.2
        # Cxtp = 1.82
        poste.seccionamento(5)
        Atp_a=list(map(lambda x:x*self.pressao_vento()[0]*Cxtp,poste.area_cg_a))
        Atp_b=list(map(lambda x:x*self.pressao_vento()[0]*Cxtp,poste.area_cg_b))

        print(poste.normalizacao_vento(Atp_a))
        print(poste.normalizacao_vento(Atp_b))

        pass
# Marangatu