
for i in range(3):
    dni = input("DNI :> ")
    diaCumple = int(input("DIA DE NACIMIENTO"))
    mesCumple = int(input("MES DE NACIMIENTO"))
    yearCumple = int(input("AÑO DE NACIMIENTO"))
    genero = input("GENERO (M/F) :> ")
    fechaActual = [21,12,2023]
    edad = fechaActual[2] - yearCumple

    print(f"DNI : {dni}")
    print(f"FECHA DE NACIMIENTO : {diaCumple}-{mesCumple}-{yearCumple}")
    print(f"FECHA ACTUAL : {fechaActual}")
    print(f"GENERO : {genero}")

    if(mesCumple > fechaActual[1]):
        edad -= 1
    elif((mesCumple == fechaActual[1]) and (diaCumple > fechaActual[0]) ):
        edad -= 1

    print(f"EDAD : {edad}")

    if (edad >= 8):
        print("Resibe una Tablet")
    elif(edad == 6):
        if(genero == "M"):
            print("Recibe Carrito")
        else:
            print("Recibe Muñeca")
    

