import unittest
from src.Material import Material
from src.MaterialsManager import MaterialsManager
from src.BricksManager import BricksManager
from src.Brick import Brick


class MyTestCase(unittest.TestCase):
    def test_load_bricks(self):
        bm = BricksManager()

        first_brick = Brick(
            brick_id=1001,
            quantity=30,
            raw_material_used=20,
            cost=100,
        )
        second_brick = Brick(
            brick_id=1002,
            quantity=15,
            raw_material_used=30,
            cost=80,
        )

        bm.load_bricks(first_brick)
        bm.load_bricks(second_brick)
        self.assertEqual(2, len(bm.get_bricks()))

    def test_load_materials(self):
        mm = MaterialsManager()

        first_material = Material(
            material_id=1,
            characteristics="Material refractario",
            quantity_used=10,
            additional_cost=50,
        )
        second_material = Material(
            material_id=2,
            characteristics="Material común",
            quantity_used=5,
            additional_cost=20,
        )

        mm.load_materials(first_material)
        mm.load_materials(second_material)

        self.assertEqual(2, len(mm.get_materials()))

    def test_loads_bricks_in_materials(self):
        mm = MaterialsManager()

        first_material = Material(
            material_id=1,
            characteristics="Material refractario",
            quantity_used=10,
            additional_cost=50,
        )
        second_material = Material(
            material_id=2,
            characteristics="Material común",
            quantity_used=5,
            additional_cost=20,
        )
        first_brick = Brick(
            brick_id=1001,
            quantity=30,
            raw_material_used=20,
            cost=100,
        )
        second_brick = Brick(
            brick_id=1002,
            quantity=15,
            raw_material_used=30,
            cost=80,
        )

        first_material.add_brick(first_brick)
        second_material.add_brick(second_brick)

        mm.load_materials(first_material)
        mm.load_materials(second_material)

        self.assertEqual(1, len(mm.get_materials()[0].get_bricks()))
        self.assertEqual(1, len(mm.get_materials()[1].get_bricks()))

    def test_loads_materials_in_bricks(self):
        bm = BricksManager()

        first_material = Material(
            material_id=1,
            characteristics="Material refractario",
            quantity_used=10,
            additional_cost=50,
        )
        second_material = Material(
            material_id=2,
            characteristics="Material común",
            quantity_used=5,
            additional_cost=20,
        )
        first_brick = Brick(
            brick_id=1001,
            quantity=30,
            raw_material_used=20,
            cost=100,
        )
        second_brick = Brick(
            brick_id=1002,
            quantity=15,
            raw_material_used=30,
            cost=80,
        )

        first_brick.add_material(first_material)
        second_brick.add_material(second_material)

        bm.load_bricks(first_brick)
        bm.load_bricks(second_brick)

        self.assertIsNotNone(bm.get_bricks()[0].get_material())
        self.assertIsNotNone(bm.get_bricks()[1].get_material())

    def test_calculate_unitary_cost(self):
        mm = MaterialsManager()
        bm = BricksManager()

        first_material = Material(
            material_id=1,
            characteristics="Material refractario",
            quantity_used=10,
            additional_cost=50,
        )
        first_brick = Brick(
            brick_id=1001,
            quantity=30,
            raw_material_used=20,
            cost=100,
        )

        first_material.add_brick(first_brick)
        first_brick.add_material(first_material)

        mm.load_materials(first_material)
        bm.load_bricks(first_brick)
        expected_total = (20*50)+100
        self.assertEqual(expected_total, bm.calculate_unitary_cost(0))

    def test_get_brick_cost(self):
        mm = MaterialsManager()
        bm = BricksManager()

        first_material = Material(
            material_id=1,
            characteristics="Material refractario",
            quantity_used=10,
            additional_cost=50,
        )
        second_material = Material(
            material_id=2,
            characteristics="Material común",
            quantity_used=5,
            additional_cost=20,
        )
        first_brick = Brick(
            brick_id=1001,
            quantity=30,
            raw_material_used=20,
            cost=100,
        )
        second_brick = Brick(
            brick_id=1002,
            quantity=15,
            raw_material_used=30,
            cost=80,
        )

        first_material.add_brick(first_brick)
        second_material.add_brick(second_brick)
        first_brick.add_material(first_material)
        second_brick.add_material(second_material)

        mm.load_materials(first_material)
        mm.load_materials(second_material)
        bm.load_bricks(first_brick)
        bm.load_bricks(second_brick)

        expected_total = (20*50)+100
        self.assertEqual(expected_total, bm.get_brick_cost(1001))

    def test_get_brick_order_cost(self):
        mm = MaterialsManager()
        bm = BricksManager()

        first_material = Material(
            material_id=1,
            characteristics="Material refractario",
            quantity_used=10,
            additional_cost=50,
        )
        second_material = Material(
            material_id=2,
            characteristics="Material común",
            quantity_used=5,
            additional_cost=20,
        )
        first_brick = Brick(
            brick_id=1001,
            quantity=30,
            raw_material_used=20,
            cost=100,
        )
        second_brick = Brick(
            brick_id=1002,
            quantity=15,
            raw_material_used=30,
            cost=80,
        )

        first_material.add_brick(first_brick)
        second_material.add_brick(second_brick)
        first_brick.add_material(first_material)
        second_brick.add_material(second_material)

        mm.load_materials(first_material)
        mm.load_materials(second_material)
        bm.load_bricks(first_brick)
        bm.load_bricks(second_brick)
        budget: dict = {}

        for i in range(len(self.__bricks)):
            budget[i] = self.calculate_unitary_cost(i) * quantity

        return budget


if __name__ == '__main__':
    unittest.main()
