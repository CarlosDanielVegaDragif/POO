class Marino:
    def __init__(self):
        pass

    def hablar(self):
        print("Hola, soy un animal marino!")

class Pulpo(Marino):
    def hablar(self):
        print("Hola, soy un pulpo!")

class Foca(Marino):
    def hablar(self, mensaje=""):
        if(mensaje != ""):
            print(mensaje)
        else:
            print("Hola, soy una foca!")

marino = Marino()
pulpo = Pulpo()
foca = Foca()

marino.hablar()
pulpo.hablar()
foca.hablar("focaaaaaaaaaaaaaaa")
