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
        cls.trainings_manager = TrainingsManager()
        cls.registrations_manager = RegistrationsManager()

        cls.employee1 = Employee("Juan Pérez", 1, "Developer")
        cls.employee2 = Employee("María García", 2, "Analyst")
        cls.employee3 = Employee("Germán Gambarte", 3, "Developer")
        cls.employee4 = Employee("Micaela Farias", 4, "Analyst")
        cls.employee5 = Employee("José Videla", 5, "Analyst")
        cls.employee6 = Employee("Fernanda Flores", 6, "Analyst")

        cls.training1 = Training("Python Basic", "PY101", 40)
        cls.training2 = Training("Java Basic", "JV101", 40)

        cls.registration1 = Registration("11-01-2025", cls.employee1, cls.training1)
        cls.registration2 = Registration("11-01-2025", cls.employee1, cls.training2)
        cls.registration3 = Registration("11-01-2025", cls.employee2, cls.training1)
        cls.registration4 = Registration("11-01-2025", cls.employee3, cls.training1)
        cls.registration5 = Registration("11-01-2025", cls.employee4, cls.training1)
        cls.registration6 = Registration("11-01-2025", cls.employee4, cls.training2)

        cls.employees_manager.add_employee(cls.employee1)
        cls.employees_manager.add_employee(cls.employee2)
        cls.employees_manager.add_employee(cls.employee3)
        cls.employees_manager.add_employee(cls.employee4)
        cls.employees_manager.add_employee(cls.employee5)
        cls.employees_manager.add_employee(cls.employee6)

        cls.trainings_manager.add_training(cls.training1)
        cls.trainings_manager.add_training(cls.training2)

        cls.registrations_manager.add_registration(cls.registration1)
        cls.registrations_manager.add_registration(cls.registration2)
        cls.registrations_manager.add_registration(cls.registration3)
        cls.registrations_manager.add_registration(cls.registration4)
        cls.registrations_manager.add_registration(cls.registration5)
        cls.registrations_manager.add_registration(cls.registration6)

    def set_empty_registrations(self):
        self.registrations_manager.set_registrations([])

    def test_add_registration(self):
        self.set_empty_registrations()

        self.registrations_manager.add_registration(self.registration1)
        self.registrations_manager.add_registration(self.registration2)
        self.registrations_manager.add_registration(self.registration3)
        self.registrations_manager.add_registration(self.registration4)
        self.registrations_manager.add_registration(self.registration5)
        self.registrations_manager.add_registration(self.registration6)

        self.assertEqual(6, len(self.registrations_manager.get_registrations()))

    def test_get_duration_of_trainings_by_employee(self):
        durations = self.registrations_manager.get_duration_of_trainings_by_employee(1)
        total = 0
        for k, duration in durations.items():
            total += duration

        self.assertEqual(80, total)

    def test_get_registered_employees_by_training(self):
        actual_registered_employees = self.registrations_manager.get_registered_employees_by_training("Python Basic")
        expected_registered_names = ["Juan Pérez", "María García", "Germán Gambarte", "Micaela Farias"]
        self.assertEqual(expected_registered_names, actual_registered_employees)

    def test_get_employees_without_registrations(self):
        all_employees = self.employees_manager.get_employees()
        actual_non_registered_names = self.registrations_manager.get_employees_without_registrations(all_employees)
        expected_non_registered_names = ["José Videla", "Fernanda Flores"]
        self.assertEqual(expected_non_registered_names, actual_non_registered_names)


if __name__ == '__main__':
    unittest.main()
