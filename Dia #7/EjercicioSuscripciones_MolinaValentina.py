name=[] #lista deonde se guardara el nombre del usuario

password=[] # lista donde se gardara la contraseña del usuario

cuentaCliente=0 #variable donde se guarara el dinero del usuario

suscripcion=10000 #valor de la suscripcion

print("""BIENVENIDO AL MENU PRINCIPAL
      1. Crear cuenta
      2. Iniciar sesion
      3. Recargar dinero a tu cuenta
      4. Compra de suscripcion
      5. Cerrar sesion""")  # se le da la bienvenida y se le muestra el menu de opciones

opcion=int(input("Elige una opcion"))# variable donde se guardara la opcion del usuario

if opcion==1: # si el usuario elige 1 se ejecutara la creacion de la cuenta
    user=print("ingresa tu usuario") # ingreso del usuario
    name.append(user) # el valor de la variable (user) se guardar en la lista (name) con la ayuda de (append)
    contra=print("ingresa tu contraseña")#ingreso de la contraseña del usuario
    password.append(contra)# el valor de la variable (contra) se guardar en la lista (password) con la ayuda de (append)
    print("usuario registrado con exito")#se le hara saber al usuario que su usuario fue registrado con exito

elif opcion==2: # si el usuario elige 2 se ejecutara el inicio de sesion
    nombre=print("ingresa tu usuario")# ingreso del usuario anteriosmente registrado
    if nombre in name: #con la ayuda del condicional if se revisara si el nombre recien ingresado en la variable(nombre) esta en la lista(name) de usuarios registrados
        contraseña=print("ingresa la contraseña")# ingreso de la contraseña del usuario anteriosmente registrado
        if contraseña in password:#con la ayuda del condicional if se revisara si la contrtaseña recien ingresada en la variable(contraseña) esta en la lista(password) de contraseñas registradas
            print("Haz iniciado seccion correctamente") # si las anteriores condicionales se cumplen se le imformara al cliente que inicio sesion correctamente
        else: # si if no encuentra el valor de (contraseñas) en (password) se le imformara al cliente que la contraseña es incorrecta
            print("Contraseña incorrecta")
    else:# si if no encuentra el valor de (nombre) en (name) se le imformara al cliente que el usuario es incorrecto o no se encuentra registrado 
        print("Usuario es incorrecto o no se encuentra registrado")

elif opcion==3:
    ingreso=int(input("ingresa la cantidad de dinero que deseas ingresar"))
    ingreso += cuentaCliente
    print(ingreso)

elif opcion==4:
    VerifC=print("Deseas hacer la compra de suscripcion \nsi \nno ")
    if VerifC == "si":
        compra_sus=int(input("cuantos años de suscripcion deseas adquirir"))
        suscripcion*compra_sus<=cuentaCliente 
        elige_Años=int(input("Desde que años deseas "))
# Esta siendo desarrollado por Valentina Molina CC.1007109135

