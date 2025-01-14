# import json
# import os
#
#
# class ObjectEncoder:
#     __file_path = os.path.join(os.path.dirname(__file__), "heaters.json")
#
#     @staticmethod
#     def dictionary_decoder(some_dict):
#         if '__class__' not in some_dict:
#             return some_dict
#         else:
#             custom_list = None
#             custom_list_class_name = some_dict['__class__']
#             custom_list_class = eval(custom_list_class_name)
#             if custom_list_class_name == 'List':
#                 heaters = some_dict['heaters']
#                 heat_item = heaters[0]
#                 custom_list = custom_list_class()
#                 for i in range(len(heaters)):
#                     heat_item = heaters[i]
#                     custom_list_class_name = heat_item.pop('__class__')
#                     custom_list_class = eval(custom_list_class_name)
#                     heat_attributes = heat_item['__attributes__']
#                     new_heater = custom_list_class(**heat_attributes)
#                     custom_list.add_new_heater(new_heater)
#             return custom_list
#
#     @staticmethod
#     def save_json(self, some_dict):
#         with open(self.__file_path, "w", encoding="UTF-8") as file:
#             return json.dump(some_dict, file, indent=4)
#
#     @staticmethod
#     def read_json(self):
#         with open(self.__path_file, encoding="UTF-8") as file:
#             return json.load(file)
#
#     @staticmethod
#     def dict_to_text(self, text):
#         return json.loads(text)
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

    def save_json(self, some_dict):
        """
        Guarda un diccionario como un archivo JSON en la ruta especificada.
        :param some_dict: Diccionario a guardar.
        """
        with open(self.__file_path, "w", encoding="UTF-8") as file:
            json.dump(some_dict, file, indent=4)

    def read_json(self):
        """
        Lee un archivo JSON desde la ruta especificada y devuelve su contenido como un diccionario.
        """
        with open(self.__file_path, encoding="UTF-8") as file:
            return json.load(file)

    @staticmethod
    def dict_to_text(text):
        """
        Convierte un texto en formato JSON a un diccionario.
        :param text: Texto JSON.
        :return: Diccionario.
        """
        return json.loads(text)

if __name__ == "__main__":
    # Crear una instancia de ObjectEncoder
    encoder = ObjectEncoder()

    # Leer el JSON desde el archivo y decodificarlo
    print("Leyendo JSON...")
    data = encoder.read_json()
    print("Datos originales del archivo JSON:")
    print(data)

    # Decodificar el JSON a objetos Python
    print("\nDecodificando datos a objetos...")
    decoded_obj = encoder.dictionary_decoder(data)
    print("Objeto decodificado:")
    print(decoded_obj)

    # Modificar el objeto y volverlo a guardar como JSON
    # print("\nAgregando un nuevo Heater...")
    # new_heater = Heater(brand="LG", power=1800)
    # decoded_obj.add_new_heater(new_heater)
    # print("Objeto actualizado:")
    # print(decoded_obj)
    #
    # # Guardar los datos actualizados en el archivo JSON
    # print("\nGuardando el objeto actualizado en JSON...")
    # encoder.save_json(decoded_obj.__dict__)
    # print("Guardado exitosamente. Verifica el archivo JSON.")

