from src.Material import Material


class MaterialsManager:
    __materials: [Material]

    def __init__(self):
        self.__materials = []

    def load_materials(self,material:Material):
        self.__materials.append(material)

    def get_materials(self):
        return self.__materials