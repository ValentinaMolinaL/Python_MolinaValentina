#---------------------------------
#---PYTHON - OPERADORES LÓGICOS---
#---------------------------------

#1.El programa dará la bienvenida y explicará la naturaleza de la Secuencia de Fibonacci

while True: 
    print("""Hola Bienvenido a nuesto programa 
      A continuacion te explicaremos la secuencia Fibonacci
      esta es una suma de los dos numeros anteriores comenzando por 0 y siento todos numeros naturaales""")

    # solicitará al usuario ingresar un valor entero "n", representando hasta qué término de la secuencia se generará

    n=int(input("Ingresa la cantidad de numeros que deseas generar"))

    x = 1
    a = 0
    b = 1

    while x <= n:
        if x%2 == 1:
           print(a)
           a = a + b
        else:
           print(b)			
           b = b + a	
        x = x + 1
        # Luego, preguntará si el usuario desea continuar o salir, donde si se decide salir, 
        # el programa se detendrá; de lo contrario, se repetirá el proceso.


    caso=int(input("""Presiona 1 si quieres continuar en el programa
      Presiona 2 si quieres salir del programa"""))
    if caso==1:
     print("                                      ")
    elif caso==2:
           break
    


# Desarrollado por Valentina Molina CC 1007109135

