from src.Employee import Employee


class EmployeesManager:
    __employees: [Employee]

    def __init__(self, employees=[]):
        self.__employees = employees

    def get_employees(self):
        return self.__employees

    def add_employee(self, employee):
        self.__employees.append(employee)
