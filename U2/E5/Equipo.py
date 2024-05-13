class Equipo:
    __id: int
    __nombre_equipo: str
    __goles_favor: int
    __goles_contra: int
    __diferencia_goles: int
    __puntos: int

    def __init__(
        self, id, nombre_equipo, goles_favor, goles_contra, diferencia_goles, puntos
    ):
        self.__id = id
        self.__nombre_equipo = nombre_equipo
        self.__goles_favor = goles_favor
        self.__goles_contra = goles_contra
        self.__diferencia_goles = diferencia_goles
        self.__puntos = puntos

    def __gt__(self, otro_equipo):
        if self.get_puntos() == otro_equipo.get_puntos():
            if self.get_diferencia_goles() == otro_equipo.get_diferencia_goles():
                return self.get_goles_favor() > otro_equipo.get_goles_favor()
            else:
                return self.get_diferencia_goles() > otro_equipo.get_diferencia_goles()
        else:
            return self.get_puntos() > otro_equipo.get_puntos()

    def get_id(self):
        return self.__id

    def get_nombre_equipo(self):
        return self.__nombre_equipo

    def get_goles_favor(self):
        return self.__goles_favor

    def get_goles_contra(self):
        return self.__goles_contra

    def get_diferencia_goles(self):
        return self.__diferencia_goles

    def get_puntos(self):
        return self.__puntos

    def actualizar_datos(self, gf, gc):
        self.__goles_favor += gf
        self.__goles_contra += gc
        diferencia = gf - gc
        self.__diferencia_goles += diferencia

        if diferencia > 0:
            self.__puntos += 3
        elif diferencia == 0:
            self.__puntos += 1

    def reset_equipo(self):
        self.__goles_favor = 0
        self.__goles_contra = 0
        self.__diferencia_goles = 0
        self.__puntos = 0
