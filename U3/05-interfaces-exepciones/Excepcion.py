from zope.interface import implementer

from Interfaz import IFoo


@implementer(IFoo)
class Excepcion:
    __coleccion: list

    def __init__(self) -> None:
        self.__coleccion = []

    def insertar_elemento(self, indice, elemento):
        try:
            self.__coleccion[indice] = elemento
        except IndexError:
            print("Indice no valido")

    def agregar_elemento(self, elemento):
        self.__coleccion.append(elemento)

    def mostrar_elemento(self, indice):
        try:
            print(self.__coleccion[indice])
        except IndexError:
            print("Indice no valido")
