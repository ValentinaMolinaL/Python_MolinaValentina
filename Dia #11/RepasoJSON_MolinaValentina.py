#!/usr/bin/python
# -*- coding: utf-8 -*-
import json

def abrirArchivo():
    miJSON=[]
    with open("C:/Users/Usuario/Downloads/info.json", encoding="utf-8")as openfile: 
        miJSON= json.load(openfile)
    return miJSON

def guardarArchivo(miData):
    with open("C:/Users/Usuario/Downloads/info.json","w") as outfile:
        json.dump(miData,outfile)

inicioFin=True     
while inicioFin:  
    print("-------------------------------------------")
    print("-----PLATAFORMA DE GESTION CAMPUSLANDS-----")
    print("-------------------------------------------")
    print("""Hola! Por favor escoge alguna de las opciones:\n
          1.Revisar estudiantes
          2.Modificar estudiante
          3.Crear estudiantes
          4.Eliminar estudiantes\n""")
    opPricipal=int(input("Cual opción escoges:\n"))
    miInfo=[]
    if(opPricipal==1):#---------------REVISAR LISTADO DE ESTUDIANTES-----------------------------
        miInfo=abrirArchivo()
        for i in miInfo:
            for ubicacion in i["estudiantes"]:
                print("---------------------------------------")
                print("ID:",ubicacion["id"])
                print("Nombre:",ubicacion["nombre"])
                print("Apellido:",ubicacion["apellido"])
                print("Edad:",ubicacion["edad"])
                print("Fecha de Nacimiento (DD-MM-AAAA):",ubicacion["fechaNacimiento"])
                print("Cédula:",ubicacion["cedula"])
                print("E-mail:",ubicacion["email"])
                print("GitHub:",ubicacion["github"])
    elif(opPricipal==2):#-------------------MODIFICAR DATOS DE ESTUDIANTES-------------------------
        miInfo=abrirArchivo()
        contador = 0
        for i in miInfo:
            for ubicacion in i["estudiantes"]:
                contador = contador+1
                print("------------------------------------------------------------------")
                print(" ESTUDIANTE #",contador)
                print("ID:",ubicacion ["id"])
                print("Nombre:",ubicacion["nombre"])
                print("Apellido:",ubicacion["apellido"])
                print("Edad:",ubicacion["edad"])
                print("Fecha de Nacimiento (DD-MM-AAAA):",ubicacion["fechaNacimiento"])
                print("Cédula:",ubicacion["cedula"])
                print("E-mail:",ubicacion["email"])
                print("GitHub:",ubicacion["github"])
            contador = 0
        print("\n----Actualizacion de Datos----")
        salon=int(input("""En que salon esta el estudiante?
                        1. Salon T2
                        2. Salon P1\n"""))
        if salon==1 or 2:
            estudiante = int(input("Para hacer cambios por favor digite el ID del estudiante\n"))
            datoCambiar=int(input("""Que dato te gustaría cambiar del estudiante?
                                  1.ID:
                                  2.Nombre:
                                  3.Apellido:
                                  4.Edad:
                                  5.Fecha de Nacimiento:
                                  6.Cedula:
                                  7.E-mail:
                                  8.GitHub:\n"""))
            if (datoCambiar==1):
                nuevoID= input("Ingresa el nuevo ID:")
                miInfo[0]["estudiantes"][estudiante-1]["id"] = nuevoID
                guardarArchivo(miInfo)
                print("Cambio realizado!")
        
            elif (datoCambiar==2):
                nuevoNombre = input("Ingresa el nuevo nombre:")
                miInfo[0]["estudiantes"][estudiante-1]["nombre"] = nuevoNombre
                guardarArchivo(miInfo)
                print("Cambio realizado!")
        
            elif (datoCambiar==3):
                nuevoApellido = input("Ingresa el nuevo apellido:")
                miInfo[0]["estudiantes"][estudiante-1]["apellido"] = nuevoApellido
                guardarArchivo(miInfo)
                print("Cambio realizado!")

            elif (datoCambiar==4):
                nuevaEdad = input("Ingresa la nueva edad:")
                miInfo[0]["estudiantes"][estudiante-1]["edad"] = nuevaEdad
                guardarArchivo(miInfo)
                print("Cambio realizado!")    

            elif(datoCambiar==5):
                nuevaFNacimiento = input("Ingresa la nueva fecha de nacimiento:")
                miInfo[0]["estudiantes"][estudiante-1]["fechaNacimiento"] = nuevaFNacimiento
                guardarArchivo(miInfo)
                print("Cambio realizado!")

            elif (datoCambiar==6):
                nuevaCedula = input("Ingresa la nueva cedula:")
                miInfo[0]["estudiantes"][estudiante-1]["cedula"] = nuevaCedula
                guardarArchivo(miInfo)
                print("Cambio realizado!")

            elif (datoCambiar==7):
                nuevoEmail= input("Ingresa el nuevo E-mail:")
                miInfo[0]["estudiantes"][estudiante-1]["email"] = nuevoEmail
                guardarArchivo(miInfo)
                print("Cambio realizado!")

            elif (datoCambiar==8):
                nuevoGitHub = input("Ingresa el nuevo GitHub:")
                miInfo[0]["estudiantes"][estudiante-1]["github"] = nuevoGitHub
                guardarArchivo(miInfo)
                print("Cambio realizado!")
                contador = 0
            miInfo=abrirArchivo()
            for i in miInfo[0]["estudiantes"]:
                contador = contador +1
                print("-------------------------------------------------------")
                print(" ESTUDIANTE #",contador)
                print("ID:",i["id"])
                print("Nombre:",i["nombre"])
                print("Apellido:",i["apellido"])
                print("Edad",i["edad"])
                print("Fecha de Nacimiento (DD-MM-AAAA):",i["fechaNacimiento"])
                print("Cédula:",i["cedula"])
                print("E-mail:",i["email"])
                print("GitHub:",i["github"])
                print("--------------------------------------------------------")
                print("")
                contador = 0
    elif(opPricipal==3):#---------------CREACION ESTUDIANTES---------------------------
        miInfo = abrirArchivo()
        print("----Registros de Estudiantes----")
        grupo = int(input("""¿En qué grupo desea ingresar al estudiante? 
                          1. Salon T2
                          2. Salon P1\n"""))
        if 0 <= grupo < len(miInfo):
            datosEstNuevo = {}
            datosEstNuevo["id"] = int(input("ingresa el ID del estudiante:\n"))
            datosEstNuevo["nombre"] = str(input("Ingresa los nombre del estudiante:\n"))
            datosEstNuevo["apellido"] = str(input("Ingresa los apellido del estudiante:\n "))        
            datosEstNuevo["edad"] = int(input("ingresa la edad del estudiante:\n"))
            datosEstNuevo["fechaNacimiento"] = str(input("Ingresa la fecha de nacimiento del estudiante:\n"))
            datosEstNuevo["cedula"] = int(input("Ingresa el número de cédula del estudiante:\n "))
            datosEstNuevo["email"] = str(input("Ingresa la direccion del correo electrónico del estudiante: \n"))
            datosEstNuevo["github"] = str(input("Ingresa el enlace de github del estudiante: \n"))
            miInfo[grupo]["estudiantes"].append(datosEstNuevo)
            guardarArchivo(miInfo)
    elif (opPricipal==4):#------------------ELIMINACIÓN ESTUDIANTES---------------------------------------
        miInfo = abrirArchivo()
        salon4 = int(input("""En qué salon se encuentra el estudiante que desea eliminar 
                           0. Salon T2 
                           1. Salon P1\n"""))
        if 0 <= salon4 < len(miInfo):
            eliminar=int(input("Ingresa el ID de estudiante que deseas eliminar: "))
            for estudiante in miInfo[salon4]["estudiantes"]:
                if estudiante["id"] == eliminar:
                    miInfo[salon4]["estudiantes"].remove(estudiante)
                    guardarArchivo(miInfo)
                    print("El estudiante ha sido eliminado exitosamente")
                    break
                else:
                    print("Ingresaste el ID mal o el estudiante no existe")
                    break
    elif (opPricipal==5):
        print("Haz salido del sistema")
        inicioFin=False

    