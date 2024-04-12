t=True
boole=True
import string 
import secrets
while t== True:
    print("""--------Menu de Opciones--------
          1.Si quiere consultar si un numero es primo
          2.Si quieres obtener información adicional
          3.Si deseas generar una contraseña segura
          0.Si deseas salir del programa""")
    h=int(input("Por favor elige una de las opciones"))
    if h==1:
        r=True
        while r ==True:
            a=int(input("Por favor ingresa el numero"))
            contador = 0 
            for i in range (1,a+1):#PREGUNTARLE AL PROFE PEDRO 
                if a % i == 0:
                    contador = contador + 1

            if contador == 2:
                print(a,"es un numero primo")
            else:
                print(a,"no es un numero primo")

            p=int(input("0.Si deseas salir del programa"))
            if p==0:
                print("Volver al menu principal")
                r==False

    if h==2:
        print("""¿Qué son los números primos?
        Los números primos son aquellos que solo son 
        divisibles entre ellos mismos y el 1, es decir, 
        que si intentamos dividirlos por cualquier otro             
        número, el resultado no es entero. Dicho de otra 
        forma, si haces la división por cualquier número 
        que no sea 1 o él mismo, se obtiene un resto distinto de cero.""")
        n=input("\nPresiona Enter para continuar")

    if h==3:
        k=True
        while k==True:
            mayuscula=string.ascii_uppercase
            minusculas=string.ascii_lowercase
            numeros=string.digits
            simbolos=string.punctuation
            almacenamiento=mayuscula+minusculas+numeros+simbolos

            longitud=int(input("Cuantos caracteres deseas que lleve tu contraseña"))
            j=""
            for i in range (1,longitud+1):
                j+="".join(secrets.choice(almacenamiento))#El += se hace la funcion de sumar el valor de j + el proceso de la fila 75/ join es para pegar los valores de cadena en una misma fila
                if i == longitud:
                    print(j)
                    u=input("0.Si deseas salir del programa")
                if u==0:
                    k==False
    if t==0:
        t==False