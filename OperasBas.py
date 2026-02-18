import os
def limpiar():
    os.system("cls")

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b==0:
        return "Error: no se puede dividir entre o"
    return a / b

def menu():
    print("-----Menu de operaciones-----")
    print("1.- Suma (+)")
    print("2.- Resta (-)")
    print("3.- Multiplicacion (*)")
    print("4.- Division (/)")
    print("5.- Salir")
    
while True :
    menu()
    opcion = input("Selecciona una opcion: ")
    
    if opcion == "5":
        print("Saliendo del programa...")
        break
    
    num1 = float(input("Ingresa el primer numero: "))
    num2 = float(input("Ingresa el segundo numero: "))
    
    if opcion == "1":
        resultado = suma(num1, num2)
        print(f"El resultado de la suma es: {resultado}")
    elif opcion == "2":
        resultado = resta(num1, num2)
        print(f"El resultado de la resta es: {resultado}")
    elif opcion == "3":
        resultado = multiplicacion(num1, num2)
        print(f"El resultado de la multiplicacion es: {resultado}")
    elif opcion == "4":
        resultado = division(num1, num2)
        print(f"El resultado de la division es: {resultado}")
    else:
        print("Opcion no valida. Por favor, selecciona una opcion del 1 al 5.")
    
    input("Presiona Enter para continuar...")
    limpiar()
    
