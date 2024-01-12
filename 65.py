
import math

radio = float(input("RADIO"))
altura = float(input("ALTURA"))

area = 2 * math.pi * radio * (altura + radio)
volumen = math.pi * (radio * radio) * altura

print(f"ÁREA TOTAL DEL CILINDRO : {area}cm2")
print(f"VOLUMEN DEL CILINDRO : {volumen}cm3")

