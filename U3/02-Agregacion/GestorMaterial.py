from Material import Material


class Gestor_Material:
    __materiales: list[Material]

    def __init__(self) -> None:
        self.__materiales = []

    def carga_materiales(self):
        material_1 = Material(1, "Caracteristica 1 y 2", 10, 0.20)
        self.__materiales.append(material_1)
        material_2 = Material(3, "Caracteristica 3 y 4", 10, 0.50)
        self.__materiales.append(material_2)
