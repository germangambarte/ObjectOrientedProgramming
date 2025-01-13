from abc import ABC, abstractmethod


class Interface(ABC):
    @abstractmethod
    def add_element(self, new_element: object):
        pass

    @abstractmethod
    def insert_element(self, index: int, new_element: object):
        pass

    @abstractmethod
    def show_element(self, index: int):
        pass
