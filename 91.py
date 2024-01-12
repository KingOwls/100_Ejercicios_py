
print(
"""
CLAVES DE DESTINO"
    1. Estados Unidos - $0.13
    2. Canadá - $0.11
    5. América del Sur - $0.52
    6. América Central - $0.99
    8. México - $0.17
    9. Europa - $0.17
    10. Asia - $0.20
    15. África - $0.59
    20. Oceanía - $0.28
"""
)

clave = int(input("INGRESE CLAVE DESTINO"))
minutos = int(input("DURACIÓN DE LA LLAMADA MINUTOS"))

if (clave == 1):
    print(f"COSTO : $.{minutos * 0.13}")
elif (clave == 2):
    print(f"COSTO : $.{minutos * 0.11}")
elif (clave == 5):
    print(f"COSTO : $.{minutos * 0.52}")
elif (clave == 6):
    print(f"COSTO : $.{minutos * 0.99}")
elif (clave == 8):
    print(f"COSTO : $.{minutos * 0.17}")
elif (clave == 9):
    print(f"COSTO : $.{minutos * 0.17}")
elif (clave == 10):
    print(f"COSTO : $.{minutos * 0.20}")
elif (clave == 15):
    print(f"COSTO : $.{minutos * 0.59}")
elif (clave == 20):
    print(f"COSTO : $.{minutos * 0.28}")
else:
    print(f"¡¡ Error en clave !!")