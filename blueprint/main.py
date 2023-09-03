import numpy as np
import matplotlib.pyplot as plt

# Parâmetros da catenária
a = 1.0
x1, y1 = 0, 0
x2, y2 = 4, 2

# Valores de t variando de 0 a d
d = np.sqrt((x2 - x1)**2 + (y2 - y1)**2)
t_values = np.linspace(0, d, 100)

# Equações paramétricas da catenária
x_values = x1 + (x2 - x1) * (t_values / d)
y_values = y1 + a * np.cosh(t_values / a)

# Plotagem do gráfico
plt.figure(figsize=(8, 6))
plt.plot(x_values, y_values, label='Catenária')
plt.scatter([x1, x2], [y1, y2], color='red', label='Pontos de fixação')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Gráfico da Catenária')
plt.legend()
plt.grid()
plt.show()