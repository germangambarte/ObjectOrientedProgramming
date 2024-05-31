from Material import Material


class Ladrillo:
    __alto = 8
    __largo = 27
    __ancho = 13
    __cantidad: int
    __id: int
    __kg_mat_pri_uti: float
    __costo: float
    __material: Material

    def __init__(
        self,
        id: int,
        cantidad: int,
        costo: float,
        material=None,
    ):
        self.__id = id
        self.__cantidad = cantidad
        self.__costo = costo
        if material != None:
            self.__material = material
            self.__kg_mat_pri_uti = material.get_cant_utilzada()

    def get_id(self):
        return self.__id

    def get_material(self):
        return self.__material

    def get_costo_total(self):
        costo_total = self.__costo
        costo_total += (
            self.__material.get_costo() * self.__material.get_cant_utilizada()
        )
        return costo_total

    def agregar_material(self, material):
        self.__material = material
