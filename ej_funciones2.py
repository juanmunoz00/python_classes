import random

def GeneraNumeroAleatorio(int_o_float, limite_inf, limite_sup):
  if( int_o_float == "int" ):
    numero_aleatorio = random.randint(limite_inf, limite_sup)
  if( int_o_float == "float" ):
    numero_aleatorio = random.uniform(limite_inf, limite_sup)
  
  return numero_aleatorio

def PrintLista(nombre_lista, lista):
  print(nombre_lista)
  print(lista)

lista_de_numeros_int = []
lista_de_numeros_float = []

for i in range(9):
  num_int = GeneraNumeroAleatorio("int", 10, 100)
  num_float = GeneraNumeroAleatorio("float", 10.1, 99.9)
  lista_de_numeros_int.append(num_int)
  lista_de_numeros_float.append(num_float)

PrintLista("Int", lista_de_numeros_int)
PrintLista("Float", lista_de_numeros_float)
