class Cuenta:
    __apellido: str
    __nombre: str
    __dni: str
    __tel: str
    __saldo: float
    __cvu: str
    __porcentaje: float

    def __init__(
        self,
        apellido: str,
        nombre: str,
        dni: str,
        tel: str,
        saldo: float,
        cvu: str,
        porcentaje: float,
    ) -> None:
        self.__apellido = apellido
        self.__nombre = nombre
        self.__dni = dni
        self.__tel = tel
        self.__saldo = saldo
        self.__cvu = cvu
        self.__porcentaje = porcentaje

    def get_apellido(self):
        return self.__apellido

    def get_nombre(self):
        return self.__nombre

    def get_dni(self):
        return self.__dni

    def get_tel(self):
        return self.__tel

    def get_saldo(self):
        return self.__saldo

    def get_cvu(self):
        return self.__cvu

    def get_porcentaje(self):
        return self.__porcentaje
