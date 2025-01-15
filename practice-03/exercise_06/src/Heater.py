from abc import ABC, abstractmethod


class Heater(ABC):
    __brand: str
    __model: str
    __manufacture_country: str
    __list_price: float
    __payment_method: str
    __installments_number: int | None
    __in_promotion: bool

    def __init__(self,
                 brand: str,
                 model: str,
                 manufacture_country: str,
                 list_price: float,
                 payment_method: str,
                 in_promotion: bool,
                 installments_number: int | None = None,
                 ):
        self.__brand = brand
        self.__model = model
        self.__manufacture_country = manufacture_country
        self.__list_price = list_price
        self.__payment_method = payment_method
        self.__installments_number = installments_number
        self.__in_promotion = in_promotion

    def get_brand(self):
        return self.__brand

    def get_model(self):
        return self.__model

    def get_manufacture_country(self):
        return self.__manufacture_country

    def get_list_price(self):
        return self.__list_price

    def get_payment_method(self):
        return self.__payment_method

    def get_installments_number(self):
        return self.__installments_number

    def get_in_promotion(self):
        return self.__in_promotion

    @abstractmethod
    def calculate_final_cost(self):
        pass
