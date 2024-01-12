
usuario = input("INGRESE USUARIO")
clave = int(input("INGRESE CODIGO "))

if (usuario == "ADMIN" and clave == 123456):
    print(f"ACCESO PERMITIDO")
else:
    print(f"ACCESO DENEGADO")