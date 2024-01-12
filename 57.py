
import math

dias = int(input("Ingrese los Dias"))

year = math.trunc(dias / 365)
mes = math.trunc((dias - (year * 365)) / 30)
dia = math.trunc(dias - ((year * 365) + (mes * 30)))

print(f"Año : {year}")
print(f"Mes : {mes}")
print(f"Día : {dia}")