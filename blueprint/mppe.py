import matplotlib.pyplot as plt
import numpy as np


x1 = np.linspace(0, 100, 101)
y1 = np.exp(0.02*x1)

x2 = np.linspace(0, 100, 101)
y2 = x2*0.01

x3 = np.linspace(0, 100, 101)
y3 = np.exp(-0.02*x1)

#================================================
plt.subplot(1,3,1)
plt.plot(x1, y1,'b')

plt.xticks([])
plt.yticks([])

plt.xlabel('Comprimento da rede', fontsize=14)
plt.ylabel('Perdas por efeito Joule', fontsize=14)

plt.xlim(-10, 110) 
plt.ylim(-0.5, 10)

#================================================
plt.subplot(1,3,2)
plt.plot(x2, y2,'b')

plt.xticks([])
plt.yticks([])

plt.xlabel('Comprimento da rede', fontsize=14)

plt.ylabel('Queda de tensão', fontsize=14)
plt.xlim(-10, 110)
plt.ylim(-0.5, 2)

#================================================
plt.subplot(1,3,3)
plt.plot(x3, y3,'b')

plt.xticks([])
plt.yticks([])

plt.xlabel('Comprimento da rede', fontsize=14)
plt.ylabel('Nível de curto circuito', fontsize=14)

plt.xlim(-10, 110) 
plt.ylim(-0.2, 1.3)

#================================================




plt.show()