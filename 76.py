

n1 = int(input("INGRESE NÚMERO 01"))
n2 = int(input("INGRESE NÚMERO 02"))
n3 = int(input("INGRESE NÚMERO 03"))

if (n1 > n2):
    medio = n1
    xtem = n2
else:
    medio = n2
    xtem = n1

if (medio > n3):
    medio = n3

if (medio < xtem):
    medio = xtem

print(f"EL NÚMERO MEDIO ES : {medio}")