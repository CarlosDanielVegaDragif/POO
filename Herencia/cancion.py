from abc import ABC, abstractmethod

class Cancion(ABC):
    _canciones = []

    def __init__(self, n_ref, titulo, album, grupo):
        self._n_ref = n_ref
        self._titulo = titulo
        self._album = album
        self._grupo = grupo
        self.crear(self)

    @abstractmethod
    def imprimir_cancion(self):
        pass

    @staticmethod
    def crear(cancion):
        Cancion._canciones.append(cancion)

    @staticmethod
    def eliminar(n_ref):
        for cancion in Cancion._canciones:
            if cancion._n_ref == n_ref:
                Cancion._canciones.remove(cancion)
                break

    @staticmethod
    def listado():
        for cancion in Cancion._canciones:
            cancion.imprimir_cancion()
            print("\n")

class Clasica(Cancion):
    def __init__(self, n_ref, titulo, album, grupo, instrumento="Piano"):
        self._instrumento = instrumento
        super().__init__(n_ref, titulo, album, grupo)

    def imprimir_cancion(self):
        print(f"Referencia: {self._n_ref}")
        print(f"Titulo: {self._titulo}")
        print(f"Album: {self._album}")
        print(f"Grupo: {self._grupo}")
        print(f"Instrumento: {self._instrumento}")

class TestClasica:
    def __init__(self):
        cancion1 = Clasica(1, "Canon in D", "Pachelbel", "Johann Pachelbel", "Piano")
        cancion2 = Clasica(2, "Fur Elise", "Beethoven", "Ludwig van Beethoven", "Piano")
        cancion3 = Clasica(3, "Las Cuatro Estaciones", "Vivaldi", "Antonio Vivaldi", "Violin")

        Cancion.listado()

test = TestClasica()
