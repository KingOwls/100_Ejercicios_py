
run = True

turnoMañana= 0
turnoNoche= 0
importeOnimus=0
importeMinivan=0
importeMicro=0



while(run):
    print(
        """TIPO DE VEHICULO

    1. Omnibus
    2. Minivan
    3. Micro
    4. Salir

    """
    )
    option = int(input(""))
    tarifa = 0
    if (option == 1):
        tarifa = 5
        importeOnimus+=  tarifa
    elif(option == 2):
        tarifa = 10
        importeMinivan +=  tarifa
    elif(option == 3):
        tarifa = 8
        importeMicro+=  tarifa
    elif(option == 4):
        run = False
    else:
        print("No Conosco esa Opcion")
    
    turno = input("Ingresa el Turno (M/N) :> ").upper()
    
    if (turno == "M"):
        turnoMañana+=  tarifa
    else:
        turnoNoche+=  tarifa

print(f"Turno de La Mañana : {turnoMañana}")
print(f"Turno de La Noche : {turnoNoche}")

print(f"Importe de Ohmibus : {importeOnimus}")
print(f"Importe de Minivan : {importeMinivan}")
print(f"Importe de Micro : {importeMicro}")
