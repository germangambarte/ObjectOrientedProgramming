from abc import ABC, abstractmethod


class Post(ABC):
    __title: str
    __category: str
    __base_price: float

    def __init__(self,
                 title: str,
                 category: str,
                 base_price: float,
                 ):
        self.__title = title
        self.__category = category
        self.__base_price = base_price

    def get_title(self):
        return self.__title

    def get_category(self):
        return self.__category

    def get_base_price(self):
        return self.__base_price

    @abstractmethod
    def get_selling_price(self):
        pass
