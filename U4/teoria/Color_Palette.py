class Color_Palette:
    __bg: str
    __fg: str
    __bg_2: str
    __fg_2: str
    __red: str
    __green: str
    __blue: str
    __yellow: str
    __magenta: str
    __cyan: str

    def __init__(self) -> None:
        self.__fg = "#cdd6f4"
        self.__bg = "#1e1e2e"
        self.__bg_2 = "#e6e9ef"
        self.__fg_2 = "#4c4f69"
        self.__red = "#f38ba8"
        self.__green = "#94e2d5"
        self.__blue = "#89b4fa"
        self.__yellow = "#f2cdcd"
        self.__magenta = "#f5c2e7"
        self.__cyan = "#89dceb"

    def get_bg(self):
        return self.__bg

    def get_fg(self):
        return self.__fg

    def get_bg_2(self):
        return self.__bg_2

    def get_fg_2(self):
        return self.__fg_2

    def get_red(self):
        return self.__red

    def get_green(self):
        return self.__green

    def get_blue(self):
        return self.__blue

    def get_yellow(self):
        return self.__yellow

    def get_cyan(self):
        return self.__cyan

    def get_magenta(self):
        return self.__magenta
