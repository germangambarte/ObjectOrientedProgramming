import json
import os
from src.List import List
from src.ElectricHeater import ElectricHeater
from src.GasHeater import GasHeater

CLASS_MAP = {
    'List': List,
    'GasHeater': GasHeater,
    'ElectricHeater': ElectricHeater,
}


class ObjectEncoder:
    def __init__(self):
        self.__file_path = os.path.join(os.path.dirname(__file__), "../src/heaters.json")

    @staticmethod
    def dictionary_decoder(some_dict):
        if '__class__' not in some_dict:
            return some_dict

        class_name = some_dict['__class__']
        class_type = CLASS_MAP.get(class_name)
        if not class_type:
            raise ValueError(f"Clase {class_name} no reconocida.")

        if class_name == 'List':
            heaters = some_dict['heaters']
            custom_list = class_type()
            for heater_dict in heaters:
                heater_class_name = heater_dict.pop('__class__')
                heater_class = CLASS_MAP.get(heater_class_name)
                if not heater_class:
                    raise ValueError(f"Clase {heater_class_name} no reconocida.")
                attributes = heater_dict['__attributes__']
                custom_list.add_new_heater(heater_class(**attributes))
            return custom_list

        return class_type(**some_dict['__attributes__'])

    @staticmethod
    def dict_to_text(text):
        return json.loads(text)

    def save_json(self, some_dict):
        with open(self.__file_path, "w", encoding="UTF-8") as file:
            json.dump(some_dict, file, indent=4)

    def read_json(self):
        with open(self.__file_path, encoding="UTF-8") as file:
            return json.load(file)


