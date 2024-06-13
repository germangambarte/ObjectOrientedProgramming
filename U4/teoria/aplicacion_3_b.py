from tkinter import *
from tkinter import ttk

from Color_Palette import Color_Palette


class Aplicacion:
    __ventana: Tk
    __pulgadas: StringVar
    __centimetros: StringVar

    def __init__(self) -> None:
        palette = Color_Palette()

        # configuracion ventana
        self.__ventana = Tk()
        self.__ventana.geometry("300x150")
        self.__ventana.title("Conversor Pulgadas a Centimetros")
        self.__ventana.configure(bg=palette.get_bg())
        ttk.Style().configure(
            "TFrame", background=palette.get_bg(), foreground=palette.get_fg()
        )

        # crear contenedor
        contenedor = ttk.Frame(
            self.__ventana,
            padding=(10, 10),
            relief="sunken",
            style="TFrame",
        )
        contenedor.grid(column=0, row=0, sticky="nesw")

        # formatear variables
        self.__pulgadas = StringVar()
        self.__centimetros = StringVar()

        # input y label pulgadas
        self.input_pulgadas = ttk.Entry(
            contenedor,
            width=7,
            textvariable=self.__pulgadas,
        )
        self.input_pulgadas.grid(column=2, row=1, sticky="we")
        ttk.Label(
            contenedor,
            text="pulgadas",
            background=palette.get_bg(),
            foreground=palette.get_fg(),
            padding=(10, 10),
        ).grid(column=3, row=1, sticky="w")

        # label equivalecia
        ttk.Label(
            contenedor,
            text="es equivalente a",
            background=palette.get_bg(),
            foreground=palette.get_fg(),
            padding=(10, 10),
        ).grid(column=1, row=2, sticky=W)

        # input y label centimetros

        ttk.Label(
            contenedor,
            textvariable=self.__centimetros,
            background=palette.get_bg(),
            foreground=palette.get_fg(),
        ).grid(column=2, row=2, pady=10, sticky="we")

        ttk.Label(
            contenedor,
            text="centimetros",
            background=palette.get_bg(),
            foreground=palette.get_fg(),
        ).grid(column=3, row=2, sticky=W)

        ttk.Button(contenedor, text="Calcular", command=self.calcular).grid(
            column=2, row=3, sticky="we"
        )
        ttk.Button(contenedor, text="Salir", command=self.__ventana.destroy).grid(
            column=3, row=3, sticky="we"
        )
        self.__ventana.mainloop()

    def calcular(self):
        try:
            valor = float(self.input_pulgadas.get())
            self.__centimetros.set(str(2.54 * valor))
        except ValueError:
            print("Error de tipo: Debe ingresar un valor numerico")
            self.__pulgadas.set("")
            self.input_pulgadas.focus()


if __name__ == "__main__":
    app = Aplicacion()
