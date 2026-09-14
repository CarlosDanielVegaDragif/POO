while pref := input("Ingrese el prefijo del numero de telefono: ").strip():
    if len(pref) > 3:
        print("El prefijo debe tener un maximo de 3 digitos")
        continue
    break

while num := input("Ingrese el numero de telefono: ").strip():
    if len(num) > 10 or len(num) < 10:
        print("El numero debe tener 10 digitos")
        continue
    break

while ext := input("Ingrese la extension: ").strip():
    if len(ext) > 4:
        print("La extension debe tener maximo 4 digitos")
        continue
    break

print(f"{num}")
print(f"+{pref}-{num}-{ext}")
