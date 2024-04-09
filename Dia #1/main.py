#--------------------------------
#---- DIA 1 CHEAT SHEET PYTHON ------
#--------------------------------

#Imprimir hola mundo
print("Hola mundoooooooooooooo!!!")

#Datos primitivos

#Numero
numerito = 1 #nombreVariable = valor
print(numerito) #imprimir(variable)
print(type(numerito)) #imprimir(tipo(variable))

#Decimal
numeritoDecimal = 1.1
print(numeritoDecimal)
print(type(numeritoDecimal))

#Booleano
miBooleanito = True
print(miBooleanito)
print(type(miBooleanito))

#Cadena de texto
texto = "MI TIBU"
print(texto)
print(type(texto))

#Ingresa por teclado la infomarcion

edad = int(input("por favor ingresar tu edad"))
print(edad)

#Conversion de tipos de variable
print(int(12.3))
print(float(20))
print(bool(False))
print(bool(True))
print(str("Valentina"))

#Bucle For 
for a in range(1,11):
  print(a)
#Bucle While
a = 1
while a < 11:
  print(a)
  a += 1
#Funciones (4 Tipos)
#Primera Funcion 
def my_function():
  print("Hola mundo")

my_function()
#Segunda Funcion
def my_function(**nom):
  print("Tu primer nombre es: " + nom ["nombre"])

my_function(nombre = "Valentina")
#Tercer funcion
def my_function(a):
  print(" compañeros/as "+a)

my_function("Jerson")
my_function("Zully")
my_function("Guadalupe")
my_function("Brayan")
#Cuarta funcion
def my_function(*hermanos):
  print("Entre mis hermanas/os yo soy la " + hermanos[1])

my_function("Mayor", "del Medio", "Menor")
#Desarrollado por Valentina Molina