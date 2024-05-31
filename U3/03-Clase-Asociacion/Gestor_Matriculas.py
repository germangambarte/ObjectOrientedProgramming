# from Matricula import Matricula


class Gestor_Matriculas:
    __matriculas: list[object]

    def __init__(self) -> None:
        self.__matriculas = []

    def agregar_matricula(self, matricula: object):
        self.__matriculas.append(matricula)

    def get_matriculas(self):
        return self.__matriculas
