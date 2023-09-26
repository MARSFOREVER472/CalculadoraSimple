def sumar2NumerosCualquiera ():
    global n1, n2
    n1 = int(input("INGRESE UN NÚMERO: "))
    n2 = int(input("INGRESE OTRO NÚMERO: "))

def sumar3NumerosCualquiera ():
    global n1, n2, n3
    n1 = int(input("INGRESE UN NÚMERO: "))
    n2 = int(input("INGRESE OTRO NÚMERO: "))
    n3 = int(input("INGRESE OTRO NÚMERO: "))

def sumar2Numeros (a, b):
    print("LA SUMA DE DOS NÚMEROS ",a," + ",b," = ",a+b)

def sumar3Numeros (a, b, c):
    print("LA SUMA DE TRES NÚMEROS ",a," + ",b," + ",c," = ",a+b+c)

while True:
    print("""
          Indique la operación a realizar:
          
          1) SUMAR 2 NÚMEROS
          2) SUMAR 3 NÚMEROS
          3) SALIR DE LA CALCULADORA
          """)
    
    eleccion = int(input())

    if eleccion == 1:
        sumar2NumerosCualquiera()
        sumar2Numeros(n1, n2)
    elif eleccion == 2:
        sumar3NumerosCualquiera()
        sumar3Numeros(n1, n2, n3)
    elif eleccion == 3:
        print("HASTA PRONTO!!")
        break
