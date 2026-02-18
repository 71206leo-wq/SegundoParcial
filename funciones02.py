import os

def suma():
    os.system("cls")
    a=int(input('Numero 1: '))
    b=int(input('Numero 2: '))
    resultado=a+b
    print("la suma es: ", resultado)
    input()

def resta():
    os.system("cls")
    a=int(input('Numero 1: '))
    b=int(input('Numero 2: '))
    resultado=a-b
    print("la resta es: ", resultado)
    input()

def menu():
    op=0
    while op!=3:
        os.system("cls")
        print("1.+ \n2.- \n3.Salir")
    
        op=int(input("Selecciona una opcion: "))
        
        if op==1:
            suma()
        if op==2:
            resta()
       
    