from Publicacion import Publicacion


class Audiolibro(Publicacion):
    __duracion: int
    __narrador: str

    def __init__(
        self,
        titulo: str,
        categoria: str,
        precio_base: float,
        duracion: int,
        narrador: str,
    ) -> None:
        super().__init__(titulo, categoria, precio_base)
        self.__duracion = duracion
        self.__narrador = narrador

    def get_duracion(self):
        return self.__duracion

    def get_narrador(self):
        return self.__narrador

    def get_precio_final(self) -> float:
        precio_base = super().get_precio_base()
        porcentaje_extra = precio_base * 0.1
        return precio_base + porcentaje_extra
