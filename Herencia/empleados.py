from enum import Enum

class Contrato(Enum):
    PLANTA = 1
    TEMPORAL = 2
    GERENTE = 3

class EstadoCivil(Enum):
    SOLTERO = 1
    CASADO = 2

class Empleado():
    def __init__(self, contrato, antiguedad, hijos, est_marital, horas_trabajadas):
        self.__contrato = contrato
        self.__antiguedad = antiguedad
        self.__hijos = hijos
        self.__est_marital = est_marital
        self.__horas_trabajadas = horas_trabajadas

    def calcular_sueldo(self):
        self.__sueldo = 0

        if self.__contrato == Contrato.PLANTA:
            salario_antiguedad = 100 * self.__antiguedad
            self.__sueldo = 300 * self.__horas_trabajadas + salario_antiguedad
        elif self.__contrato == Contrato.TEMPORAL:
            self.__sueldo = 200 * self.__horas_trabajadas 
        else:
            salario_antiguedad = 150 * self.__antiguedad
            self.__sueldo = 400 * self.__horas_trabajadas + salario_antiguedad

        if self.__hijos > 0:
            self.__sueldo += 200 * self.__hijos

        if self.__est_marital == EstadoCivil.CASADO:
            self.__sueldo += 100
        
        return self.__sueldo

class Empresa():
    def __init__(self):
        self.__empleados = []

    def agregar_empleado(self, empleado):
        self.__empleados.append(empleado)

    def calcular_sueldos(self):
        self.__dinero_a_pagar = 0

        for empleado in self.__empleados:
            self.__dinero_a_pagar += empleado.calcular_sueldo()

        print(f"El monto total a pagar a los empleados es: ${self.__dinero_a_pagar}")

class TestEmpresa():
    def __init__(self):
        self.__empresa = Empresa()

        empleado1 = Empleado(Contrato.PLANTA, 5, 2, EstadoCivil.CASADO, 40)
        empleado2 = Empleado(Contrato.TEMPORAL, 0, 0, EstadoCivil.SOLTERO, 30)
        empleado3 = Empleado(Contrato.GERENTE, 10, 1, EstadoCivil.CASADO, 50)

        self.__empresa.agregar_empleado(empleado1)
        self.__empresa.agregar_empleado(empleado2)
        self.__empresa.agregar_empleado(empleado3)

        self.__empresa.calcular_sueldos()

empresa = TestEmpresa()
