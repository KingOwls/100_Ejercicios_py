horas = int(input("hora"))
minutos = int(input("minutos"))
segundos = int(input("segundos"))

costo = ((horas * 3600) + (minutos * 60) + segundos) * 0.25


print(f"COSTO TOTAL : {costo}")