class Training:
    __name: str
    __code: str
    __duration: int

    def __init__(self,
                 name: str,
                 code: str,
                 duration: int,
                 ):
        self.__name = name
        self.__code = code
        self.__duration = duration

    def get_name(self):
        return self.__name

    def get_code(self):
        return self.__code

    def get_duration(self):
        return self.__duration
