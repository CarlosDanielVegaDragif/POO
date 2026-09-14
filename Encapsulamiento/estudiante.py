class Estudiante:
    nombre = ""
    nota = 0.0

    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
        print(f"Estudiante: {self.nombre} - Nota: {self.nota}")
        if self.nota < 4:
            print("Desaprobado")
        else:
            print("Aprobado")

Estudiante("Juan", 4.5)
