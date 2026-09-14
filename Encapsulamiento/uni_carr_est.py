class Universidad:
    nombre = ""

    def __init__(self, nombre):
        self.nombre = nombre

class Carrera:
    especialidad = ""

    def __init__(self, esp):
        self.especialidad = esp

class Estudiante:
    nombre = ""
    edad = ""

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

class Persona:
    def __init__(self, estudiante, carrera, universidad):
        self.estudiante = estudiante
        self.carrera = carrera
        self.universidad = universidad
        
universidad = Universidad("Universidad Nacional Del Oeste")
carrera = Carrera("Informatica")
estudiante = Estudiante("Carlos", "23")
persona = Persona(estudiante, carrera, universidad)

print(persona.universidad.nombre)
print(persona.carrera.especialidad)
print(persona.estudiante.nombre)
print(persona.estudiante.edad)
