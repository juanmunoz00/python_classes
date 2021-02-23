print("1 = suma")
print("2 = resta")
print("3 = mult")
print("4 = div")
print("") ##Espacio en blanco
opcion = input("Seleccionar operacion: ")

if( type(opcion % 2) == int ):
    opcion = int(opcion)
    print("opcion: ", str(opcion))
    
    if( opcion <= 0 ): 
        print("lte 0")
        print(opcion, " no es una opcion no valida")
    elif( opcion > 4 ): 
        print("gte 4")
        print(opcion, " no es una opcion no valida")
    else:
        x = input("x? ")
        y = input("y? ")

        continuar = 1##Bandera

        if( type(x % 2) == int ): print(x, "es numero entero")
        elif( type(x % 2) == float ): print(x, "es numero decimal punto flotante")
        else: 
            print(x, " no es numero")
            continuar = 0

        if( type(y % 2) == int ): print(y, "es numero entero")
        elif( type(y % 2) == float ): print(y, "es numero decimal punto flotante")
        else: 
            print(y, " no es numero")
            continuar = 0

        ##if( continuar == 1 )


