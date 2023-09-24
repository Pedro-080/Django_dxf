from modules import *


class Vao:
    def __init__(self, estrutura_inicial, estrutura_final):
        self.Estrutura_inicial = estrutura_inicial
        self.Estrutura_final = estrutura_final

        self.comprimento = self._calc_comprimento()
        
        self.pt_inicial = self.Estrutura_inicial.coord_topo
        self.pt_final = self.Estrutura_final.coord_topo
        
        
        self.T = None
        self.p = None
        
        self.cat_nivel1 = None
        
        pass

    def __str__(self):
        print(f" Vão entre {self.Estrutura_inicial} e {self.Estrutura_final}")
    
    
    def set_cabo_esticamento(self, T, p ):
        self.T = T
        self.p = p
        
    
    def add_estruturas(self, pt_inicial, pt_final): #Obsoleto
        self.pt_inicial = pt_inicial
        self.pt_final = pt_final
 
 
    def _calc_comprimento(self):
        
        comprimento = abs(self.Estrutura_final.coord_base[0] - self.Estrutura_inicial.coord_base[0])
        # print(f"{self.Estrutura_final.coord_base[0]} - {self.Estrutura_inicial.coord_base[0]} = {comprimento}")
        return comprimento
        pass
    
    def create_cat_nivel1(self,T, p):
        vert = [self.pt_inicial,self.pt_final]
        
        cat_nivel1 = Catenaria(vert,p,T)
        x,fx = cat_nivel1._calc()
        vertices = list(zip(x,fx))
        return vertices
        # print(f"self.pt_inicial: {self.pt_inicial}")
        # pass