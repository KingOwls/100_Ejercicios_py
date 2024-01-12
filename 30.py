


catidadEmpleados = int(input("Ingresa la Cantidad de Empleados"))
empleados = []
MVentas = 0
FVentas = 0

porcMujeres = 0

for i in range(catidadEmpleados):
    nombre = input("Ingresa el Nombre del Empleado :> ")
    genero = input("Ingresa el Genero del Empleado (M/F) :> ").upper()
    ventas = int(input(f"Ingresa el total de Ventas del Empleado {nombre}"))
    empleado = {
        "Nombre": nombre,
        "Genero": genero,
        "Ventas": ventas
    }
    if (genero == "M"):
        MVentas += ventas
    else:
        MVentas += ventas
        porcMujeres += 1

    empleados.append(empleado)

print(f"TOTAL DE VENTAS HOMBRES {MVentas}")
print(f"TOTAL DE VENTAS MUJERES {MVentas}")



print(f"PORCENTAJE DE MUJERES {(porcMujeres / len(empleados) * 100)}")

