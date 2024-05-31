from Matricula import Matricula
from Programa_Capacitacion import Programa_Capacitacion


class Empleado:
    __nombre_apellido: str
    __id_empleado: int
    __puesto: str
    __matriculas: list[Matricula]

    def __init__(
        self,
        nombre_apellido: str,
        id_empleado: int,
        puesto: str,
    ) -> None:
        self.__nombre_apellido = nombre_apellido
        self.__id_empleado = id_empleado
        self.__puesto = puesto
        self.__matriculas = []

    def get_id(self):
        return self.__id_empleado

    def get_nombre_apellido(self):
        return self.__nombre_apellido

    def get_puesto(self):
        return self.__puesto

    def get_matriculas(self):
        return self.__matriculas

    def agregar_matricula(self, gm, fecha: str, capacitacion: Programa_Capacitacion):
        matricula = Matricula(fecha, self, capacitacion)
        gm.agregar_matricula(matricula)
        self.__matriculas.append(matricula)
