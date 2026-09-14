import math

class Punto:
    x = 0.0
    y = 0.0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def estaSobreEjeX(self):
        if self.y == 0:
            return True
        else:
            return False

    def estaSobreEjeY(self):
        if self.x == 0:
            return True
        else:
            return False

    def esOrigenDeCoordenadas(self):
        if self.x == 0 and self.y == 0:
            return True
        else:
            return False

    def distanciaAlOrigen(self):
        d = math.sqrt(math.pow(self.x, 2) + math.pow(self.y, 2))
        return d

    def distanciaEntrePuntos(self, p1, p2):
        diffx = math.pow((p2.x - p1.x), 2)
        diffy = math.pow((p2.y - p1.y), 2)
        d = math.sqrt(diffx + diffy)
        return d

punto1 = Punto(5,5)
punto2 = Punto(0, 3)

print(punto1.distanciaAlOrigen())
print(punto1.distanciaEntrePuntos(punto1, punto2))

if punto2.estaSobreEjeY():
    print("Punto 2 esta sobre eje y")

if punto2.estaSobreEjeX():
    print("Punto 2 esta sobre eje X")
