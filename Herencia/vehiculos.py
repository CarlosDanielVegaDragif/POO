import random as rand

class Vehiculo:
    def __init__(self, chofer, acomp, pasajeros):
        self._chofer = chofer
        self._acomp = acomp
        self._pasajero = pasajeros
        self._km = rand.randrange(100, 10000)

    def cambiar_chofer(self, nuevo_chofer):
        self._chofer = nuevo_chofer
        print(f"El chofer ha sido cambiado a: {self._chofer}")

    def km_recorridos(self):
        print(f"Kilometros recorridos: {self._km}")

class Colectivo(Vehiculo):
    def __init__(self, chofer, pasajeros):
        super().__init__(chofer, 0, pasajeros)

    def cambiar_chofer(self, nuevo_chofer):
        if self._pasajero == 0 and isinstance(nuevo_chofer, str):
            super().cambiar_chofer(nuevo_chofer)
        elif not isinstance(nuevo_chofer, str):
            print("El nombre del chofer es invalido!")
        else:
            print("No se puede cambiar el chofer si hay pasajeros en el colectivo")

    def cambiar_pasajeros(self, nuevos_pasajeros=0):
        self._pasajero = nuevos_pasajeros
        if self._pasajero == 0 and isinstance(self._pasajero, int):
            print("Todos los pasajeros se bajaron")
        elif not isinstance(self._pasajero, int):
            print("La cantidad de pasajeros es invalida!")
        else:
            print(f"Ahora hay {self._pasajero} pasajeros")


class Moto(Vehiculo):
    def __init__(self, chofer, acomp):
       super().__init__(chofer, acomp, 0)

    def cambiar_chofer(self, nuevo_chofer):
        if self._acomp == "" and isinstance(nuevo_chofer, str):
            super().cambiar_chofer(nuevo_chofer)
        elif not isinstance(nuevo_chofer, str):
            print("El nombre del chofer es invalido!")
        else:
            print("No se puede cambiar el chofer si hay acompañante en la moto.")

    def cambiar_acompanante(self, nuevo_acomp=""):
        self._acomp = nuevo_acomp
        if self._acomp != "" and isinstance(self._acomp, str):
            print(f"El nuevo acompanante es: {self._acomp}")
        elif not isinstance(self._acomp, str):
            print("El nombre del pasajero es invalido!")
        else:
            print("El acompanante se bajo")

moto = Moto("Juan","")

moto.km_recorridos()
moto.cambiar_chofer(233)
moto.cambiar_chofer("Pedro")
moto.cambiar_acompanante(2)
moto.cambiar_acompanante()
moto.cambiar_acompanante("Joaquin")
moto.cambiar_chofer("Mario")

print("\n")

colectivo = Colectivo("Rodrigo", 0)

colectivo.km_recorridos()
colectivo.cambiar_chofer(442)
colectivo.cambiar_chofer("Messi") #si, ahora messi es colectivero
colectivo.cambiar_pasajeros("dwadw")
colectivo.cambiar_pasajeros(0)
colectivo.cambiar_pasajeros(10)
colectivo.cambiar_chofer("De Paul") #no lo quiere dejar solo a messi
