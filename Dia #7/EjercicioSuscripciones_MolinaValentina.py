#---------------------------------
#---------Suscripciones-----------
#---------------------------------
name=[] #lista deonde se guardara el nombre del usuario
password=[] # lista donde se gardara la contraseña del usuario
obsequio=[]
cuentaCliente=0 #variable donde se guarara el dinero del usuario
suscripcion=10000 #valor de la suscripcion

inicio_fin=True
while inicio_fin==True:

    print("""\n-----BIENVENIDO AL MENU PRINCIPAL-----
        1. Crear cuenta
        2. Iniciar sesion
        3. Recargar dinero a tu cuenta
        4. Compra de suscripcion
        5. Obsequiar suscripcion 
        0. Cerrar sesion""")  # se le da la bienvenida y se le muestra el menu de opciones

    opcion=int(input("        Elige una opcion\n"))# variable donde se guardara la opcion del usuario

    #------------opcion 1--------------
    if opcion==1: # si el usuario elige 1 se ejecutara la creacion de la cuenta
        print("----Crea tu cuenta----")
        user=(input("\nIngresa tu usuario\n")) # ingreso del usuario
        name.append(user) # el valor de la variable (user) se guardar en la lista (name) con la ayuda de (append)
        contra=(input("Ingresa tu contraseña\n"))#ingreso de la contraseña del usuario
        password.append(contra)# el valor de la variable (contra) se guardar en la lista (password) con la ayuda de (append)
        print("-USUARIO REGISTRADO CON EXITO")#se le hara saber al usuario que su usuario fue registrado con exito

    #------------opcion 2--------------
    elif opcion==2: # si el usuario elige 2 se ejecutara el inicio de sesion
        print("----Inicio de seccion----")
        nombre=(input("\ningresa tu usuario\n"))# ingreso del usuario anteriosmente registrado
        if nombre in name: #con la ayuda del condicional if se revisara si el nombre recien ingresado en la variable(nombre) esta en la lista(name) de usuarios registrados
            contraseña=(input("ingresa la contraseña\n"))# ingreso de la contraseña del usuario anteriosmente registrado
            if contraseña in password:#con la ayuda del condicional if se revisara si la contrtaseña recien ingresada en la variable(contraseña) esta en la lista(password) de contraseñas registradas
                print("HAZ INICIADO SESION CORRECTAMENTE") # si las anteriores condicionales se cumplen se le imformara al cliente que inicio sesion correctamente
            else: # si if no encuentra el valor de (contraseñas) en (password) se le imformara al cliente que la contraseña es incorrecta
                print("CONTRASEÑA INCORRECTA")
        else:# si if no encuentra el valor de (nombre) en (name) se le imformara al cliente que el usuario es incorrecto o no se encuentra registrado 
            print("USUARIO INCORRECTO O EL USUARIO NO HA SIDO REGISTRADO")

    #------------opcion 3--------------
    elif opcion==3:# si el usuario elige 3 se ejecutara la recargar de dinero a su cuenta
        print("\n-Para recargar tu cuenta")
        ingreso=int(input("Ingresa la cantidad de dinero que deseas recargar\n"))#se crea la variable (ingreso) que es el dinero que el usuario ingrese
        cuentaCliente += ingreso # se valor de la variable ingreso se sumara y se guardara en la lista cuentaCliente
        print("Usuario el saldo de tu cuenta es de:",cuentaCliente) #se da a mostrar el total

    #------------opcion 4--------------
    elif opcion==4:# si el usuario elige 4 se ejecutara la Compra de suscripcion
        print("\n----Compra de suscripcion----") 
        print("\nDeseas hacer la compra de suscripcion?") 
        print("Recuerda que cada suscripcion tiene el valos de ",suscripcion,"y dura un año ")# se le imforma al cliente el valor y la duracion de la suscripcion
        VerifC=int(input("\n1.si \n2.no\n"))#variable para la siguiente condicional
        if VerifC == 1:#condicional if para verificar si desea hacer la compra
            compra_sus=int(input("\nCuantas suscripcion deseas adquirir?\n"))#solictar la cantidad de compra 
            if suscripcion*compra_sus<=cuentaCliente:# si el precio*cantidad de compra es menor o igual a el dinero que tiene el cliente se hara
                elige_Años=int(input("\nDesde que año deseas activar la suscripcion?\n")) # variable para condicionar el año 
                if elige_Años > 2024:
                    compraFinal=compra_sus+elige_Años#variable para guardar la suma del año de inicio + camtidad de  compra para saber el año final
                    cuentaCliente-=compra_sus*suscripcion# se multiplicara el precio*cantidad de compra y se restaran de la cuenta del usuario para asi saber cuanto le queda
                    print("Tu suscripcion inicia en el año", elige_Años+1 ,"finalizara en el año", compraFinal )# se muestra el año el inicio y final de la suscripcion
                    print("el saldo actual de tu cuneta es: ",cuentaCliente)# se muestra el saldo total
            else:# si precio*cantidad de compra es mayor al dinero del usuario (la compra no sera posible)
                print("Oh!! No tienes saldo suficiente para la compra \nTe recordamos que el valor de la suscripcion es de ",suscripcion,)
    #------------opcion 5--------------
    elif opcion==5:# si el usuario elige 5 se ejecutara la compra de obsequio
        print("\nDeseas obsequiar una suscripción? ")
        print("Recuerda que cada suscripcion tiene el valos de ",suscripcion,"y dura un año ")# se le imforma al cliente el valor y la duracion de la suscripcion
        veriReg=int(input("\n1.si \n2.no\n"))#variable para la siguiente condicional
        if veriReg== 1:
            compra_sus=int(input("\ncuantas suscripciones deseas obsequiar\n"))#solictar la cantidad de compra
            if suscripcion*compra_sus <= cuentaCliente:
                usuario2=input("\ningrese el nombre de la persona a la que le obsequiara la suscripcion\n")# ingreso del usuario2
                obsequio.append(usuario2)# se guardara en la lista obsequio el valor de usuario2 con la ayuda de append
                cuentaCliente-=suscripcion*compra_sus # # se multiplicara el precio*cantidad de compra y se restaran de la cuenta del usuario para asi saber cuanto le queda
                print("\nHaz obsequiado",compra_sus,"suscripciones a ",usuario2) #se mostrara que la compra fue exitosa
                print("El saldo actual de tu cuenta es:",cuentaCliente) #estado actual de la cuenta
            else:# si precio*cantidad de compra es mayor al dinero del usuario (la compra no sera posible)
                print("No cuentas con el saldo suficiente para hacer la compra del obsequio \nPor favor recarga.")
    #------------opcion 5--------------
    elif opcion==0:# si el usuario elige 5 se ejecutara la finalizacion del programa
        print("Gracias por utilizar nuestro programa")
        inicio_fin=False
# Esta siendo desarrollado por Valentina Molina CC.1007109135