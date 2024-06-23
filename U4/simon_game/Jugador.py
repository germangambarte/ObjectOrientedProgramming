class Jugador:
    __nombre: str
    __fecha: str
    __hora: str
    __puntaje: int

    def __init__(self, nombre, fecha, hora, puntaje) -> None:
        self.__nombre = nombre
        self.__fecha = fecha
        self.__hora = hora
        self.__puntaje = puntaje

    def __gt__(self, otro):
        if isinstance(otro, Jugador):
            return self.get_puntaje() > otro.get_puntaje()

    def get_nombre(self):
        return self.__nombre

    def get_fecha(self):
        return self.__fecha

    def get_hora(self):
        return self.__hora

    def get_puntaje(self):
        return self.__puntaje

    def tojson(self):
        return dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(
                nombre=self.__nombre,
                fecha=self.__fecha,
                hora=self.__hora,
                puntaje=self.__puntaje,
            ),
        )
