

SueldoBase = 0
num_hijos = 0
dias_no_laborables = 0
sueldo_final = 0


SueldoBase = float(input("Ingrese Sueldo Base"))
num_hijos = int(input("Ingrese Número de Hijos"))
dias_no_laborables = float(input("Ingrese Días no Laborables Trabajados"))

sueldo_final = SueldoBase + (num_hijos * 100) +(dias_no_laborables * 25)

print(f"SUELDO FINAL : ${sueldo_final}")