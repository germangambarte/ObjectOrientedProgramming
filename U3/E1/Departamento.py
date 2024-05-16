class Departamento:
    __id: int
    __propietario: str
    __nro_piso: int
    __nro_depto: int
    __cant_habitaciones: int
    __cant_banios: int
    __sup_cubierta: float

    def __init__(
        self,
        id: int,
        propietario: str,
        nro_piso: int,
        nro_depto: int,
        cant_habitaciones: int,
        cant_banios: int,
        sup_cubierta: float,
    ) -> None:
        self.__id = id
        self.__propietario = propietario
        self.__nro_piso = nro_piso
        self.__nro_depto = nro_depto
        self.__cant_habitaciones = cant_habitaciones
        self.__cant_banios = cant_banios
        self.__sup_cubierta = sup_cubierta

    def get_id(self):
        return self.__id

    def get_propietario(self):
        return self.__propietario

    def get_nro_piso(self):
        return self.__nro_piso

    def get_nro_depto(self):
        return self.__nro_depto

    def get_cant_habitaciones(self):
        return self.__cant_habitaciones

    def get_cant_banios(self):
        return self.__cant_banios

    def get_sup_cubierta(self):
        return self.__sup_cubierta
