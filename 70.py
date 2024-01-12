
n1 = float(input("INGRESE NOTA 01"))
n2 = float(input("INGRESE NOTA 02"))
n3 = float(input("INGRESE NOTA 03"))

prom = (n1 + n2 + n3)/3

if (prom > 10.5):
    print(f"APROBADO CON {prom}")
else:
    print(f"DESAPROBADO CON {prom}")