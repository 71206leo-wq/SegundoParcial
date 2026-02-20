import os
import math

class Areas:

    def inicializar(self):
        self.l1 = 0
        self.l2 = 0
        self.b = 0
        self.h = 0
        self.radio = 0
        self.B = 0
        self.res = 0

    def pedirDatos(self, opcion):

        if opcion == 1:
            self.l1 = float(input("Ingresa lado 1: "))
            self.l2 = float(input("Ingresa lado 2: "))

        elif opcion == 2:
            self.b = float(input("Ingresa base: "))
            self.h = float(input("Ingresa altura: "))

        elif opcion == 3:
            self.radio = float(input("Ingresa radio: "))

        elif opcion == 4:
            self.b = float(input("Ingresa base: "))
            self.h = float(input("Ingresa altura: "))

        elif opcion == 5:
            self.B = float(input("Ingresa base mayor: "))
            self.b = float(input("Ingresa base menor: "))
            self.h = float(input("Ingresa altura: "))


    def cuadrado(self):
        self.res = self.l1 * self.l2

    def rectangulo(self):
        self.res = self.b * self.h

    def circulo(self):
        self.res = math.pi * self.radio ** 2

    def triangulo(self):
        self.res = (self.b * self.h) / 2

    def trapecio(self):
        self.res = (self.B + self.b) * self.h / 2


    def imprimir(self):
        print("El resultado es:", self.res)


def menu():
    print("----- MENU DE AREAS -----")
    print("1. Cuadrado")
    print("2. Rectangulo")
    print("3. Circulo")
    print("4. Triangulo")
    print("5. Trapecio")
    print("6. Salir")


def programa():

    obj = Areas()
    obj.inicializar()

    op = 0

    while op != 6:
        os.system("cls")
        menu()

        op = int(input("Opcion: "))

        if op == 1:
            obj.pedirDatos(op)
            obj.cuadrado()
            obj.imprimir()
            input()

        elif op == 2:
            obj.pedirDatos(op)
            obj.rectangulo()
            obj.imprimir()
            input()

        elif op == 3:
            obj.pedirDatos(op)
            obj.circulo()
            obj.imprimir()
            input()

        elif op == 4:
            obj.pedirDatos(op)
            obj.triangulo()
            obj.imprimir()
            input()

        elif op == 5:
            obj.pedirDatos(op)
            obj.trapecio()
            obj.imprimir()
            input()

        elif op == 6:
            print("Adios")
            input()

        else:
            print("Opcion no valida")
            input()

programa()