import unittest
from src.BuildingsManager import BuildingsManager


class Test(unittest.TestCase):
    def test_load_buildings(self):
        bm = BuildingsManager()
        bm.load_buildings()
        buildings = bm.get_buildings()
        self.assertEqual(2, len(buildings))

        apartments_count = buildings[0].get_apartments_count()
        self.assertEqual(6, apartments_count)

        apartments_count = buildings[1].get_apartments_count()
        self.assertEqual(6, apartments_count)

    def test_show_proprietaries_name(self):
        bm = BuildingsManager()
        bm.load_buildings()
        names = bm.show_proprietaries_name()

        self.assertEqual(12, len(names))

    def test_total_area_by_building(self):
        bm = BuildingsManager()
        bm.load_buildings()
        actual_area = bm.show_total_area_by_building(1)
        expected_area = 70 + 61 + 65.5 + 70 + 70 + 70

        self.assertEqual(expected_area, actual_area)

    def test_apartments_count_by_floor(self):
        bm = BuildingsManager()
        bm.load_buildings()

        actual_count = bm.apartments_count_by_floor(2)
        expected_count = 4

        self.assertEqual(expected_count, actual_count)
