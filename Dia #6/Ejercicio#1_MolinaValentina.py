cantidad=[] # array que almacenara la lista 
hola=True #definimos que la variable (hola) sera true
while hola==True: #Bucle while hola sera igual a true hara 
    t = int(input("")) # ingreso del valor de la variable t que sera la longitud de la lista
    if t<=300 and t>0: #condicional if para que el rango de cantidad no sea mas bajo que 0 y tampoco mas alto que 300
        hola=False #dependiendo de si la condicion se cumple o no (hola) sera false
#se separa o saca for de while para que solo se repita el ingreso de la cantidad y no la lista 
for a in range(0,t): #bucle for que cuente a desde el rango 0 hasta el rango t
    cantidad.append(input("")) #append para juntar los numeros de la nueva lista 
    cant=list(set(cantidad)) #list para acomodar los numeros en forma de fila y set para eliminar los numeros repetidos
    cant.sort()# sort para ordenar el resultado de la lista de forma ascendente 
print(cant) 
# Desarrollado por Valentina Molina CC.1.007.109.135