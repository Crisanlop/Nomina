class Empresa:
    """
    Clase que representa una empresa.

    Atributos:
        nombre (str): Nombre de la empresa.
        departamentos (list[Departamento]): Lista de departamentos de la empresa.
    Métodos:
        calcular_nomina(): Calcula la nómina total de la empresa.
    """

    def __init__(self, nombre):
        self.nombre = nombre
        self.departamentos = []

    def calcular_nomina(self):
        nomina_total = 0
        for departamento in self.departamentos:
            nomina_total += departamento.calcular_nomina()
        return nomina_total