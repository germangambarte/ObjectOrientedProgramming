from src.Node import Node
from src.Book import Book
from src.CompactDisk import CompactDisk


class LinkedList:
    __head: Node | None
    __current: Node | None
    __index: int
    __stop: int

    def __init__(self,
                 ):
        self.__head = None
        self.__current = None
        self.__index = 0
        self.__stop = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.__index >= self.__stop:
            self.__current = self.__head
            self.__index = 0
            raise StopIteration
        post = self.__current.get_post()
        self.__current = self.__current.get_next()
        self.__index += 1
        return post

    def add_post(self, post):
        new_node = Node(post)
        new_node.set_next(self.__head)
        self.__head = new_node
        self.__current = new_node
        self.__stop += 1

    def get_post_type(self, index):
        self.reset_list_index()

        if 0 > index or index > self.__stop:
            return None

        while self.__index != index:
            self.__current = self.__current.get_next()
            self.__index += 1

        post = self.__current.get_post()
        if isinstance(post, Book):
            return "Book"
        else:
            return "Compact Disk"

    def get_items_quantity(self):
        self.reset_list_index()
        book_quantity = 0
        compact_disks_quantity = 0

        while self.__index < self.__stop and self.__current is not None:
            if isinstance(self.__current.get_post(), Book):
                book_quantity += 1
            else:
                compact_disks_quantity += 1
            self.__current = self.__current.get_next()
            self.__index += 1

        return book_quantity, compact_disks_quantity

    def show_post_data(self):
        self.reset_list_index()

        while self.__index < self.__stop:
            post = self.__current.get_post()
            print(f"título: {post.get_title()}, categoría: {post.get_category()}, import: ${post.get_selling_price():2f}")

            self.__current = self.__current.get_next()
            self.__index += 1

    def reset_list_index(self):
        self.__current = self.__head
        self.__index = 0
