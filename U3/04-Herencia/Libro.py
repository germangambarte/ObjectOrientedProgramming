from datetime import datetime

from Publicacion import Publicacion


class Libro(Publicacion):
    __autor: str
    __fecha_edicion: int
    __cant_paginas: int

    def __init__(
        self,
        titulo: str,
        categoria: str,
        precio_base: float,
        autor: str,
        fecha_edicion: int,
        cant_paginas: int,
    ) -> None:
        super().__init__(titulo, categoria, precio_base)
        self.__autor = autor
        self.__fecha_edicion = fecha_edicion
        self.__cant_paginas = cant_paginas

    def get_precio_final(self) -> float:
        precio_base = super().get_precio_base()
        antiguedad = datetime.now().year - self.__fecha_edicion
        descuento = (precio_base * 0.01) * antiguedad
        return precio_base - descuento
