n = input("Ingrese un numero entero positivo: ")
idx = 1
total = 0
while idx <= int(n):
    print("idx: ", idx, " total: ", total)
    total += idx
    idx += 1
print("El resultado de la suma de ", n, " es: ", total)
