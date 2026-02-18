#Captura de datos de alumnos
alumnos = []
cantidad = int(input("¿Cuántos alumnos quieres capturar? "))

for i in range(cantidad):
    print("\nAlumno", i + 1)
    
    nombre = input("Ingresa el nombre: ")
    edad = int(input("Ingresa la edad: "))
    carrera = input("Ingresa la carrera: ")
    
    alumno = {
        "nombre": nombre,
        "edad": edad,
        "carrera": carrera
    }
    
    alumnos.append(alumno)

print("\n--- LISTA DE ALUMNOS ---")

for alumno in alumnos:
    print("Nombre:", alumno["nombre"])
    print("Edad:", alumno["edad"])
    print("Carrera:", alumno["carrera"])
    print("------------------------")