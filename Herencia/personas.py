class Personas:
    def __init__(self, nombre, apellido):
        self.__nombre = nombre
        self.__apellido = apellido

    def nombre_completo(self):
        print(f"{self.__nombre} {self.__apellido}")

class Estudiante(Personas):
    def __init__(self, nombre, apellido, edad, carrera):
        super().__init__(nombre, apellido)
        self.__edad = edad
        self.__carrera = carrera

    def mostrar_carrera(self):
        print(f"{self.__carrera}")

est = Estudiante("Carlos", "Vega", 105, "Informatica")

est.nombre_completo()
est.mostrar_carrera()
