import numpy as np
import matplotlib.pyplot as plt

class Catenaria:
    def __init__(self,vao,p,To):
        self.vao = vao
        self.p = p
        self.To = To
        self.C1 = self.To/self.p
        self.n_div = 100
        # self._calc()
        
        pass
    
    def _calc(self):
        x = np.linspace(-self.vao/2, self.vao/2, self.n_div+1)
        fx = self.C1*(np.cosh(x/self.C1)-1)
        fo = self.p*self.vao**2/(8*self.To)
        plt.figure(figsize=(10, 8))
        plt.plot(x, fx, label=f'vão de {self.vao} metros \n tração de {self.To:.2f} kgf \n peso do cabo de {self.p} kg/m')
        show_eixo_x = [-self.vao/2,0, self.vao/2]
        show_eixo_y = [0,fo]


        plt.xlabel('x')
        plt.ylabel('f(x)')
        plt.title('Gráfico da catenaria')
        plt.legend()
        plt.grid()
        # plt.scatter(eixo_x,eixo_y)
        plt.xticks(show_eixo_x)
        plt.yticks(show_eixo_y)

        plt.xlim(-self.vao/2*1.1,self.vao/2*1.1)

        plt.show()
        return x, fx
        ...