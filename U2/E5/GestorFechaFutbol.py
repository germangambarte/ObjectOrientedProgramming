import numpy as np
import csv

from FechaFutbol import FechaFutbol


class GestorFechaFutbol:
    __dimension: int
    __cantidad: int
    __incremento: int
    __fechas: np.ndarray

    def __init__(self):
        self.__dimension = 1
        self.__cantidad = 0
        self.__incremento = 1
        self.__fechas = np.empty(self.__dimension, FechaFutbol)

    def get_fechas(self):
        return self.__fechas

    def agregar_fecha(self, nueva_fecha: FechaFutbol):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__fechas.resize(self.__dimension)
        self.__fechas[self.__cantidad] = nueva_fecha
        self.__cantidad += 1

    def carga_fechas_por_archivo(self):
        with open("fechasFutbol.csv", "r") as archivo:
            lector = csv.reader(archivo, delimiter=";")

            for fila in lector:
                fecha = FechaFutbol(
                    fila[0],
                    int(fila[1]),
                    int(fila[2]),
                    int(fila[3]),
                    int(fila[4]),
                )
                self.agregar_fecha(fecha)

    def mostrar_fechas_por_equipo(self, equipo):
        id = equipo.get_id()
        print("Fecha \t\tEquipo \t\tGF \tGC \tDF \tPTS")
        for fecha in self.__fechas:
            if id in (fecha.get_id_local(), fecha.get_id_visitante()):
                if id == fecha.get_id_local():
                    goles_favor = fecha.get_goles_local()
                    goles_contra = fecha.get_goles_visitante()
                else:
                    goles_favor = fecha.get_goles_visitante()
                    goles_contra = fecha.get_goles_local()

                diferencia_goles = goles_favor - goles_contra
                puntos = 0

                if diferencia_goles > 0:
                    puntos = 3
                elif diferencia_goles == 0:
                    puntos = 1

                print(
                    f"{fecha.get_fecha_partido()} \t{equipo.get_nombre_equipo()} \t{goles_favor} \t{goles_contra} \t{diferencia_goles} \t{puntos}"
                )
        print(
            f"Total \t\t\t\t{equipo.get_goles_favor()} \t{equipo.get_goles_contra()} \t{equipo.get_diferencia_goles()} \t{equipo.get_puntos()}"
        )

    def mostrar_fechas(self):
        for fecha in self.__fechas:
            print(f"fecha: {fecha.get_fecha_partido()}")
