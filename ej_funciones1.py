print('Curso: Python para no-programadores')
print('Autor: Juan Munoz') 
print('https://github.com/juanmunoz00/python_classes')
print('*********************************************')
print('******** ESTRUCTURAS DE CONTROL *************')
print('******** Funciones   ************************') 
print('*********************************************')

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def mult(a, b):
    return a * b

def div(a, b):
    return a / b

a = 100
b = 10

print("La suma de " + str(a) + " y " + str(b) + " es: " + str(suma(a,b)))
print("La resta de " + str(a) + " y " + str(b) + " es: " + str(resta(a,b)))
print("La mult de " + str(a) + " y " + str(b) + " es: " + str(mult(a,b)))
print("La div de " + str(a) + " y " + str(b) + " es: " + str(div(a,b)))