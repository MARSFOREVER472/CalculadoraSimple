# EN ESTE PROYECTO CREAREMOS UNA CALCULADORA BÁSICA EN PYTHON CON 2 VALORES.

def switch ():
   global n, n2 # HAY QUE DECLARAR VARIABLES ANTES DE INGRESAR UN NÚMERO.
   n = int(input("Ingrese un número: "))
   n2 = int(input("Ingrese otro número: "))

eleccion = 0 # Inicializa su selección en 0.

while True:
    print("""
    Selecciona una operación a realizar:
          
    1) Suma
    2) Resta
    3) Multiplicación
    4) División
    5) Modificar valores
    6) Salir
    """)

    eleccion = int(input()) # SE INGRESA CUALQUIER OPCIÓN PRESENTADA ANTERIORMENTE.

    if eleccion == 1: # SI ES UNA SUMA
        print("")
        print("RESPUESTA: ", n ," + ", n2 , " = ", n+n2)
    elif eleccion == 2: # SI ES UNA RESTA
        print("")
        print("RESPUESTA: ", n ," - ", n2 , " = ", n - n2)
    elif eleccion == 3: # SI ES UNA MULTIPLICACIÓN
        print("")
        print("RESPUESTA: ", n ," * ", n2 , " = ", n * n2)
    elif eleccion == 4: # SI ES UNA DIVISIÓN
        print("")
        print("RESPUESTA: ", n ," / ", n2 , " = ", float(n / n2))
    elif eleccion == 5: # SI SE PUEDEN CAMBIAR CUALQUIER VALOR INGRESADO ANTERIORMENTE.
        n = int(input("Ingrese un número nuevamente: "))
        n2 = int(input("Ingrese nuevamente otro número: "))
    elif eleccion == 6: # PARA TERMINAR EL PROCESO.
        print("ADIÓS, QUE LE VAYA BIEN!! :(")