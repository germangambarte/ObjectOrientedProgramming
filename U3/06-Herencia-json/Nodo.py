from typing import Optional

from Calefactor_Electrico import Calefactor_Electrico
from Calefactor_Gas import Calefactor_Gas


class Nodo:
    __calefactor: Calefactor_Electrico | Calefactor_Gas
    __siguiente: Optional["Nodo"]

    def __init__(self, calefactor) -> None:
        self.__calefactor = calefactor
        # self.__siguiente = None

    def set_siguiente(self, siguiente):
        self.__siguiente = siguiente

    def get_siguiente(self):
        return self.__siguiente

    def get_calefactor(self):
        return self.__calefactor
