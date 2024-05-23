class Departamento:
    """
    Clase que representa un departamento de una empresa.

    Atributos:
        nombre (str): Nombre del departamento.
        gerente (Gerente): Objeto que representa al gerente del departamento.
        empleados (list[Empleado]): Lista de empleados del departamento.
    Métodos:
        nombrar_gerente(Gerente): Nombra a un gerente para el departamento.
        agregar_empleado(Empleado): Agrega un empleado al departamento.
        agregar_empleados(list[Empleado]): Agrega una lista de empleados al departamento.
        calcular_nomina(): Calcula la nómina total del departamento.
    """

    def __init__(self, nombre):
        self.nombre = nombre
        self.gerente = None
        self.empleados = []

    def nombrar_gerente(self, gerente):
        self.gerente = gerente

    def agregar_empleado(self, empleado):
        self.empleados.append(empleado)

    def agregar_empleados(self, empleados):
        self.empleados.extend(empleados)

    def calcular_nomina(self):
        nomina_total = 0
        for empleado in self.empleados:
            nomina_total += empleado.calcular_salario()
        return nomina_total