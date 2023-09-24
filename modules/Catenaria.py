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
        self.fe = None
        self.vao = None
        self.p = p
        self.To = To
        self.C1 = self.To/self.p
        self.Y_scale = 10
        self._calc_extremos()       
               
        self.n_div = 100
        ...

    def _calc(self):        
        # print(f"p1: {self.p1[1]}") 
        # print(f"p2: {self.p2[1]}")    
        
        x = np.linspace(self.x_min,
                        self.x_max,
                        self.n_div+1)            
        
        fx = self._calc_catenaria(x-self.Ae/2-self.x_min)   
            
        
        if self.p2[1]<=self.p1[1]: # Ponto inicial mais alto que o final
            # print(f"x - p1 maior")

            # self.plotar(x,fx)
            return x, fx
                     
        else:  # Ponto final mais alto que o inicial 
            # print(f"x - p2 maior")
            
            x_inv = list(reversed(x))
            # self.plotar(x_inv,fx)
            return x_inv, fx
            
        # fx = self._calc_catenaria(x-self.Ae/2-self.x_max-self.Ae) 
        # fx = self._calc_catenaria(x) 
        # fo = self.p*self.vao**2/(8*self.To)
        


        return x, fx
        ...
        
    def _calc_catenaria(self,x): #Calculo da catenária com deslocamento
        fx = self.C1*(np.cosh(x/self.C1)-1)*self.Y_scale

        if self.p2[1]<=self.p1[1]:
            return fx-fx[0]+self.p1[1]
        else:
            return fx-fx[0]+self.p2[1]
        ...
        
    def get_pontos(self):
        print(f"p1: {self.p1}")
        print(f"p2: {self.p2}")
        ...

        
    def _calc_extremos(self):
        self.x_min = min(self.p1[0],self.p2[0])
        self.x_max = max(self.p1[0],self.p2[0])
        self.y_min = min(self.p1[1],self.p2[1])
        self.y_max = max(self.p1[1],self.p2[1])
        self.vao = abs(self.x_max-self.x_min)
        # self.Ae = self.vao+2*abs(self.y_max-self.y_min)*self.To/(self.vao*self.p)-self.x_min
        self.Ae = self.vao+2*self.C1*np.arcsinh(abs(self.y_max-self.y_min)/(2*self.C1)* 1/np.sinh(self.vao/(2*self.C1)))
        # self.Ae_1 = self.vao+(2*self.C1*abs(self.y_max-self.y_min)/(self.vao))
        # self.Ae_2 = self.vao+(2*self.To*abs(self.y_max-self.y_min)/(self.vao*self.p))
        ...
        
    def _calc_vertices(self): #obsoleto
        p1 = self.vertices[0]
        p2 = self.vertices[1]

        if p1[0]<p2[0]:
            return p1,p2
        else:
            return p2,p1
        ...
    
    def _calc_vao(self): return abs(self.p2[0]-self.p1[0]) #Obsoleto
    
    def plotar(self,x,y):
        plt.figure(figsize=(10, 8))
        plt.plot(x, y, label=f'Vão de {self.vao} metros \nTração de {self.To:.2f} kgf \nPeso do cabo de {self.p} kg/m')
        p1 = [self.p1[0],self.p2[0]]
        p2 = [self.p1[1],self.p2[1]]

        # Plotar os pontos
        plt.scatter(p1, p2, color='blue', marker='o')
        
        if self.vao >= self.Ae/2:
            show_eixo_x = [self.p1[0],self.p2[0]]
            show_eixo_y = [self.p1[1],self.p2[1], min(y)]
            self.fe = self.y_min - min(y)
            print(f"fe: {self.fe}")
        else: 
            show_eixo_x = [self.p1[0],self.p2[0]]
            show_eixo_y = [self.p1[1],self.p2[1]]

        plt.xticks(show_eixo_x)
        plt.yticks(show_eixo_y)


        plt.xlabel('x')
        plt.ylabel('f(x)')
        plt.title('Gráfico da catenaria')
        plt.legend()
        plt.grid()
        
        plt.show()

        ...
