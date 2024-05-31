from Programa_Capacitacion import Programa_Capacitacion


class Gestor_Programa_Capacitacion:
    __programas: list[Programa_Capacitacion]

    def __init__(self) -> None:
        self.__programas = []

    def agregar_programa(self, programa: Programa_Capacitacion):
        self.__programas.append(programa)

    def get_programas(self):
        return self.__programas
