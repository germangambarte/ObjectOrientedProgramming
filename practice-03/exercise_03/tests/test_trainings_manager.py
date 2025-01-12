import unittest
from src.Training import Training
from src.TrainingsManager import TrainingsManager


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.trainings_manager = TrainingsManager()

        cls.training1 = Training("Python Basic", "PY101", 40)
        cls.training2 = Training("Java Basic", "JV101", 40)

    def test_add_training(self):
        self.trainings_manager.add_training(self.training1)
        self.trainings_manager.add_training(self.training2)

        self.assertEqual(2, len(self.trainings_manager.get_trainings()))


if __name__ == '__main__':
    unittest.main()
