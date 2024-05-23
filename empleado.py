class Empleado:
    """
    Clase que representa un empleado de una empresa.

    Atributos:
        nombres (str): Nombres del empleado.
        apellidos (str): Apellidos del empleado.
        cargo (str): Cargo del empleado.
        salario (int): Salario del empleado.
    Métodos:
        calcular_salario(): Calcula el salario del empleado.
    """

    def __init__(self, nombres, apellidos, cargo, salario):
        self.nombres = nombres
        self.apellidos = apellidos
        self.cargo = cargo
        self.salario = salario

    def calcular_salario(self):
        return self.salario