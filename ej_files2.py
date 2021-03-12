from csv import writer
from csv import reader

import random
import pandas as pd 
from os import system, name
import os



"""
- Se genera una lista en blanco. Usando un ciclo for se generan numeros aleatorios y se agregan a la lista.
"""
lista_numeros_de_parte = []

for i in range(10):
    numero_de_parte = "NP0"+str(random.randint(1, 99))
    lista_numeros_de_parte.append(numero_de_parte)

#print(lista_numeros_de_parte)

"""
- Se crean 2 objetos csv: uno de lectura (read_obj) y uno de escritura (write_obj).
- read_obj aloja el contenido del archivo csv al que le agregaremos la columna.
- write_obj es un archivo csv nuevo

- Se crea un ciclo con read_obj el cual iterará linea por linea. Cada una la guarda en la variable row.

- Se inicializa un contador de indice para la lista de numeros de parte. Se itera y concatena la "," (coma) al contenido de row.

- Despues del ciclo se guarda el archivo write_obj
"""
with open('20200220000948.csv', 'r') as read_obj, \
        open('output_1.csv', 'w', newline='') as write_obj:
    
    csv_reader = reader(read_obj)    
    csv_writer = writer(write_obj)
    
    indx = 0
    for row in csv_reader:        
        newTextColumn = "," + lista_numeros_de_parte[indx]
        row.append(newTextColumn)
        
        csv_writer.writerow(row)

print("¡Listo!")
