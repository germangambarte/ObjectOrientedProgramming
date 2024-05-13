class FechaFutbol:
    __fecha_partido: str
    __id_local: int
    __id_visitante: int
    __goles_local: int
    __goles_visitante: int

    def __init__(
        self, fecha_partido, id_local, id_visitante, goles_local, goles_visitante
    ):
        self.__fecha_partido = fecha_partido
        self.__id_local = id_local
        self.__id_visitante = id_visitante
        self.__goles_local = goles_local
        self.__goles_visitante = goles_visitante

    def get_fecha_partido(self):
        return self.__fecha_partido

    def get_id_local(self):
        return self.__id_local

    def get_id_visitante(self):
        return self.__id_visitante

    def get_goles_local(self):
        return self.__goles_local

    def get_goles_visitante(self):
        return self.__goles_visitante
