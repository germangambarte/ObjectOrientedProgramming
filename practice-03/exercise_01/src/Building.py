from src.Apartment import Apartment


class Building:
    __building_id: int
    __name: str
    __address: str
    __construction_company: str
    __floors_count: int
    __apartments_count: int
    __apartments: [Apartment]

    def __init__(self,
                 building_id: int,
                 name: str,
                 address: str,
                 construction_company: str,
                 floors_count: int,
                 apartment_count: int
                 ):
        self.__building_id = building_id
        self.__name = name
        self.__address = address
        self.__construction_company = construction_company
        self.__floors_count = floors_count
        self.__apartments_count = apartment_count
        self.__apartments = []

    def add_apartment(self, apartment: Apartment):
        self.__apartments.append(apartment)
        if self.__apartments_count < len(self.__apartments):
            self.__apartments_count += 1

    def get_building_id(self):
        return self.__building_id

    def get_name(self):
        return self.__name

    def get_apartments_count(self):
        return len(self.__apartments)

    def get_apartments(self):
        return self.__apartments
