import matplotlib.pyplot as plt
import numpy as np

Ae=800.2568

def calc_fx(x):
    C1 = 1545/0.7816
    fx = C1*(np.cosh(x/C1)-1)
    return fx-fx[0]+40
    ...


# Seus valores de x e y
x = np.linspace(0, 350, 101) 
y = calc_fx(x-Ae/2)

x_inv = [valor_x *-1 + 350 for valor_x in x]
y_inv = [valor_y *-1 for valor_y in y]


# plt.figure(figsize=(10, 8))
# plt.plot(x, y)
# plt.plot(x_inv,y)
# plt.grid()
# plt.show()




# # Inverter os valores de x e y
# x_invertido = [valor_x * -1 for valor_x in x]
# y_invertido = [valor_y * -1 for valor_y in y]

# # Crie o gráfico com os valores de x e y invertidos
# plt.plot(x_invertido, y_invertido)

# # Adicione rótulos aos eixos
# plt.xlabel('Eixo X (invertido)')
# plt.ylabel('Eixo Y (invertido)')

# # Exiba o gráfico
# plt.show()
