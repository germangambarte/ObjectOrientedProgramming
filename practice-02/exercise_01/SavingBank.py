class SavingBank:
    __account_number: str
    __cuil: str
    __last_name: str
    __first_name: str
    __balance: float

    def __init__(
            self,
            account_number: str,
            cuil: str,
            last_name: str,
            first_name: str,
            balance: float,
    ) -> None:
        self.__account_number = account_number
        self.__cuil = cuil
        self.__last_name = last_name
        self.__first_name = first_name
        self.__balance = balance

    def show_data(self) -> None:

        print(f"""
            __account_number= {self.__account_number}
            __cuil= {self.__cuil}
            __last_name= {self.__last_name}
            __first_name= {self.__first_name}
            __balance= {self.__balance}
        """)

    def extract(self, amount: float) -> float:
        if self.__balance == 0 or self.__balance < amount:
            return -1
        self.__balance -= amount
        return self.__balance

    def deposit(self, amount: float) -> float:
        if amount < 0:
            return -1
        self.__balance += amount
        return self.__balance

    def validate_cuil(self, cuil: str = None) -> bool:
        if cuil is None:
            cuil = self.__cuil

        genre = int(cuil[:2])
        verification_digit = int(cuil[-1])
        factors = [5, 4, 3, 2, 7, 6, 5, 4, 3, 2]

        if len(cuil) != 11:
            return False

        if not genre in [20, 23, 27, 30]:
            return False

        sum = 0

        for i in range(0, 10):
            sum += int(cuil[i]) * factors[i]

        rest = sum % 11

        if rest == 0 == verification_digit:
            return True

        if rest == 1:
            if genre == 23:
                return verification_digit in [9, 4]

        return 11 - rest == verification_digit

    def get_cuil(self):
        return self.__cuil

    def get_last_name(self):
        return self.__last_name

    def get_first_name(self):
        return self.__first_name

    def get_balance(self):
        return self.__balance

