import math

def show_menu():
    print("\n--- CALCULADORA CON SUMAS O VICEVERSA ---")
    print("1. Sumar")
    print("2. Potencia")
    print("3. Raíz Cuadrada")
    print("4. Salir")

def calculadora():
    while True:
        show_menu()
        opcion = input("\nElige una opción del 1 al 10: ")

        if opcion == "4":
            print("¡HASTA PRONTO!")
            break