while True:
    monedaD=[10,5,1]

    valorM=int(input("""Hola bienvenido
                  Por favor ingresa el valor del 
                  dinero que deseas cambiar"""))
    #Agregarle la eleccion de que tipos de monedas quiere
    cantidadM=int(input("""\nPor favor ingresa la cantidad de monedas 
                        en la que deseas hacer el cambio
                        Estos don los valores de las monedas 
                        con las que te haremos el cambio
                        $1 $5 $10              """))
    #Darle a conocer al cliente el valor y la cantidad de las monedas
    multi= valorM // cantidadM
    valorM = valorM % multi
    if multi == valorM:
        print (valorM,"no se puede cambiar en",cantidadM)
    else:
        print("Asi ha quedado tu cambio")
    print("tienes",multi)