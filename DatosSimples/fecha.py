#Se ingresa un valor numérico de 8 dígitos que representa una fecha con el siguiente formato aaaammdd. Se pide informar por separado el día, el mes y el año de la fecha ingresada

#dia = input("Ingrese el dia: ").strip()
while dia := input("Ingrese el dia: ").strip():
    if not dia.isdigit() or not (1 <= int(dia) <= 31) or len(dia) > 2:
        print("Por favor, ingrese un día válido entre 1 y 31.")
        continue
    break
#mes = input("Ingrese el mes: ").strip()
while mes := input("Ingrese el mes: ").strip():
    if not mes.isdigit() or not (1 <= int(mes) <= 12) or len(mes) > 2:
        print("Por favor, ingrese un mes válido entre 1 y 12.")
        continue
    break
#ano = input("Ingrese el año: ").strip()
while ano := input("Ingrese el año: ").strip():
    if not ano.isdigit() or len(ano) != 4 or int(ano) < 1900 or int(ano) > 2026:
        print("Por favor, ingrese un año válido de 4 dígitos.")
        continue
    break
fecha = ano + "/" + mes.zfill(2) + "/" + dia.zfill(2)
print("La fecha ingresada es: ", fecha)

f_fecha = f"{int(ano):04d}/{int(mes):02d}/{int(dia):02d}"
print("La fecha con f-string es: ", f_fecha)
