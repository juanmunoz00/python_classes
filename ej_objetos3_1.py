import clase1

##Object definition
listA = ['a','b','c']
listB = ['e','f','g']

NP = clase1.NP
EMP = clase1.Cl2

empleado = EMP(123, 'Joel', 'Pruebas')

print(empleado.nombre)

obj1 = NP('np001', 210, 100, listA)
obj2 = NP('np002', 70, 90, listA)

#Print an object property
##print("El NP1 es: " + str(obj1.np))
##print("El NP2 es: " + str(obj2.np))
print("El limite inferior de Temp es: " + str(obj1.TEMP_LIMITE_INF) + " y el limite superior es: " + str(obj1.TEMP_LIMITE_SUP))
print("Temp actual: " + str(obj1.temp))
obj1.Compara_Con_Limites()
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