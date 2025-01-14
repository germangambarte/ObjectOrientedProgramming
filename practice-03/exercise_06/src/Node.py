from src.Heater import Heater


class Node:
    __heater: Heater
    __next_heater: object

    def __init__(self,
                 heater: Heater
                 ):
        self.__heater = heater
        self.__next_heater = None

    def get_heater(self):
        return self.__heater

    def get_next_heater(self):
        return self.__next_heater

    def set_next_heater(self, next):
        self.__next_heater = next
