
import numpy as np 


data = np.loadtxt('monthrg.dat')
year = data[:,0]
month = data[:,1]
days = data[:,2]
manchas = data[:,3]


#Eliminamos los datos antes 1900
ii = (days>0) & (year>1900)
manchas = manchas[ii]
t = year[ii] + month[ii]/12.0

nuevo_a = np.array([t,manchas])
nuevo = np.transpose(nuevo_a)

np.savetxt("fecha_manchas.dat", nuevo)




