
import random


rebajt = 0
compra = 0


compra = int(input("VALOR DE COMPRA"))
color = random.randint(1, 5)


if (color == 1):
    print(f"COLOR : BLANCO")
    rebajt = 1
elif (color == 2):
    print(f"COLOR : VERDE")
    rebajt = 0.5
elif (color == 3):
    print(f"COLOR : NEGRO")
    rebajt = 0.4
elif (color == 4):
    print(f"COLOR : CELESTE")
    rebajt = 0.05
elif (color == 5):
    print(f"COLOR : ROJO")
    rebajt = 0

print(f"rebajUENTO : {rebajt}")
print(f"IMPORTE rebajT. : {compra * rebajt}")
print(f"PAGO FINAL : {compra - (compra * rebajt)}")