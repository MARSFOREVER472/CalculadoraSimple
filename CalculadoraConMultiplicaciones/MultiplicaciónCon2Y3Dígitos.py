# PASO 1: DEFINIREMOS LAS VARIABLES PARA INTRODUCIR 2 Y 3 NÚMEROS CUALQUIERA, SEGÚN CORRESPONDA.

# 1.- PARA MULTIPLICAR 2 NÚMEROS CUALQUIERA:

def multiplicar2NumerosCualquiera ():
    global numero1, numero2
    numero1 = int(input("INGRESE UN NÚMERO: "))
    numero2 = int(input("INGRESE OTRO NÚMERO: "))

# 2.- PARA MULTIPLICAR 3 NÚMEROS CUALQUIERA:

def multiplicar3NumerosCualquiera ():
    global numero1, numero2, numero3
    numero1 = int(input("INGRESE UN NÚMERO: "))
    numero2 = int(input("INGRESE OTRO NÚMERO: "))
    numero3 = int(input("INGRESE UN ÚLTIMO NÚMERO: "))

# AL ELEGIR CUALQUIERA DE ESTAS 2 OPCIONES, REALIZAREMOS ESTOS SIGUIENTES PROCEDIMIENTOS:

# 1.1.- PARA MULTIPLICAR 2 NÚMEROS:

def multiplicar2Numeros (a, b):
    print("LA MULTIPLICACIÓN DE 2 NÚMEROS ",a," * ",b," = ", a * b)

# 1.2.- PARA MULTIPLICAR 3 NÚMEROS:

def multiplicar3Numeros (a, b, c):
    print("LA MULTIPLICACIÓN DE 3 NÚMEROS ",a," * ",b," * ",c," = ", a * b * c)

# CREAREMOS UN MENÚ PRINCIPAL PARA PODER INTERACTUAR CON ESTAS OPCIONES:

while True:
    print("""
          ************¡¡¡¡¡BIENVENIDO A LA ZONA DE SACRIFICIO!!!!!************
          
          SELECCIONE LA OPERACIÓN A EFECTUAR:
          
          1) MULTIPLICAR 2 NÚMEROS
          2) MULTIPLICAR 3 NÚMEROS
          3) SALIR DE LA CALCULADORA
          """)
    
    seleccion = int(input())

    if seleccion == 1:
        multiplicar2NumerosCualquiera()
        multiplicar2Numeros(numero1, numero2)
    
    elif seleccion == 2:
        multiplicar3NumerosCualquiera()
        multiplicar3Numeros(numero1, numero2, numero3)

    elif seleccion == 3:
        print("HASTA PRONTO!!")
        break