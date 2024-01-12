
import math

segundos = int(input("Ingresa el numero de segundos"))

hor = math.trunc(segundos / 3600)
minu = math.trunc((segundos - (hor * 3600)) / 60)
seg = math.trunc(segundos - ((hor * 3600) + (minu * 60)))

print(f"Hora : {hor}")
print(f"Mminuto : {minu}")
print(f"Segundos : {seg}")

