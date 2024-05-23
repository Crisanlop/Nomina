from empleado import Empleado

class Gerente(Empleado):
    """
    Clase que representa un gerente de una empresa.

    Herencia:
        Empleado: Clase base de la que hereda.

    Atributos:
        ninguno

    Métodos:
        calcular_salario(): Calcula el salario del gerente (sobrescrito).
    """

    def calcular_salario(self):
        salario_base = super().calcular_salario()
        return salario_base * 1.2