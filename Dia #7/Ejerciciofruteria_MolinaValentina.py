#------------------
#-----fruteria-----
#------------------
Fruits=[("Melon",0.45,6),("Fresa",4.55,5),("ochuva",5,2)]

booleanito = True
while booleanito == True:

    print("""\n---Bienvenidos a fruti---
        ----------menu----------
    1). Ver las frutas que estan disponibles
    2). Ver las frutas que tienen un precio menor a 0.50
    3). Ver la fruta con más cantidad disponible
    4). Ver el precio de todas las frutas que hay disponibles
    0). Cerrar la tienda""")

    opcion=int(input("    ingrese una opcion\n")) #para elegir opcion

    if opcion==1: 
            print("\nFrutas disponibles")
            for i in Fruits:print(i[0])

    if opcion==2:
            print("\nFrutas con precios mas bajos que 0.50") 
            for i in Fruits: 
                if i[1] <= 0.50:
                    print(i)
    if opcion== 3:
            print("\nEsta es la fruta mas disponible")
            FrutaMayor=max(Fruits, key=lambda x: x[2]); print(FrutaMayor)

    if opcion== 4:
            print("\nPrecio de todas las frutas que hay disponibles es") 
            for i in Fruits:
                Precio=i[1]*i[2]
            print(Precio)

    if opcion==0:
            print("\nGracias por tu compra")
            inicio_fin=False #fin del programa
# Desarrollado por Valentina Molina CC.1007109135