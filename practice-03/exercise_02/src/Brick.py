# from src.Material import Material


class Brick:
    __tall = 7
    __large = 25
    __width = 15
    __quantity: int
    __brick_id: int
    __raw_material_used: float
    __cost: float
    __material: object

    def __init__(self,
                 brick_id: int,
                 quantity: int,
                 raw_material_used: float,
                 cost: float,
                 ):
        self.__quantity = quantity
        self.__brick_id = brick_id
        self.__raw_material_used = raw_material_used
        self.__cost = cost
        self.__material = None

    def add_material(self, material: object):
        self.__material = material

    def get_quantity(self):
        return self.__quantity

    def get_brick_id(self):
        return self.__brick_id

    def get_raw_material_used(self):
        return self.__raw_material_used

    def get_cost(self):
        return self.__cost

    def get_material(self):
        return self.__material
