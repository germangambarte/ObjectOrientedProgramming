class Transaccion:
    __cvu: str
    __nro_transaccion: str
    __importe: float
    __tipo: str

    def __init__(
        self, cvu: str, nro_transaccion: str, importe: float, tipo: str
    ) -> None:
        self.__cvu = cvu
        self.__nro_transaccion = nro_transaccion
        self.__importe = importe
        self.__tipo = tipo

    def get_cvu(self):
        return self.__cvu

    def get_nro_transaccion(self):
        return self.__nro_transaccion

    def get_importe(self):
        return self.__importe

    def get_tipo(self):
        return self.__tipo
