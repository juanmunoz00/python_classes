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
        ##print("Temp: " + str(self.temp))
        if( (self.temp < self.TEMP_LIMITE_INF) ):
            print("La tempreatura esta abajo del limite")
        if( (self.temp > self.TEMP_LIMITE_SUP) ):
            print("La tempreatura esta arriba del limite")
        else:
            print("La temperatura es nominal")

    def Listas(self, lista2):
        print(self.lista)
        print(lista2)

class Cl2:
    def __init__(self, num_empledo, nombre, depto):
        self.num_empledo = num_empledo
        self.nombre = nombre
        self.depto = depto