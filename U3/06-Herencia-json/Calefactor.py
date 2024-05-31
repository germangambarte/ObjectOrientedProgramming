from abc import abstractmethod


class Calefactor:
    __modelo: str
    __precio_lista: float
    __forma_pago: str
    __cant_cuotas: int
    __promocion: str

    def __init__(
        self,
        modelo: str,
        precio_lista: float,
        forma_pago: str,
        cant_cuotas: int,
        promocion: str,
    ) -> None:
        self.__modelo = modelo
        self.__precio_lista = precio_lista
        self.__forma_pago = forma_pago
        self.__cant_cuotas = cant_cuotas
        self.__promocion = promocion

    def get_modelo(self):
        return self.__modelo

    def get_precio_lista(self):
        return self.__precio_lista

    def get_forma_pago(self):
        return self.__forma_pago

    def get_cant_cuotas(self):
        return self.__cant_cuotas

    def get_promocion(self):
        return self.__promocion

    @abstractmethod
    def get_importe(self) -> float:
        pass

    @abstractmethod
    def toJSON(self) -> dict:
        pass
