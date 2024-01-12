
numero = str(input("Ingresa Un Numero Para Verificar si es capicúa"))

if (numero == (numero[::-1])):
    print("SI ES UN NUMERO CAPICUA")
else: 
    print("NO ES UN NUMERO CAPICUA")