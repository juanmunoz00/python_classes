class NP:
    ##Constantes en la clase
    TEMP_LIMITE_SUP = 200
    TEMP_LIMITE_INF = 50

    ##Definicion de los miembros(atributos) de la clase
    def __init__(self, np, temp, rH, lista):
        self.np = np
        self.temp = temp
        self.rH = rH
        self.lista = lista

    ## Metodos
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

##Instanciacion de la clase
lista1 = ['uno', 'dos', 'tr3s']
np1 = NP('np001', 100, 50, lista1)
print (str(np1.TEMP_LIMITE_SUP))
print (str(np1.TEMP_LIMITE_INF))
print(np1.lista)
print (str(np1.np))
print (str(np1.temp))
print (str(np1.rH))

np1.Compara_Con_Limites()

lista2 = ['one', 'two', 'three']
np1.Listas(lista2)