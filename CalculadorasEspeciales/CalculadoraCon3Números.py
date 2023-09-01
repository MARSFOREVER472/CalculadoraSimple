# ESTO ES UNA CALCULADORA QUE CONTIENE 3 NÚMEROS GLOBALES.
def ingresarTresNumeros ():
    global n1, n2, n3 # VARIABLES NUMÉRICAS A DECLARAR
    n1 = int(input("INGRESE UN VALOR 1: "))
    n2 = int(input("INGRESE UN VALOR 2: "))
    n3 = int(input("INGRESE UN VALOR 3: "))

def sumaTresNumeros (a, b, c): # SUMA DE TRES NÚMEROS CONSECUTIVOS CUALQUIERA.
    print("LA SUMA DE TRES NÚMEROS CONSECUTIVOS ",a," + ",b," + ",c," = ",a+b+c)

def restaTresNumeros (a, b, c): # RESTA DE TRES NÚMEROS CONSECUTIVOS CUALQUIERA.
    print("LA RESTA DE TRES NÚMEROS CONSECUTIVOS ",a," - ",b," - ",c, " = ",a-b-c)

def multiplicacionTresNumeros (a, b, c): # MULTIPLICACIÓN DE TRES NÚMEROS CONSECUTIVOS CUALQUIERA.
    print("LA MULTIPLICACIÓN DE TRES NÚMEROS CONSECUTIVOS ",a," * ",b," * ",c," = ",a*b*c)

def divisionTresNumeros (a, b, c): # DIVISIÓN DE TRES NÚMEROS CONSECUTIVOS CUALQUIERA.
    print("LA DIVISIÓN DE TRES NÚMEROS CONSECUTIVOS ",a," / ",b," / ",c," / ",a/b/c)

# MENÚ PRINCIPAL DE LA CALCULADORA ESPECIAL:

while True:
    print("""
    SELECCIONE UNA OPERACIÓN A REALIZAR:
    
    1) SUMAR 3 NÚMEROS
    2) RESTAR 3 NÚMEROS
    3) MULTIPLICAR 3 NÚMEROS
    4) DIVIDIR 3 NÚMEROS
    5) SALIR DE LA CALCULADORA
    
    """)

    seleccionar = int(input()) # VARIABLE PARA SELECCIONAR ENTRE CADA UNA DE ESTAS 5 OPCIONES.

    if seleccionar == 1:
        ingresarTresNumeros()
        sumaTresNumeros(n1, n2, n3)
    elif seleccionar == 2:
        ingresarTresNumeros()
        restaTresNumeros(n1, n2, n3)
    elif seleccionar == 3:
        ingresarTresNumeros()
        multiplicacionTresNumeros(n1, n2, n3)
    elif seleccionar == 4:
        ingresarTresNumeros()
        divisionTresNumeros(n1, n2, n3)
    elif seleccionar == 5:
        print(str('HASTA PRONTO :('))
        break
