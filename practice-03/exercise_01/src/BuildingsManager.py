import csv
import os.path

from src.Apartment import Apartment
from src.Building import Building


class BuildingsManager:
    __buildings: [Building]
    __file_path = os.path.join(os.path.dirname(__file__), './EdificioNorte.csv')

    def __init__(self):
        self.__buildings = []

    def load_buildings(self):
        with open(self.__file_path, encoding='utf-8') as file:
            reader = csv.reader(file, delimiter=';')
            new_building = None
            for row in reader:
                if len(row) == 7:
                    if new_building is not None:
                        self.__buildings.append(new_building)
                    new_building = Building(
                        building_id=int(row[0]),
                        name=row[1],
                        address=row[2],
                        construction_company=row[3],
                        floors_count=int(row[4]),
                        apartment_count=int(row[5])
                    )
                else:
                    new_apartment = Apartment(
                        apartment_id=int(row[1]),
                        proprietary=row[2],
                        floor=int(row[3]),
                        apartment=int(row[4]),
                        rooms_count=int(row[5]),
                        baths_count=int(row[6]),
                        covered_area=float(row[7])
                    )
                    new_building.add_apartment(new_apartment)

            self.__buildings.append(new_building)

    def show_proprietaries_name(self):
        names: [str] = []
        for building in self.__buildings:
            print(f"Propietarios del {building.get_name()}")
            for apartment in building.get_apartments():
                names.append(apartment.get_proprietary())
                print(f"\t{apartment.get_proprietary()}")
        return names

    def show_total_area_by_building(self, building_id: int):
        total_area: float = 0
        building = self.__buildings[building_id - 1]
        for apartment in building.get_apartments():
            total_area += apartment.get_covered_area()
        return total_area

    def calculate_area_covered_by_proprietary(self, proprietary: str):
        i = 0
        j = 0
        for building in self.__buildings:
            for apartment in building.get_apartments():
                if apartment.get_proprietary() == proprietary:
                    building_area = self.show_total_area_by_building(building.get_building_id())
                    area_percentage = (apartment.get_covered_area() * 100) / building_area
                    return area_percentage

    def apartments_count_by_floor(self, floor: int):
        count = 0
        for building in self.__buildings:
            for apartment in building.get_apartments():
                if (apartment.get_floor() == floor and
                        apartment.get_rooms_count() == 3 and
                        apartment.get_baths_count() > 1):
                    count += 1
        return count

    def get_buildings(self):
        return self.__buildings
