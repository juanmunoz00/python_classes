##Usando Python 2.7
##Definicion de listas
productos = ["np001", "np002", "np003", "np004"]
resultados_de_pruebas_temp = [30, 28.4, 40, 25]
resultados_de_pruebas_humedad = [88.6, 90, 79.9, 99.9]
##Muestra listas
print(productos)
print(resultados_de_pruebas_temp)
print(resultados_de_pruebas_humedad)
##Agrega un elemento a la lista
prod_nuevo = "np005"
productos.append(prod_nuevo)
print(productos)

temp = 95.3
humedad = 98.3

resultados_de_pruebas_temp.append(temp)
resultados_de_pruebas_humedad.append(humedad)

print(resultados_de_pruebas_temp)
print(resultados_de_pruebas_humedad)
##Obtener el indice de un elemento
prod = "np003"
i = productos.index(prod)
print("El indice de " + prod + " es: " + str(i))

##Modificando el valor del elemento
temp_nueva = input("Cual es valor de temp a modificar?")
resultados_de_pruebas_temp[i] = temp_nueva
print(resultados_de_pruebas_temp)

"""
##Eliminar un elemento de la lista por valor del elemento
np = raw_input('np? ')
##print(np)

##i = productos.index(np)
productos.remove(np)
print(productos)
"""
##Eliminar un elemento de la lista por indice
np = raw_input('np? ')
i = productos.index(np)
print("i: " + str(i))
productos.pop(i)
resultados_de_pruebas_temp.pop(i)
resultados_de_pruebas_humedad.pop(i)

print(productos)
print(resultados_de_pruebas_temp)
print(resultados_de_pruebas_humedad)

print("La cantidad de elementos en la lista de productos es: " + str(len(productos)))
print("La cantidad de elementos en la lista de temps es: " + str(len(resultados_de_pruebas_temp)))
print("La cantidad de elementos en la lista de humedades es: " + str(len(resultados_de_pruebas_humedad)))
