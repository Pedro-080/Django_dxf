import numpy as np
import matplotlib.pyplot as plt

To = 1551.0428 #kgf
p= 0.7816  #kgf/m
vao = 350 # vao em m

C1=To/p

# Valores de x para o plot
x = np.linspace(-vao/2, vao/2, 101)

# Calcula o cosseno hiperbólico para cada valor de x
fx = C1*(np.cosh(x/C1)-1)
fo = p*vao**2/(8*To)

# print(fo)
# print(type(fx))
print(fx)

print(x)


# Plotagem do gráfico
plt.figure(figsize=(10, 8))
plt.plot(x, fx, label=f'vão de {vao} metros \n tração de {To:.2f} kgf \n peso do cabo de {p} kg/m')
show_eixo_x = [-vao/2,0, vao/2]
show_eixo_y = [0,fo]


plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Gráfico da catenaria')
plt.legend()
plt.grid()
# plt.scatter(eixo_x,eixo_y)
plt.xticks(show_eixo_x)
plt.yticks(show_eixo_y)

plt.xlim(-vao/2*1.1,vao/2*1.1)

plt.show()



