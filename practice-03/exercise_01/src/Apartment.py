class Apartment:
    __apartment_id: int
    __proprietary: str
    __floor: int
    __apartment: int
    __rooms_count: int
    __baths_count: int
    __covered_area: float

    def __init__(self,
                 apartment_id: int,
                 proprietary: str,
                 floor: int,
                 apartment: int,
                 rooms_count: int,
                 baths_count: int,
                 covered_area: float,
                 ):
        self.__apartment_id = apartment_id
        self.__proprietary = proprietary
        self.__floor = floor
        self.__apartment = apartment
        self.__rooms_count = rooms_count
        self.__baths_count = baths_count
        self.__covered_area = covered_area

    def get_proprietary(self):
        return self.__proprietary
    def get_covered_area(self):
        return self.__covered_area
    def get_floor(self):
        return self.__floor
    def get_rooms_count(self):
        return self.__rooms_count
    def get_baths_count(self):
        return self.__baths_count