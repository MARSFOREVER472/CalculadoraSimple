def ingresarNumeros ():
    global num1, num2 # VARIABLES NUMÉRICAS A DECLARAR
    num1 = int(input("INGRESE UN NÚMERO: "))
    num2 = int(input("INGRESE UN NÚMERO: "))

def suma (a, b):
    print("LA SUMA DE ",a," + ",b," = ",a+b)

def resta (a, b):
    print("LA RESTA DE ",a," - ",b," = ",a-b)

def multiplicacion (a, b):
    print("LA MULTIPLICACIÓN DE ",a," * ",b," = ",a*b)

def division (a, b):
    if b == 0:
        print("INDETERMINADO")
    else:
        print("LA DIVISIÓN DE ",a," / ",b," = ",a/b)

while True:
    print("""
    Selecciona una operación a realizar:
          
    1) Suma
    2) Resta
    3) Multiplicación
    4) División
    5) Salir
    """)

    eleccion = int(input()) # SE INGRESA CUALQUIER OPCIÓN PRESENTADA ANTERIORMENTE.

    if eleccion == 1: # SI ES UNA SUMA
        ingresarNumeros()
        suma(num1, num2)
    elif eleccion == 2: # SI ES UNA RESTA
        ingresarNumeros()
        resta(num1, num2)
    elif eleccion == 3: # SI ES UNA MULTIPLICACIÓN
        ingresarNumeros()
        multiplicacion(num1, num2)
    elif eleccion == 4: # SI ES UNA DIVISIÓN
        ingresarNumeros()
        division(num1, num2)
    elif eleccion == 5: # PARA SALIR DE LA CALCULADORA
        print("ADIÓS, QUE LE VAYA BIEN!! :(")
        break