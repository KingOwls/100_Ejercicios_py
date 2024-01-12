

bestAlumno = {
    "nombre": "",
    "promedio": 0
}

for x in range(5):
    nombre = input("Ingresa el nombre del alumno :> ")
    promedio = input(f"Ingresa el Promedio de {nombre}")
    if (bestAlumno["promedio"] < promedio):
        bestAlumno["nombre"] = nombre
        bestAlumno["promedio"] = promedio

print(f"El Alumno con mayor nota es ")
print({bestAlumno['nombre']})
print(f"El Promedio es ")
print({bestAlumno['promedio']})