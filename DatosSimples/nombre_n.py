nombre = input("Por favor, ingrese su nombre: ")
veces = int(input("Ingrese la cantidad de repeticiones: "))

for i in range(veces):
    print(f"{nombre}")
    print(f"{nombre.lower()}")
    print(f"{nombre.upper()}")
    print(f"{nombre.capitalize()}")
    print(f"{len(nombre)}")
