import numpy as np
import matplotlib.pyplot as plt

archivo = np.loadtxt("fecha_manchas.dat")
x = archivo[:,0]
y = archivo[:,1]

plt.plot(x,y,c = "m")
plt.xlabel("Tiempo(years)")
plt.ylabel("Manchas Solares")
plt.title("Manchas Solares en el Tiempo")
plt.savefig("fecha_manchas.pdf")
