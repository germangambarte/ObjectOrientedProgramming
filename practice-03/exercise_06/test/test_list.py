import unittest

from src.ElectricHeater import ElectricHeater
from src.GasHeater import GasHeater
from src.List import List
from utils.ObjectEncoder import ObjectEncoder


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.encoder = ObjectEncoder()
        cls.data = cls.encoder.read_json()
        cls.list = cls.encoder.dictionary_decoder(cls.data)

        cls.new_electric_heater = ElectricHeater(
            brand="Propia",
            model="acb123",
            manufacture_country="Argentina",
            list_price=123,
            payment_method="cash",
            installments_number=None,
            in_promotion=True,
            max_power=4000,
        )

        cls.new_gas_heater = GasHeater(
            brand="Propia",
            model="acb123",
            manufacture_country="Argentina",
            list_price=123,
            payment_method="cash",
            in_promotion=True,
            installments_number=None,
            registration="bcd234",
            calories=4000,
        )
    def setUp(self):
        self.encoder = ObjectEncoder()
        self.data = self.encoder.read_json()
        self.list = self.encoder.dictionary_decoder(self.data)

    def test_insert_heater(self):
        self.list.insert_heater_modified(2, self.new_gas_heater)

        actual_heater = self.list.get_item_by_index(2)
        self.assertEqual(self.new_gas_heater.get_model(), actual_heater.get_model(), "test_insert_heater")

    def test_add_new_heater(self):
        self.list.add_new_heater(self.new_gas_heater)

        actual_heater = self.list.get_item_by_index(0)
        self.assertEqual(self.new_gas_heater.get_model(), actual_heater.get_model(), "test_insert_heater")

    def test_get_heater_type(self):

        actual_heater_type = self.list.get_heater_type(2)
        expected_gas_heater = "Calefactor a Gas"

        self.assertEqual(expected_gas_heater, actual_heater_type)

        actual_heater_type = self.list.get_heater_type(3)
        expected_electric_heater = "Calefactor Eléctrico"

        self.assertEqual(expected_electric_heater, actual_heater_type)

    def test_get_lower_price_gas_heater(self):
        self.list.insert_heater_modified(5, self.new_gas_heater)
        actual_lower_price = self.list.get_lower_price_gas_heater()
        expected_lower_price = 19.68
        self.assertEqual(expected_lower_price, actual_lower_price)

    def test_get_heater_by_brand(self):
        actual_heaters = self.list.get_heater_by_brand("Frigidaire")
        expected_heaters_count = 3
        self.assertEqual(expected_heaters_count, len(actual_heaters))

    def test_get_in_promotion_heaters(self):
        actual_in_promotion_heaters = self.list.get_in_promotion_heaters()
        expected_in_promotion_heaters_count = 4
        self.assertEqual(expected_in_promotion_heaters_count,len(actual_in_promotion_heaters))


if __name__ == '__main__':
    unittest.main()
