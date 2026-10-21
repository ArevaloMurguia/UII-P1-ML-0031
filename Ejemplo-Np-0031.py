import numpy as np

Califas=np.array([60,70,90])
print(" --------- Ej 1 Imprimir Califas ----------")
print(Califas)   # Imprime la lista de Califas
print(type(Califas))  # Muestra el tipo de arrreglo
print(" --------- Ej 2 Dimensiones de un array ----------")
Califas=np.array(60)
print(Califas)
print("Dimension : ", Califas.ndim)
print(" --------- Ej 1 Dimension de un array ----------")
Califas=np.array([60,70,90])
print(Califas)  
print("Dimension : ", Califas.ndim)
print(" --------- Ej 2 Dimensiones de un array ----------")
Califas=np.array([
    [60,70,90]
    [50,80,98]
    ]) # Un arreglo de 2 dimensiones es como una tabla en excel
print(Califas)  
print("Dimension : ", Califas.ndim)