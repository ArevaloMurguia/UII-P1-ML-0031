import numpy as np

print("--------- Llenar Matriz de ceros ---------")
Matriz=np.zeros([3,5]) # 3 filas x 5 columnas 
print(Matriz)
print("--------- Llenar Matriz de unos ---------")
Matriz=np.ones([3,5])
print(Matriz)
print("--------- Llenar Matriz vacios ---------")
Matriz=np.empty([3,5])
print(Matriz)
print("--------- Llenar Lista con rango ---------")
# El primer parametro es el valor inicial
# El segundo parametro es el valor final
# El tercer parametro es el incremento
Lista=np.arange(0,10,2)
print(Lista)
print("--------- Llenar Lista con rango No 2---------")
Lista=np.arange(0,10,1)
print(Lista)