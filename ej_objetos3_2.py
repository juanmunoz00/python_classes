import csv
import pandas as pd 
from os import system, name
import os

class NP:
    ##Class constants
    TEMP_LIMITE_SUP = 200
    TEMP_LIMITE_INF = 50

    ##Class properties definition
    def __init__(self, np, temp, rH, lista):
        self.np = np
        self.temp = temp
        self.rH = rH
        self.lista = lista

    ## Methods
    def Compara_Con_Limites(self):
        if( (self.temp < self.TEMP_LIMITE_INF) ):
            print("La tempreatura esta abajo del limite")
        if( (self.temp > self.TEMP_LIMITE_SUP) ):
            print("La tempreatura esta arriba del limite")
        else:
            print("La temperatura es nominal")

    def Listas(self, lista2):
        print(self.lista)
        print(lista2)

##All files in directory
for filename in os.listdir(directory):
    print(filename)

fileName = r'20200220000947.csv'
fullPath = r'C:\dev1\py\20200220000947.csv'

data = pd.read_csv(fullPath) 
print(data)

"""
with open(fullPath, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
"""

"""
lista1 = ['uno', 'dos', 'tr3s']
##np1 is the class instance (copy)
np1 = NP('np001', 100, 50, lista1) 
##Display the class properties
print (str(np1.TEMP_LIMITE_SUP))
print (str(np1.TEMP_LIMITE_INF))
print(np1.lista)
print (str(np1.np))
print (str(np1.temp))
print (str(np1.rH))

##The class method
np1.Compara_Con_Limites()

##A class with a value *external* to the class but taken as parameter.
lista2 = ['one', 'two', 'three']
np1.Listas(lista2)
"""