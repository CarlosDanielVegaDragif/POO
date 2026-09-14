class Fabrica:
    def __init__(self, llantas, color, precio):
        self._llantas = llantas
        self._color = color
        self._precio = precio

class Moto(Fabrica):
    def cant_llantas(self):
        print(f"Llantas de Moto: {self._llantas}")

    def color(self):
        print(f"Color de Moto: {self._color}")

    def precio(self):
        print(f"Precio de Moto: {self._precio}")   

class Auto(Fabrica):
    def cant_llantas(self):
        print(f"Llantas de Auto: {self._llantas}")

    def color(self):
        print(f"Color de Auto: {self._color}")

    def precio(self):
        print(f"Precio de Auto: {self._precio}")

moto = Moto(2, "Rojo", 1234)
auto = Auto(4, "Negro", 1234)

auto.cant_llantas()
auto.color()
auto.precio()
