class Estrutura:
    def __init__(self,altura):
        self.altura = altura
        self.esforco = None
        
        self.altura_util = self._h_util()
        self.engastamento = self.altura-self.altura_util
        
        self.coord_base = None
        self.coord_topo = None
        ...
    
    def __str__(self):
        # return f"p base: {self.altura}/{self.esforco}"
        return f"p base: {self.coord_base}\np topo:/{self.coord_topo}"
    
    def __len__(self):
        pass
        ...
        
    def _h_util(self):
        return self.altura-self.altura*0.1+0.6
    
    def set_p_base(self,p_base):
        self.coord_base = p_base
        self._set_p_topo(p_base)
        return None
    
    def _set_p_topo(self,p_base):
        self.coord_topo = (p_base[0],p_base[1]+self.altura*10)
        return None
    