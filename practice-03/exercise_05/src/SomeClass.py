from src.Interface import Interface


class SomeClass(Interface):
    __elements: []

    def __init__(self):
        self.__elements = []

    def insert_element(self, index: int, new_element: object):
        if 0 > index or index > len(self.__elements):
            raise IndexError("Índice no válido")

        self.__elements.append(None)

        for i in range(len(self.__elements) - 1, index, -1):
            self.__elements[i] = self.__elements[i - 1]

        self.__elements[index] = new_element

    def add_element(self, new_element: int):
        self.__elements.append(new_element)

    def show_element(self, index: int):
        if 0 > index or index > len(self.__elements):
            raise IndexError("Índice no válido")

        print(f"element[{index}]: {self.__elements[index]}")

    def show_elements(self):
        for item in self.__elements:
            print(item)


if __name__ == "__main__":
    sc = SomeClass()

    sc.add_element(1)
    sc.add_element(2)
    sc.add_element(3)
    sc.add_element(4)

    sc.insert_element(2, 7)
    sc.insert_element(0, 9)

    sc.show_element(2)
    sc.show_elements()
