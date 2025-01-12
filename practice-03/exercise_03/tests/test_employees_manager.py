import unittest
from src.Employee import Employee
from src.EmployeesManager import EmployeesManager
from src.Training import Training
from src.TrainingsManager import TrainingsManager
from src.Registration import Registration
from src.RegistrationsManager import RegistrationsManager


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.employees_manager = EmployeesManager()

        cls.employee1 = Employee("Juan Pérez", 1, "Developer")
        cls.employee2 = Employee("María García", 2, "Analyst")
        cls.employee3 = Employee("Germán Gambarte", 3, "Developer")
        cls.employee4 = Employee("Micaela Farias", 4, "Analyst")
        cls.employee5 = Employee("José Videla", 5, "Analyst")
        cls.employee6 = Employee("Fernanda Flores", 6, "Analyst")

    def test_add_employee(self):
        self.employees_manager.add_employee(self.employee1)
        self.employees_manager.add_employee(self.employee2)
        self.employees_manager.add_employee(self.employee3)
        self.employees_manager.add_employee(self.employee4)
        self.employees_manager.add_employee(self.employee5)
        self.employees_manager.add_employee(self.employee6)

        self.assertEqual(6, len(self.employees_manager.get_employees()))


if __name__ == '__main__':
    unittest.main()
