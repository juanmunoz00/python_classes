import random

##Definimos la lista
milista = ["Ford", "Toyota", "Nissan", "Dodge", "Masserati"]
##Imprimimos la lista
print(milista)
print("****************************************")
##Agregamos un elemento a la lista
milista.append("Porshe")
##Imprimimos la lista
print(milista)
print("****************************************")
##Cuantos elementos tiene la lista?
print("La lista tiene " + str(len(milista)) + " elementos")
print("****************************************")
##Indice de un elemento
marca = "Nissan"
print("El indice del elemento " + marca + " es: " + str(milista.index(marca) + 1))
print("****************************************")
marca = "Toyota"
print("Removiendo la marca " + marca)
milista.remove(marca)
print(milista)
print("****************************************")
##Remvemos por indice
_index = 2
print("Remover el elemento " + milista[_index])
milista.pop(_index)
print(milista)
print("****************************************")
##Ordenar
print("Ordenar alfabeticamente la lista")
milista.sort()
print(milista)

print("Z-A la lista")
milista.sort(reverse=True)
print(milista)
print("****************************************")
tamano_arreglo = random.randint(1, 10)
print("Un numero enterio aleatorio: " + str(tamano_arreglo))

#Generar una lista de numeros aleatorios
arrNum=[]
for x in range(tamano_arreglo):
    ale = random.randint(1, 99)
    arrNum.append(ale)

print(arrNum)

for i in arrNum:
    print(i)## i es el elemento del arreglo

##print(arrNum)

