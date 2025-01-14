from src.Heater import Heater


class ElectricHeater(Heater):
    __max_power: str

    def __init__(self,
                 brand: str,
                 model: str,
                 manufacture_country: str,
                 list_price: float,
                 payment_method: str,
                 installments_number: int,
                 in_promotion: bool,
                 max_power: str
                 ):
        super().__init__(
            brand,
            model,
            manufacture_country,
            list_price,
            payment_method,
            installments_number,
            in_promotion
        )
        self.__max_power = max_power

    def get_max_power(self):
        return self.__max_power

    def calculate_final_cost(self):
        list_price = super().get_list_price()
        total = list_price * 0.15
        if self.__max_power > 1000:
            total += list_price * .01

        if super().get_payment_method() == "installment":
            total += list_price * .30