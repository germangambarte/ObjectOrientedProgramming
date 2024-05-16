import csv
from Edifico import Edificio
from Departamento import Departamento


class GestorEdificio:
    __edificios: list[Edificio]

    def __init__(self) -> None:
        self.__edificios = []
        self.cargar_por_archivo()

    def cargar_por_archivo(self) -> None:

        with open("datos.csv", "r") as archivo:
            lector = csv.reader(archivo, delimiter=";")
            edificio_actual = None
            for fila in lector:
                # print(fila)
                if edificio_actual != fila[0]:
                    edificio_actual = fila[0]
                    edificio = Edificio(
                        int(fila[0]),
                        fila[1],
                        fila[2],
                        fila[3],
                        int(fila[4]),
                        int(fila[5]),
                    )
                    self.__edificios.append(edificio)
                else:
                    depto = Departamento(
                        int(fila[1]),
                        fila[2],
                        int(fila[3]),
                        int(fila[4]),
                        int(fila[5]),
                        int(fila[6]),
                        float(fila[7]),
                    )
                    # print(depto.get_propietario())
                    self.__edificios[-1].agregar_depto(depto)

    def buscar_edificio_por_nombre(self, nombre: str):
        valor_retorno = None
        i = 0
        bandera = False
        while not bandera and i < len(self.__edificios):
            if self.__edificios[i].get_nombre() == nombre:
                valor_retorno = i
                bandera = True
            else:
                i += 1
        return valor_retorno

    def buscar_edificio_por_nombre_propietario(self, nombre: str):
        valor_retorno = None
        i = 0
        bandera_edificio = False
        while not bandera_edificio and i < len(self.__edificios):
            deptos = self.__edificios[i].get_deptos()
            j = 0
            bandera_depto = False
            while not bandera_depto and j < len(deptos):
                if deptos[j].get_propietario().lower() == nombre.lower():
                    valor_retorno = i
                    bandera_depto = True
                    bandera_edificio = True
                else:
                    j += 1
            i += 1
        return valor_retorno

    def buscar_depto_por_nombre_propietario(self, indice: int, nombre: str):
        valor_retorno = None
        i = 0
        bandera = False
        deptos = self.__edificios[indice].get_deptos()
        print(f"len: {len(deptos)}")

        while not bandera and i < len(deptos):
            if deptos[i].get_propietario().lower() == nombre.lower():
                valor_retorno = i
                bandera = True
            else:
                i += 1
        return valor_retorno

    def mostrar_propietarios(self, indice: int):
        i = 1
        edificio = self.__edificios[indice]
        print(f"\nEdificio: {edificio.get_nombre()}")
        print("Propietarios:")
        for depto in edificio.get_deptos():
            print(f"{i}. {depto.get_propietario()}")
            i += 1
        return None

    def calcular_sup_total(self, indice: int):
        sum = 0
        edificio = self.__edificios[indice]
        for depto in edificio.get_deptos():
            sum += depto.get_sup_cubierta()
        print(f"\nSuperficie total del edificio: {sum}mts")
        return sum

    def mostrar_sup_por_propietario(self, i_edificio, i_propietario: int):
        sup_total = self.calcular_sup_total(i_edificio)
        porcentaje = None
        depto: Departamento = self.__edificios[i_edificio].get_deptos()[i_propietario]
        porcentaje = (depto.get_sup_cubierta() * 100) / sup_total
        print(f"\nSuperficie: {depto.get_sup_cubierta()}")
        print(f"La superficie corresponde al {porcentaje:.2f}%")
        return None

    def contar_deptos(self, indice, nro_piso: int):
        sum = 0
        edificio = self.__edificios[indice]
        for depto in edificio.get_deptos():
            if depto.get_nro_piso() == nro_piso:
                if depto.get_cant_habitaciones() == 3 and depto.get_cant_banios() > 1:
                    sum += 1
        print(f"{sum} deptos tienen 3 habitaciones y mas de un banio")

    def mostrar_edificios(self):
        i = 1
        for edificio in self.__edificios:
            print(f"Edificio: {edificio.get_nombre()}")
            print("Propietarios")
            for depto in edificio.get_deptos():
                print(f"{i}. {depto.get_propietario()}")
                i += 1
        return None
