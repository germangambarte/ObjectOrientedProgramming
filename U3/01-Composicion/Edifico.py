from Departamento import Departamento


class Edificio:
    __id: int
    __nombre: str
    __direccion: str
    __nombre_constructora: str
    __cantidad_pisos: int
    __cantidad_deptos: int
    __deptos: list[Departamento]

    def __init__(
        self,
        id: int,
        nombre: str,
        direccion: str,
        nombre_constructora: str,
        cantidad_pisos: int,
        cantidad_deptos: int,
    ) -> None:
        self.__id = id
        self.__nombre = nombre
        self.__direccion = direccion
        self.__nombre_constructora = nombre_constructora
        self.__cantidad_pisos = cantidad_pisos
        self.__cantidad_deptos = cantidad_deptos
        self.__deptos: list[Departamento] = []

    def get_id(self):
        return self.__id

    def get_nombre(self):
        return self.__nombre

    def get_direccion(self):
        return self.__direccion

    def get_nombre_constructora(self):
        return self.__nombre_constructora

    def get_cantidad_pisos(self):
        return self.__cantidad_pisos

    def get_cantidad_deptos(self):
        return self.__cantidad_deptos

    def get_deptos(self):
        return self.__deptos

    def agregar_depto(self, depto):
        self.__deptos.append(depto)
