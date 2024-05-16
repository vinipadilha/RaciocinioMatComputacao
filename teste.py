import matplotlib.pyplot as plt

import numpy as np
"""

fig = plt.figure(figsize=(5,5))

x = np.arange(-6 * np.pi,6*np.pi,0.1)
#print(x)

ySeno = np.sin(x)
plt.plot(x,ySeno, color='c')
plt.show( )
fig.savefig('grafico1.png')
"""


import math 
def convGrausRad(numero):
    rad = (numero/180) * math.pi
    return rad

print("-------- Funções Trigonométricas ----------")
angulo = float(input("Digite o valor em graus: "))
conv = convGrausRad(angulo)
print(f"Ângulo {angulo} em graus equivale a {conv:.2f} radianos")



