num=input("")
array=list(sorted(set(map(int, num.split(",")))))#Guarda en la lista
Contador=0 
NumeroUbicar=int(input("")) 
array.append(NumeroUbicar) 
array.sort() 
lisn=list(set(array))
for a in lisn: 
    Contador+=1 
    if NumeroUbicar ==a: 
        print(Contador-1)
        break