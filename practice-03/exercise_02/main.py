# from src.Material import Material
# from src.MaterialsManager import MaterialsManager
# from src.BricksManager import BricksManager
# from src.Brick import Brick
#
#
# def test():
#     mm = MaterialsManager()
#     bm = BricksManager()
#
#     first_material = Material(
#         material_id=1,
#         characteristics="Material refractario",
#         quantity_used=10,
#         additional_cost=50,
#     )
#     second_material = Material(
#         material_id=2,
#         characteristics="Material común",
#         quantity_used=5,
#         additional_cost=20,
#     )
#     first_brick = Brick(
#         brick_id=1001,
#         quantity=30,
#         raw_material_used=20,
#         cost=100,
#     )
#     second_brick = Brick(
#         brick_id=1002,
#         quantity=15,
#         raw_material_used=30,
#         cost=80,
#     )
#
#     first_material.add_brick(first_brick)
#     second_material.add_brick(second_brick)
#     first_brick.add_material(first_material)
#     second_brick.add_material(second_material)
#
#     mm.load_materials(first_material)
#     mm.load_materials(second_material)
#     bm.load_bricks(first_brick)
#     bm.load_bricks(second_brick)
