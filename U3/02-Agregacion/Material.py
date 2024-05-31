class Material:
    __material: int
    __caracteristicas: str
    __cant_utilizada: int
    __costo_adicional: float

    def __init__(
        self,
        material: int,
        caracteristicas: str,
        cant_utilizada: int,
        costo_adicional: float,
    ) -> None:
        self.__material = material
        self.__caracteristicas = caracteristicas
        self.__cant_utilizada = cant_utilizada
        self.__costo_adicional = costo_adicional

    def get_material(self):
        return self.__material

    def get_costo(self):
        return self.__costo_adicional

    def get_caracteristicas(self):
        return self.__caracteristicas

    def get_cant_utilizada(self):
        return self.__cant_utilizada
