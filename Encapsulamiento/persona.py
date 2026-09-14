class Persona:
    _nombre = ""
    _edad = 0
    
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad
        print(f"{self._nombre} tiene {self._edad}")

    def __cumpleanos__(self):
        self._edad += 1
        print(f"{self._nombre} cumplio {self._edad}")

juan = Persona("Juan", 45)
juan.__cumpleanos__()

