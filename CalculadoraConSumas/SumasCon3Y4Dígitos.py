# ESTA ES UNA CALCULADORA ALTERNATIVA CON MÁS DÍGITOS CUALQUIERA.

def sumar3NumerosCualquiera ():
    global n1, n2, n3
    n1 = int(input("INGRESE UN NÚMERO: "))
    n2 = int(input("INGRESE OTRO NÚMERO: "))
    n3 = int(input("INGRESE UN ÚLTIMO NÚMERO: "))

def sumar4NumerosCualquiera ():
    global n1, n2, n3, n4
    n1 = int(input("INGRESE UN NÚMERO: "))
    n2 = int(input("INGRESE OTRO NÚMERO: "))
    n3 = int(input("INGRESE OTRO NÚMERO: "))
    n4 = int(input("INGRESE UN ÚLTIMO NÚMERO: "))

def sumar3Numeros (a, b, c):
    print("LA SUMA DE TRES NÚMEROS ",a," + ",b," + ",c," = ",a+b+c)

def sumar4Numeros (a, b, c, d):
    print("LA SUMA DE CUATRO NÚMEROS ",a," + ",b," + ",c," + ",d," = ",a+b+c+d)

while True:
    print("""
          Indique la operación a realizar:
          
          1) SUMAR 3 NÚMEROS
          2) SUMAR 4 NÚMEROS
          3) SALIR DE LA CALCULADORA
          """)
    
    eleccion = int(input())

    if eleccion == 1:
        sumar3NumerosCualquiera()
        sumar3Numeros(n1, n2, n3)
    elif eleccion == 2:
        sumar4NumerosCualquiera()
        sumar4Numeros(n1, n2, n3, n4)
    elif eleccion == 3:
        print("HASTA PRONTO!!")
        break