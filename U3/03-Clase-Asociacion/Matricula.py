# from Empleado import Empleado
# from Programa_Capacitacion import Programa_Capacitacion


class Matricula:
    __fecha: str
    __empleado: object
    __capacitacion: object

    def __init__(
        self,
        fecha: str,
        empleado: object,
        capacitacion: object,
    ) -> None:
        self.__fecha = fecha
        self.__empleado = empleado
        self.__capacitacion = capacitacion

    def get_fecha(self):
        return self.__fecha

    def get_empleado(self):
        return self.__empleado

    def get_capacitacion(self):
        return self.__capacitacion
