from src.Heater import Heater


class GasHeater(Heater):
    __registration: str
    __calories: int

    def __init__(self,
                 brand: str,
                 model: str,
                 manufacture_country: str,
                 list_price: float,
                 payment_method: str,
                 installments_number: int,
                 in_promotion: bool,
                 registration: str,
                 calories: int,
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
        self.__registration = registration
        self.__calories = calories

    def get_registration(self):
        return self.__registration

    def get_calories(self):
        return self.__calories

    def calculate_final_cost(self):
        list_price = super().get_list_price()
        total_price = list_price * 0.15

        if self.get_calories() > 3000:
            total_price += list_price * 0.01

        if super().get_payment_method() == "installment":
            total_price += list_price * 0.40