class Employee:
    __full_name: str
    __employee_id: int
    __position: str
    __trainings: [object]

    def __init__(self,
                 full_name: str,
                 employee_id: int,
                 position: str,
                 ):
        self.__full_name = full_name
        self.__employee_id = employee_id
        self.__position = position
        self.__trainings = []

    def get_trainings(self):
        return self.__trainings

    def add_training(self, training: object):
        self.__trainings.append(training)

    def get_full_name(self):
        return self.__full_name

    def get_employee_id(self):
        return self.__employee_id

    def get_position(self):
        return self.__position
