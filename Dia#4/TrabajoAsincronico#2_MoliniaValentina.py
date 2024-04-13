#-------------------------------------------
#------------TRABAJO ASINCRONICO------------
#-------------------------------------------
final=True
while final:
    #creacion de arreglo (en este caso el valor de las nomedas).
    #NOTA: en este caso es necesario poner los valor de los arreglo de mayor a menor - en este 
    #caso de no pponerlo asi ser asi contara del de el 1 hasta el 10.
    monedasD=[10,5,1]
    #creamos la variable que almacenara el valor del ciente y el tipo del mismo sera int(entero)
    r=int(input("Ingrese la cantidad de dinero: "))

    #Bucle (for) para que cuente desde a(0) hasta monedas (hasta que cuente los arreglos)
    for i in monedasD:
        #Bucle (if) si r es mayor o igual a i se hara (linea 15)
        if r >= i:
             # total sera igual al resultado de //(divicion entera) 
            total = r // i 
            r = r % i
            #Damos a conocerel resultado del cambio
            totalM=total+1
            print ("la cantidad de monedas de su cambio es:", totalM -1)
            print("Ahora tienes ", str(total), " monedas de ", str(i))
      
    salida=input("Presione 1 para salir del programa, de lo contrario el programa se repetira")
    if salida == 1:
        print("Saliendo del programa")
        Enter=input("")
        final=False