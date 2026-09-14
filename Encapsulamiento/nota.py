class Nota:

    def __init__(self, n):
        if 0 <= n <= 10:
            self.__nota = n
        else:
            raise ValueError("El valor tiene que ser 0 <= n <= 10")

    def obtenerValor(self):
        return self.__nota

    def aprovado(self):
        return self.__nota >= 4

    def desaprovado(self):
        return self.__nota < 4

    def nuevoValor(self, nuevaNota):
        if nuevaNota > self.__nota and nuevaNota <= 10:
            self.__nota = nuevaNota
            print(f"La nueva nota es: {self.__nota}")
        else:
            print("Solo se puede reemplazar con una nota mayor que la actual y menor que 10")


n = Nota(4)
print(f"La nota es: {n.obtenerValor()}")
print(f"Esta aprobado? {n.aprovado()}")
print(f"Esta desaprobado? {n.desaprovado()}")
n.nuevoValor(7)
