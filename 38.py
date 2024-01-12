maxPersonas = int(input("INGRESA LA CANTIDAD DE PERSONAS"))

ROJO = 0
VERDE = 0
AZUL = 0
nulo = 0

for i in range(maxPersonas):
    color = input(f"PERSONA N°{i + 1} [ROJO - VERDE - AZUL] :> ").upper()
    if (color == "ROJO"):
        ROJO += 1
    elif(color == "VERDE"):
        VERDE += 1
    elif(color == "AZUL"):
        AZUL += 1
    else:
        nulo += 1

if (ROJO > VERDE) and (ROJO > AZUL):
    print("EL ROJO FUE EL MAS VOTADO")
elif (VERDE > ROJO) and (VERDE > AZUL):
    print("EL VERDE FUE EL MAS VOTADO")
elif (AZUL > ROJO) and (AZUL > VERDE):
    print("EL AZUL FUE EL MAS VOTADO")