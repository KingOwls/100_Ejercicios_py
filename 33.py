
palabra = input("Ingresa una Frase para Saber Cuantas Vocales Tiene :> ").upper()

vocales = 0
for i in palabra:
    if((i == "A") or (i == "E") or (i == "I") or (i == "O") or (i == "U")):
        vocales += 1

print("CANTIDAD VOCALES")
print({vocales})