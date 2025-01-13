from src.Post import Post


class CompactDisk(Post):
    __duration: int
    __narrator: str

    def __init__(self,
                 title: str,
                 category: str,
                 base_price: float,
                 duration: int,
                 narrator: str,
                 ):
        super().__init__(title, category, base_price)
        self.__duration = duration
        self.__narrator = narrator

    def get_duration(self):
        return self.__duration

    def get_narrator(self):
        return self.__narrator

    def get_selling_price(self):
        return super().get_base_price() * 1.1
