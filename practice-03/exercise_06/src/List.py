from src.Node import Node
from src.Heater import Heater
from src.ElectricHeater import ElectricHeater
from src.GasHeater import GasHeater


class List:
    __head: Node | None
    __current: Node | None
    __index: int
    __last: int

    def __init__(self):
        self.__head = None
        self.__current = None
        self.__index = 0
        self.__last = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.__index == self.__last:
            self.__index = 0
            self.__current = self.__head
            raise StopIteration

        heater = self.__current.get_heater()
        self.__index += 1
        self.__current = self.__current.get_next_heater()

        return heater

    # item 1
    def insert_heater_theory(self, index: int, heater: Heater):
        if index < 0 or index > self.__last:
            raise IndexError("Índice no válido.")

        new_node = Node(heater)

        if self.__head is None:
            self.__head = new_node
            self.__current = self.__head
        elif index == 0:
            new_node.set_next_heater(self.__head)
            self.__head = new_node
        else:
            self.__reset_list()
            while self.__index < index - 1:
                self.__current = self.__current.get_next_heater()
                self.__index += 1

            new_node.set_next_heater(self.__current.get_next_heater())
            self.__current.set_next_heater(new_node)
        self.__last += 1

    def insert_heater_modified(self, index: int, heater: Heater):
        if index < 0 or index > self.__last:
            raise IndexError("Índice no válido.")

        new_node = Node(heater)

        if self.__head is None or index == 0:
            self.add_new_heater(heater)
        else:
            self.__reset_list()
            while self.__index < index - 1:
                self.__current = self.__current.get_next_heater()
                self.__index += 1

            new_node.set_next_heater(self.__current.get_next_heater())
            self.__current.set_next_heater(new_node)
        self.__last += 1

    # item 2
    def add_new_heater(self, heater: Heater):
        new_node = Node(heater)
        new_node.set_next_heater(self.__head)
        self.__head = new_node
        self.__last += 1

    # item 3
    def get_heater_type(self, index):
        if index < 0 or index > self.__last:
            raise IndexError("Índice vo válido")

        self.__reset_list()

        while self.__index < index:
            self.__current = self.__current.get_next_heater()
            self.__index += 1

        if isinstance(self.__current.get_heater(), ElectricHeater):
            return "Calefactor Eléctrico"
        else:
            return "Calefactor a Gas"

    # item 4
    def get_lower_price_gas_heater(self):
        self.__reset_list()

        min_price = 99999999
        min_heater = None

        for heater in self:
            if isinstance(heater, GasHeater):
                final_cost = heater.calculate_final_cost()
                if final_cost < min_price:
                    min_price = final_cost
                    min_heater = heater

        return min_heater.calculate_final_cost()

    # item 5
    def get_heater_by_brand(self, brand: str):
        self.__reset_list()
        heaters = []

        for heater in self:
            if heater.get_brand() == brand:
                heaters.append(heater)

        return heaters

    # item 6
    def get_in_promotion_heaters(self):
        self.__reset_list()

        heaters = []

        for heater in self:
            if heater.get_in_promotion():
                heaters.append(heater)

        return heaters

    # item 7
    def __reset_list(self):
        self.__index = 0
        self.__current = self.__head

    def show_items(self):
        self.__reset_list()

        while self.__index < self.__last - 1:
            print(self.__current.get_heater().get_brand())
            self.__current = self.__current.get_next_heater()
            self.__index += 1
            # print(isinstance(self.__current.get_heater(), Heater))
        print(self.__current.get_heater().get_brand())

    def get_item_by_index(self, index):
        self.__reset_list()

        while self.__index < index:
            self.__current = self.__current.get_next_heater()
            self.__index += 1
            # print(isinstance(self.__current.get_heater(), Heater))
        return self.__current.get_heater()
