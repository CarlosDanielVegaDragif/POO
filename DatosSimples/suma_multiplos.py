def suma_multiplos(n):
    suma = 0
    for i in range(n):
        if i % 3 == 0 or i % 5 == 0:
            suma += i
    return suma

print(suma_multiplos(10))
