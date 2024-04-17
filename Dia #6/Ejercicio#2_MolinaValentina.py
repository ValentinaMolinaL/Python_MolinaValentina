sumandos=[1,2,3,4,5] # OLVIDE POR COMPLETO TENER EN CUENTA LA LISTA PARA LA OPERACION 
 #1+2=3 - 1+3=4 - 1+4=5 - 1+5=6 / 2+3=5 - 2+4=6 - 2+5=7 / 3+4=7 - 3+5=8 / 4+5=9
  #Posibles sumas 3-4-5-6-7-8-9
limite=True
while limite==True:
    suma=int(input())
    if suma>1 and suma<=9:
        limite=False

    sumando1=int=suma//3
    sumando2=suma-sumando1
    print(sumando1,sumando2)