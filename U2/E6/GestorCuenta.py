import csv
import numpy as np

from Cuenta import Cuenta


class GestorCuenta:
    __dimension: int
    __cantidad: int
    __incremento: int
    __cuentas: np.ndarray

    def __init__(self) -> None:
        self.__dimension = 0
        self.__cantidad = 0
        self.__incremento = 1
        self.__cuentas = np.empty(self.__dimension, Cuenta)

    def agregar_cuenta(self, cuenta: Cuenta) -> None:
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__cuentas.resize(self.__dimension)
        self.__cuentas[self.__cantidad] = cuenta
        self.__cuentas += 1

    def cargar_archivo(self) -> None:
        with open("cuentasBilleteras.csv", "r") as archivo:
            lector = csv.reader(archivo, delimiter=";")
            for fila in lector:
                cuenta: Cuenta = Cuenta(
                    fila[0],
                    fila[1],
                    fila[2],
                    fila[3],
                    float(fila[4]),
                    fila[5],
                    float(fila[6]),
                )
                self.agregar_cuenta(cuenta)

    def mostrar(self) -> None:
        for pos, cuenta in enumerate(self.__cuentas):
            print(f"{pos + 1}. {cuenta.get_nombre()} {cuenta.get_apellido()}")
