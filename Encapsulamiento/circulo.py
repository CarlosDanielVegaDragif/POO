import math

class Circulo:

    def __init__(self, radio):
        self.radio = radio
    
        self.diametro = self.radio * 2
        self.perimetro = 2 * math.pi * self.radio
        self.area = math.pi * self.radio ** 2

        self.imprimirCirculo()

    def imprimirCirculo(self):
        print(f"El radio del circulo es: {self.radio}")
        print(f"El diametro del circulo es: {self.diametro}")
        print(f"El perimetro del circulo es: {self.perimetro}")
        print(f"El area del circulo es: {self.area}")
        print("\n")

    def actualizarCirculo(self, radio):
        self.radio = radio
    
        self.diametro = self.radio * 2
        self.perimetro = 2 * math.pi * self.radio
        self.area = math.pi * self.radio ** 2
        
        self.imprimirCirculo()

cir = Circulo(5)
cir.actualizarCirculo(2)
