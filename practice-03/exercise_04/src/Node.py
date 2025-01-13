from src.Post import Post


class Node:
    __post: Post
    __next_post: object

    def __init__(self, post: Post):
        self.__post = post
        self.__next_post = None

    def get_post(self):
        return self.__post

    def get_next(self):
        return self.__next_post

    def set_next(self, next_post):
        self.__next_post = next_post
