from src.Post import Post
from datetime import datetime
import math


class Book(Post):
    __author: str
    __publication_datetime: datetime
    __quantity_pages: int

    def __init__(self,
                 title: str,
                 category: str,
                 base_price: float,
                 author: str,
                 publication_date: str,
                 quantity_pages: int,
                 ):
        super().__init__(title, category, base_price)
        self.__author = author
        self.__publication_datetime = datetime.strptime(publication_date, "%d-%m-%Y")
        self.__quantity_pages = quantity_pages

    def get_author(self):
        return self.__author

    def get_publication_date(self):
        return self.__publication_datetime

    def get_quantity_pages(self):
        return self.__quantity_pages

    def get_selling_price(self):
        years_since_publication = math.floor((self.__publication_datetime - datetime.now()).days / 365)
        base_price = super().get_base_price()
        return base_price - (base_price * .01) * years_since_publication
