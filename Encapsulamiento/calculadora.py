class Calculadora:
    x = 0.0
    y = 0.0
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.sumaxy()
        self.restaxy()
        self.multxy()
        self.divxy()

    def sumaxy(self):
        res = self.x + self.y
        print(f"La suma de x e y es: {res}")

    def restaxy(self):
        res = self.x - self.y
        print(f"La resta de x e y es: {res}")

    def multxy(self):
        res = self.x * self.y
        print(f"La multiplicacion de x e y es: {res}")

    def divxy(self):
        res = self.x / self.y
        print(f"La division de x e y es: {res}")

Calculadora(3, 2)
