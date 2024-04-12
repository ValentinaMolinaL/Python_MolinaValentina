#-------------------------------------------
#------------TRABAJO ASINCRONICO------------
#-------------------------------------------

#recacion de arreglo (en este caso el valor de las nomedas)
monedasD=[10,5,1]
r=int(input("Ingrese la cantidad de dinero: "))
#Bucle (for) para que cuente desde a(0) hasta monedas (hasta que cuente los arreglos)
for i in monedasD:
    if r >= i:
        total = r // i
        print("Tu cambio es este:"
              "Tienes ", str(total), " monedas de ", str(i))
        r = r % i