import math, os

def limpiar():
    os.system("cls") 


def menu():
    print("----- MENU DE AREAS -----")
    print("1. Cuadrado")
    print("2. Rectangulo")
    print("3. Circulo")
    print("4. Triangulo")
    print("5. Trapecio")
    print("6. Salir")

def cuadrado(l1, l2):
    return l1 * l2


def rectangulo(b, h):
    return b * h


def circulo(radio):
    return math.pi * radio ** 2


def triangulo(b, h):
    return (b * h) / 2


def trapecio(B, b, h):
    return (B + b) * h / 2

def programa():
    while True:
        menu()
        opcion = input("Selecciona una opcion: ")

        if opcion == "1":
            l1 = float(input("Ingresa lado 1: "))
            l2 = float(input("Ingresa lado 2: "))
            area = cuadrado(l1, l2)
            print(f"El area del cuadrado es: {area}")

        elif opcion == "2":
            b = float(input("Ingresa base: "))
            h = float(input("Ingresa altura: "))
            area = rectangulo(b, h)
            print(f"El area del rectangulo es: {area}")

        elif opcion == "3":
            radio = float(input("Ingresa radio: "))
            area = circulo(radio)
            print(f"El area del circulo es: {area}")

        elif opcion == "4":
            b = float(input("Ingresa base: "))
            h = float(input("Ingresa altura: "))
            area = triangulo(b, h)
            print(f"El area del triangulo es: {area}")

        elif opcion == "5":
            B = float(input("Ingresa base mayor: "))
            b = float(input("Ingresa base menor: "))
            h = float(input("Ingresa altura: "))
            area = trapecio(B, b, h)
            print(f"El area del trapecio es: {area}")

        elif opcion == "6":
            print("Saliendo del programa...")
            break

        else:
            print("Opcion no valida")

        input("Presiona Enter para continuar...")


programa()