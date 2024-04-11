#Este programa simula un juego interactivo en el que el usuario debe adivinar un número secreto
#elegido aleatoriamente por el programa. El número secreto está en el rango de 1 a 100. Después 
#de cada intento del usuario, el programa proporciona pistas indicando si el número secreto es 
#mayor o menor que la suposición actual. El objetivo es adivinar el número secreto en la menor 
#cantidad de intentos posible.

#----------------------------
#-----OPERADORES LÓGICOS-----
#----------------------------

#import (llamador de librerias) randon (libreria aleatorio)
import random
#variable que teendra el numero al aleatorio/se llama a la libreria/se pone la funcion de la 
#libreria/ y el rango en el que se creara el numero aleatorio
Azar=random.randint(1,100)

#bucle while y True para que el ciclo se repita si este es verdadero 
while True:

# Aca se pondran condicionales if para comparar el numero secreto y el numero ingresado por el jugador 
#y segun el numero ingresado dar a conocer si es ganador o debe seguir intentandolo
    numero=int(input("ingrese el numero"))
    if numero!=Azar:
        print("sigue intentado")
        if numero<Azar:
            print("Tu numero ganador esta mas arriba") 
        if numero>Azar:
            print("Tu nuemro ganador esta mas abajo")
    else:
        print("ganaste")
        break # para finalizar el programa 

#Desarrollado por Valentina Molina CC. 1007109135