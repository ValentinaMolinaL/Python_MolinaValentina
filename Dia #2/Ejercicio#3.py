#El programa selecciona aleatoriamente un número secreto entre 1 y 100., donde el 
#usuario tiene un total de 10 intentos para adivinar el número secreto. Después de 
#cada intento, el programa dará pistas indicando si el número secreto es mayor o menor
# que la suposición actual del usuario. Si el usuario adivina correctamente, el programa 
#felicitará al jugador y mostrará en cuántos intentos lo logró.
#El programa debe ser amigable y explicar claramente las instrucciones al usuario.

#----------------------------
#-----OPERADORES LÓGICOS-----
#----------------------------

#import (llamador de librerias) randon (libreria aleatorio)
import random

#variable que teendra el numero al aleatorio/se llama a la libreria/se pone la funcion de la 
#libreria/ y el rango en el que se creara el numero aleatorio
Azar=random.randint(1,100)
#Bucle for con la variable que en este caso llevara el conteo de los intentos con la ayuda de rango 
for i in range (1,11):

    print("""
        -----Hola Bienvenido a AzarPlay-----
            
    El dia de hoy te invitamos a jugar nuentro mejor 
    juego de suerte ya que sabemos que la tienes
            
    Tendras 10 vidas para atinarle al numero ganador 
    y tendras algunas pistas.
            
    No siendo mas, Aprovecha tu suerte""")
    # nuevamente se ponen condicionales if para comparar el numero secreto y el numero ingresado por el jugador 
    # y segun el numero ingresado dar a conocer si es ganador o debe seguir intentandolo
    numero=int(input("Por favor ingresa tu primer numero de la suerte"))
    if numero!=Azar:
        print("Mmmm lo sentimos tal vez el proximo sera el ganador")
        if numero<Azar:
            print("Tu numero ganador esta mas arriba")
        if numero>Azar:
            print("Tu numero ganador esta mas abajo")
    else:
        print("""¡¡¡¡Wauuuu HAS GANADO!!!!
              Con el intento #""",i)
        break
# Desarrollado por Valentina Molina CC 1007109135
