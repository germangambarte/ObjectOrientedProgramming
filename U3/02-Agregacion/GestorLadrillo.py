from Ladrillo import Ladrillo


class Gestor_Ladrillo:
    __ladrillos: list[Ladrillo]

    def __init__(self) -> None:
        self.__ladrillos = []

    def get_ladrillos(self):
        return self.__ladrillos

    def carga_ladrillos(self):
        ladrillo_1 = Ladrillo(1, 1000, 10, 20)
        self.__ladrillos.append(ladrillo_1)
        ladrillo_2 = Ladrillo(2, 1000, 20, 15)
        self.__ladrillos.append(ladrillo_2)

    def buscar_ladrillo_por_id(self, id: int):
        bandera = False
        valor_retorno = None
        indice = 0
        while not bandera and indice < len(self.__ladrillos):
            if self.__ladrillos[indice].get_id() == id:
                valor_retorno = indice
                bandera = False
            else:
                indice += 1
        return valor_retorno

    def mostrar_datos_material(self, indice: int):
        material = self.__ladrillos[indice].get_material()
        print(
            f"costo: {material.get_costo()}, caracteristicas: {material.get_caracteristicas()}"
        )

    def listar_materiales_por_ladrillo(self):
        print(f"\nNro indentificador\t\tMaterial\t\tCosto asociado")
        for ladrillo in self.__ladrillos:
            print(
                f"{ladrillo.get_id()}\t\t{ladrillo.get_material().get_material()}\t\t{ladrillo.get_costo_total()}"
            )
