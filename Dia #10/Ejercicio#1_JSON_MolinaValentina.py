#--------------------------------------------------
#-----------------PYTHON - JSON--------------------
#--------------------------------------------------
import json # se llama a la biblioteca JSON con import
documentoIn="C:/Users/Usuario/Downloads/large-file.json" # se llamo al DOCUMENTO JSON
with open(documentoIn, encoding="utf-8")as file: 
    documento=json.load(file)
lista1=[] # lista donde de guardara el nombre de los eventos
contadorLista=[0,0,0,0,0,0,0,0,0,0,0,0,0,0]# lista donde se guardara la cantidad de cada  evento
for i in documento: #contara los eventos por todo el documento json
    lista1.append(i["type"]) #se agregara a lista1 el evento en la posicion (i)
    if i["type"]=="MemberEvent": 
        contadorLista[0]+=1 #cada que encuentre un evento igual sumara 1 evento en la pisicion(0)
    elif i["type"]=="IssuesEvent": 
        contadorLista[1]+=1
    elif i["type"]=="PushEvent": 
        contadorLista[2]+=1
    elif i["type"]=="ReleaseEvent": 
        contadorLista[3]+=1
    elif i["type"]=="CommitCommentEvent":
        contadorLista[4]+=1 
    elif i["type"]=="DeleteEvent": 
        contadorLista[5]+=1
    elif i["type"]=="PullRequestEvent":
        contadorLista[6]+=1 
    elif i["type"]=="CreateEvent":
        contadorLista[7]+=1 
    elif i["type"]=="IssueCommentEvent": 
        contadorLista[8]+=1
    elif i["type"]=="GollumEvent": 
        contadorLista[9]+=1
    elif i["type"] =="PublicEvent":
        contadorLista[10]+=1
    elif i["type"]=="WatchEvent":
        contadorLista[11]+=1
    elif i["type"]=="ForkEvent":
        contadorLista[12]+=1
    elif i["type"]=="PullRequestReviewCommentEvent":
        contadorLista[13]+=1

lista2=list(set(lista1)) #(Lista2) sera una (lista) que ira (eliminando) los eventos repetidos de (lista1)
inicioFin=True
while inicioFin:

    print("""
    ----Menu de opciones----
        1.crear
        2.actualizar
        3.eliminar
        4.revisar
    """) # menu de opciones

    opcion=int(input("eliga opcion")) 
    #----------------CREAR-------------------------------------------------------------------------
    if opcion==1:
        nuevoEvento=input("nombre del nuevo evento")
        if nuevoEvento in lista2:  
            print("ESTE EVENTO YA EXITE")
        else:
            lista2.append(nuevoEvento) # si el evento ingresado no existe se guardara en lista2(eventos ya registrados)
            cantNueEven=int(input("cantidad de evento")) 
            contadorLista.append(cantNueEven) # y se le guarda la cantidad
            print("EVENTO REGISTRADO")

    #------------------ACTUALIZAR-------------------------------------------------------------------
    if opcion==2:
        actualEvent=input("nombre de evento a actualizar")
        if actualEvent in lista2: # si el evento ingresado existe 
            actualCant=int(input("cantidad a actualizar "))
            for i in range(0,len(contadorLista)): # i contara desde o hasta la contidad de contadorlista
                if actualEvent== lista2[i]: # si el evento ingresado es igual al evento en la posicion [i] 
                    contadorLista[i]+=actualCant # se le sumara a la cantidad del evento en posicion[i] la cantidad ingresada por el cliente
                    print("CANTIDAD ACTUALIZADA")
        else:
            print("EL EVENTO NO ESTA REGISTRADO")
    
    #-----------------ELIMINAR-----------------------------------------------------------------------
    if opcion==3:
        Ubicacion=0
        elimiEvent=input("nombre del evento a eliminar")
        while elimiEvent in lista2: # mientras que el evento que se quiere eliminar esta entre la lista de eventos registrada
            if elimiEvent in lista2[Ubicacion]:  # y si el evento a eliminar es igual a lista2 en la posicion[i]
                lista2.remove(elimiEvent) # se elimina el nombre del evento
                contadorLista.pop(Ubicacion) # y se elimina la cantidad del evento
                print("EVENTO ELIMINADO")
            else:
                Ubicacion+=1

    #------------------REVISAR-----------------------------------------------------------------------
    if opcion==4:
        for i in range(0,len(lista2)): # i contara desde 0 hasta la cantidad de lista2
            print("nombre:",lista2[i],"cantidad:",contadorLista[i]) # se imprimira el nombre y la cantidad de i es decir de la ubicacion
# Desarrollado por Valentina Molina CC 1007109135