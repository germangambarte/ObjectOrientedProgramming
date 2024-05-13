import csv
from Equipo import Equipo


class GestorEquipo:
    __equipos: list[Equipo]

    def __init__(self):
        self.__equipos = []

    def get_equipos(self):
        return self.__equipos

    def carga_equipos_por_archivo(self):
        with open("equipos2024.csv", "r") as archivo:
            lector = csv.reader(archivo, delimiter=";")

            for fila in lector:
                equipo = Equipo(
                    int(fila[0]),
                    fila[1],
                    int(fila[2]),
                    int(fila[3]),
                    int(fila[4]),
                    int(fila[5]),
                )
                print(f"{equipo.get_nombre_equipo()}: cargado")
                self.__equipos.append(equipo)
        print(len(self.__equipos))

    def obtener_indice_por_nombre(self, nombre):
        valorRetorno = None
        i = 0
        bandera = False

        while not bandera and i < len(self.__equipos):
            if self.__equipos[i].get_nombre_equipo() == nombre:
                valorRetorno = i
                bandera = True
            else:
                i += 1
        return valorRetorno

    def obtener_indice_por_id(self, id):
        valorRetorno = None
        bandera = False
        i = 0
        while not bandera and i < len(self.__equipos):
            if self.__equipos[i].get_id() == id:
                valorRetorno = i
                bandera = True
            else:
                i += 1
        return valorRetorno

    def resetear_tabla_de_posiciones(self):
        for equipo in self.__equipos:
            equipo.reset_equipo()

    def actualizar_tabla(self, fechas):
        self.resetear_tabla_de_posiciones()
        for fecha in fechas:
            indice_local = self.obtener_indice_por_id(fecha.get_id_local())
            if indice_local is None:
                print("No se encontro el equipo local")
                return
            indice_visitante = self.obtener_indice_por_id(fecha.get_id_visitante())
            if indice_visitante is None:
                print("No se encontro el equipo visitante")
                return
            self.__equipos[indice_local].actualizar_datos(
                fecha.get_goles_local(), fecha.get_goles_visitante()
            )
            self.__equipos[indice_visitante].actualizar_datos(
                fecha.get_goles_visitante(), fecha.get_goles_local()
            )

    def ordenar_equipos(self):
        self.__equipos = sorted(self.__equipos, reverse=True)

    def exportar_datos(self):
        self.ordenar_equipos()
        with open("equiposExportado.csv", "w") as archivo:
            escritor = csv.writer(archivo, delimiter=";")
            for equipo in self.__equipos:
                fila = [
                    equipo.get_id(),
                    equipo.get_nombre_equipo(),
                    equipo.get_goles_favor(),
                    equipo.get_goles_contra(),
                    equipo.get_diferencia_goles(),
                    equipo.get_puntos(),
                ]
                escritor.writerow(fila)

    def mostrar_equipos(self):
        for pos, equipo in enumerate(self.__equipos):
            print(f"\n{pos + 1}. {equipo.get_nombre_equipo()}")
