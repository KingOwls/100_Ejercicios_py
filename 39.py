totalNotas = 0

for i in range(3):
    nota = int(input(f"Ingresa la Nota N° {i + 1}"))
    totalNotas += nota

print(f"El Promedio de las Tres Notas es : {totalNotas/3}")