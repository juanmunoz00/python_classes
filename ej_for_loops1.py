import random

print('Curso: Python para no-programadores')
print('Autor: Juan Munoz') 
print('https://github.com/juanmunoz00/python_classes')
print('*********************************************')
print('******** ESTRUCTURAS DE CONTROL *************')
print('******** Ciclos iterativos for y while   ****') 
print('*********************************************')
opcion = 2
subOpcion = 5
if( opcion == 1 ):
    print("While loop")
    #Ciclo while iterara mientras se cumpla una condicion
    i = 0
    limit = 9
    while( i <= limit):
        print(i)
        i+=1 ##Si no incrementamos el iterador el ciclo se vuelve infinito (hasta que se acabe la energia)

if( opcion == 2 ):
    print("For loop")
    if( subOpcion == 1 ):
        ##Imprimimos un valor numerico entre 0 y 9
        for i in range(10):
            print(i)
    if( subOpcion == 2 ):
        ##Imprimimos un valor numerico entre 10 y 20
        for i in range(10, 21):
            print(i)
    if( subOpcion == 3 ):
        ##Imprimimos un valor numerico entre 10 y 20 con intervalos de 2
        for i in range(10, 21, 2):
            print(i)
    if( subOpcion == 4 ):
        print("Iterando a traves de una lista")
        ##Iterar una lista
        lista = ["Juan", "Yadira", "Chino", "Tucita"]
        for i in lista:
            print(i)
    if( subOpcion == 5 ):
        print("Iterando a traves de una lista de numeros aleatorios")
        ##Iterar una lista
        numeros_aleatroios = []
        for i in range(10):
            num_aleatorio = random.uniform(0.0, 100.0)
            numeros_aleatroios.append(num_aleatorio)
        
        for j in numeros_aleatroios:
            print(j)