
class Material:
    __material_id: int
    __characteristics: str
    __quantity_used: float
    __additional_cost: float
    __bricks: [object]

    def __init__(self,
                 material_id: int,
                 characteristics: str,
                 quantity_used: float,
                 additional_cost: float,
                 ):
        self.__material_id = material_id
        self.__characteristics = characteristics
        self.__quantity_used = quantity_used
        self.__additional_cost = additional_cost
        self.__bricks = []

    def add_brick(self, brick: object):
        self.__bricks.append(brick)

    def get_material_id(self):
        return self.__material_id

    def get_characteristics(self):
        return self.__characteristics

    def get_quantity_used(self):
        return self.__quantity_used

    def get_additional_cost(self):
        return self.__additional_cost

    def get_bricks(self):
        return self.__bricks
