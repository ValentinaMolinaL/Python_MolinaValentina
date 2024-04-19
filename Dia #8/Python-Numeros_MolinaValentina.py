#----------------------
#----PITHON-NUMEROS----
#----------------------
name=[]
price=[]
canti=[]
cantSurt=int(input("cuantos productos deseas surtir"))
contador=0
for prod in range(0,cantSurt):
    nombre=str(input("ingresa el nombre del producto que vas ha ingresar\n"))
    name.append(nombre)
    precio=int(input("\ningresa el precio del producto que vas a ingresar \n"))
    price.append(precio)
    unidades=int(input("\ningresa las unidades que vas a ingresar\n"))
    canti.append(unidades)
for prod in range(0,cantSurt):
    print("\nNombre:",name)
    print("Precio:",price)
    print("Unidades",canti)
#Desarrollado por Valentina Molina CC.1007109135