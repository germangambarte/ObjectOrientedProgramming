from src.Brick import Brick


class BricksManager:
    __bricks: [Brick]

    def __init__(self):
        self.__bricks = []

    def load_bricks(self, brick: Brick):
        self.__bricks.append(brick)

    def calculate_unitary_cost(self, index):
        brick = self.__bricks[index]
        material_cost = brick.get_raw_material_used() * brick.get_material().get_additional_cost()
        return brick.get_cost() + material_cost

    def get_brick_cost(self, brick_id: int):
        i = 0
        while i < len(self.__bricks) and self.__bricks[i].get_brick_id() != brick_id:
            i += 1

        if 0 <= i < len(self.__bricks):
            return self.calculate_unitary_cost(i)
        else:
            return None

    def get_brick_order_cost(self, quantity: int):
        budget: dict = {}

        for i in range(len(self.__bricks)):
            budget[i] = self.calculate_unitary_cost(i) * quantity

        return budget

    def get_bricks(self):
        return self.__bricks