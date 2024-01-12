

print(""" 
MENÚ DE OPCIONES DE UN TRIÁNGULO "

    1. Área de un triángulo, dada la base y la altura"
    2. Base de un triángulo, dada la altura y el área"
    3. Altura de un triángulo, dada la base y el área
"""
)

opcionMenu = int(input("Selecciona una opción"))


if (opcionMenu == 1):
    base = float(input("BASE"))
    altura = float(input("ALTURA"))
    area = (base * altura) / 2
    print(f"EL ÁREA ES : {area}")

elif (opcionMenu == 2):
    altura = float(input("ALTURA"))
    area = float(input("ÁREA"))
    base = (area * 2) / altura
    print(f"LA BASE ES : {base}")

elif (opcionMenu == 3):
    base = float(input("BASE"))
    area = float(input("ÁREA"))
    altura = (area * 2) / base
    print(f"LA ALTURA ES : {altura}")

else:
    print(f"Error... Opción Incorrecta")