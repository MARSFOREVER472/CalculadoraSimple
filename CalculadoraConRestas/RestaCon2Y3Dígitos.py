# PASO 1: DEFINIREMOS LAS VARIABLES PARA INTRODUCIR 2 Y 3 NÚMEROS CUALQUIERA, SEGÚN CORRESPONDA.

# PARA RESTAR 2 NÚMEROS CUALQUIERA.

def restar2NumerosCualquiera ():
    global num1, num2
    num1 = int(input("INGRESE UN NÚMERO: "))
    num2 = int(input("INGRESE OTRO NÚMERO: "))

# PARA RESTAR 3 NÚMEROS CUALQUIERA.

def restar3NumerosCualquiera ():
    global num1, num2, num3
    num1 = int(input("INGRESE UN NÚMERO: "))
    num2 = int(input("INGRESE OTRO NÚMERO: "))
    num3 = int(input("INGRESE UN ÚLTIMO NÚMERO: "))

# AL ELEGIR CUALQUIERA DE ESTAS 2 OPCIONES, REALIZAREMOS ESTOS PROCEDIMIENTOS.

# PARA RESTAR 2 NÚMEROS.

def restar2Numeros (a, b):
    print("LA RESTA DE 2 NÚMEROS ",a," - ",b," = ", a - b)

# PARA RESTAR 3 NÚMEROS.

def restar3Numeros (a, b, c):
    print("LA RESTA DE 3 NÚMEROS ",a," - ",b," - ",c," = ", a - b - c)

# CREAREMOS UN MENÚ PRINCIPAL PARA INTERACTUAR CON ESTAS FUNCIONES.

while True:
    print("""
          ************¡¡¡¡¡BIENVENIDO A LA ZONA DE SACRIFICIO!!!!!************
          
          SELECCIONE LA OPERACIÓN A EFECTUAR:
          
          1) RESTAR 2 NÚMEROS
          2) RESTAR 3 NÚMEROS
          3) SALIR DE LA CALCULADORA
          """)
    
    seleccion = int(input())

    if seleccion == 1:
        restar2NumerosCualquiera()
        restar2Numeros(num1, num2)
    
    elif seleccion == 2:
        restar3NumerosCualquiera()
        restar3Numeros(num1, num2, num3)

    elif seleccion == 3:
        print("HASTA PRONTO!!")
        break

# ESO ES LO QUE TENEMOS HASTA EL MOMENTO!!!!!!!!!!!!!!

