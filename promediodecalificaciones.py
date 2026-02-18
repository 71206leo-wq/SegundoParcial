num=int(input("¿Cuántas alumnos quieres ingresar? "))
for i in range(1,num):
    nombre=input("Ingrese el nombre del alumno: ")
    edad=int(input("Ingrese la edad del alumno: "))
    materia=input("Ingrese la materia del alumno: ")
    promedio=float(input("Ingrese el promedio del alumno: "))
    
    alumno1["nombre"]=nombre
    alumno1["edad"]=edad
    alumno1["materia"]=materia
    alumno1["promedio"]=promedio
    
    print("lista de alumnos:")
    