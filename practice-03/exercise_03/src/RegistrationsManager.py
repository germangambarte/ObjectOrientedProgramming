from src.Registration import Registration


class RegistrationsManager:
    __registrations: [Registration]

    def __init__(self, registration=None):
        if registration is None:
            self.__registrations = []
        else:
            self.__registrations = []
            self.__registrations.append(registration)

    def get_registrations(self):
        return self.__registrations

    def set_registrations(self, value):
        self.__registrations = value

    def add_registration(self, registration):
        self.__registrations.append(registration)

    def get_duration_of_trainings_by_employee(self, employee_id):
        durations = {}
        for registration in self.__registrations:
            employee = registration.get_employee()
            if employee.get_employee_id() == employee_id:
                training = registration.get_training()
                durations[training.get_name()] = training.get_duration()
        return durations

    def get_registered_employees_by_training(self, training_name):
        employees = []
        for registration in self.__registrations:
            training = registration.get_training()
            if training.get_name() == training_name:
                employees.append(registration.get_employee().get_full_name())
        return employees

    def get_registered_employee_names(self):
        employees = []
        for registration in self.__registrations:
            employees.append(registration.get_employee().get_full_name())
        return employees

    def get_employees_without_registrations(self, all_employees):
        not_registered_employees = []
        registered_employee_names = self.get_registered_employee_names()
        for employee in all_employees:
            employee_name = employee.get_full_name()
            if employee_name not in registered_employee_names and employee_name not in not_registered_employees:
                not_registered_employees.append(employee_name)

        return not_registered_employees
