import csv

from Transaccion import Transaccion


class GestorTransacciones:
    __transacciones: list[Transaccion]

    def __init__(self) -> None:
        self.__transacciones = []

    def get_transacciones(self):
        return self.__transacciones

    def agregar_cuenta(self, transaccion: Transaccion):
        self.__transacciones.append(transaccion)

    def cargar_archivo(self) -> None:
        with open("transaccionesBilleteras.csv", "r") as archivo:
            lector = csv.reader(archivo, delimiter=";")
            for fila in lector:
                transaccion: Transaccion = Transaccion(
                    fila[0],
                    fila[1],
                    float(fila[2]),
                    fila[3],
                )
                self.agregar_cuenta(transaccion)

    def mostrar(self) -> None:
        for pos, transaccion in enumerate(self.__transacciones):
            print(f"{pos + 1}. {transaccion.get_cvu()}")
