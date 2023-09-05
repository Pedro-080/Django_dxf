import numpy as np
import matplotlib.pyplot as plt

class Catenaria:
    def __init__(self,vertices,p,To):
        self.vertices = vertices
        self.p1,self.p2 = vertices[0],vertices[1]
        self.x_min = None
        self.x_max = None
        self.y_min = None 
        self.y_max = None
        self.Ae = None
        self.vao = None
        self.p = p
        self.To = To
        self.C1 = self.To/self.p
        
        self._calc_extremos()
        
        # self.p1,self.p2 = self._calc_vertices()
        
        self.desl_y = abs(self.p2[1]-self.p1[1])
        

        
        self.n_div = 100
        
        ...

    def _calc(self):        
        # x = np.linspace(self.x_min,
        #                 self.x_min+self.Ae,
        #                 self.n_div+1)
        x = np.linspace(self.x_min,
                        self.x_max,
                        self.n_div+1)        
       
        fx = self._calc_catenaria(x-self.Ae/2-self.x_min)    
        
        fo = self.p*self.vao**2/(8*self.To)
        
        plt.figure(figsize=(10, 8))
        plt.plot(x, fx, label=f'vão de {self.vao} metros \ntração de {self.To:.2f} kgf \npeso do cabo de {self.p} kg/m')

        # show_eixo_x = [self.x_min,self.x_min+self.vao,self.Ae+self.x_min]
        show_eixo_x = [self.x_min,self.x_max]
        show_eixo_y = [self.y_min,self.y_max,fx[50]]


        plt.xlabel('x')
        plt.ylabel('f(x)')
        plt.title('Gráfico da catenaria')
        plt.legend()
        plt.grid()

        plt.xticks(show_eixo_x)
        plt.yticks(show_eixo_y)

        plt.show()
        return x, fx
        ...
        
    def _calc_catenaria(self,x): #Calculo da catenária com deslocamento
        # fx = self.C1*(np.cosh(x/self.C1)-1)-\
        #               self.y_max
        fo = self.p*self.vao**2/(8*self.To)
        fe = self.p*self.Ae**2/(8*self.To)
        xo = abs(self.p1[0]-self.Ae+self.x_min)
        print(f"xo: {xo}")
        # fx = self.C1*(np.cosh(x/self.C1)-1)
        print(f"fo: {fe:.4f}")
        fx = self.C1*(np.cosh(x/self.C1)-1)
        return fx-fx[0]+self.p1[1]
        ...
        
    def get_pontos(self):
        print(f"p1: {self.p1}")
        print(f"p2: {self.p2}")
        ...
        # [(50,10),(400,10)]
        
    def _calc_extremos(self):
        self.x_min = min(self.p1[0],self.p2[0])
        self.x_max = max(self.p1[0],self.p2[0])
        self.y_min = min(self.p1[1],self.p2[1])
        self.y_max = max(self.p1[1],self.p2[1])
        self.vao = abs(self.x_max-self.x_min)
        # self.Ae = self.vao+2*abs(self.y_max-self.y_min)*self.To/(self.vao*self.p)-self.x_min
        self.Ae = self.vao+2*self.C1*np.arcsinh(abs(self.y_max-self.y_min)/(2*self.C1)* 1/np.sinh(self.vao/(2*self.C1)))
        ...
        ...
        
    def _calc_vertices(self):
        p1 = self.vertices[0]
        p2 = self.vertices[1]

        if p1[0]<p2[0]:
            return p1,p2
        else:
            return p2,p1
        ...
    
    def _calc_vao(self): return abs(self.p2[0]-self.p1[0])