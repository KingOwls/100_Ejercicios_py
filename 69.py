
apro = int(input("INGRESE LA CANTIDAD DE ALUMNOS APROBADOS"))
desa = int(input("INGRESE LA CANTIDAD DE ALUMNOS DESAPROBADOS"))

porA = (apro * 100) / (apro + desa)
porB = (desa * 100) / (apro + desa)

print(f"APROBADOS : {round(porA * 100) / 100}%")
print(f"DESAPROBADOS : {round(porB * 100) / 100}%")