class Registration:
    __date: str
    __employee: object
    __training: object

    def __init__(self,
                 date: str,
                 employee,
                 training,
                 ):
        self.__date = date
        self.__employee = employee
        self.__training = training

    def get_date(self):
        return self.__date

    def get_employee(self):
        return self.__employee

    def set_employee(self, employee):
        self.__employee = employee

    def get_training(self):
        return self.__training

    def set_training(self, training):
        self.__training = training
