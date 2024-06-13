import tkinter as tk
from tkinter import *
from tkinter import font, ttk

from Color_Palette import Color_Palette


class Aplicacion(tk.Tk):
    __version = "Version 1.0"

    def __init__(self) -> None:
        super().__init__()
        self.fuente = font.Font(weight="normal")
        opciones = Menu(master=self)

        opciones_archivo = Menu(master=opciones, tearoff=0)
        opciones_ayuda = Menu(master=opciones, tearoff=0)
        opciones_salir = Menu(master=opciones, tearoff=0)

        opciones_archivo.add_command(
            label="Nuevo", command=self.nuevo, accelerator="Ctrl+n"
        )
        opciones_archivo.add_command(
            label="Abrir", command=self.abrir, accelerator="Ctrl+a"
        )
        opciones_archivo.add_separator()
        opciones_archivo.add_command(label="Guardar")
        opciones_archivo.add_command(label="Guardar como...")

        opciones_ayuda.add_command(label="Acerca de...", command=self.acerca_de)

        opciones_salir.add_command(
            label="Salir", command=self.destroy, accelerator="Ctrl+q"
        )
        self.configure(menu=opciones)
        self.bind("<Control-n>", self.nuevo())
        self.bind("<Control-a>", self.abrir())
        self.bind("<Control-q>", lambda event: self.destroy)

    def nuevo(self):
        pass

    def abrir(self):
        pass

    def acerca_de(self):
        pass


if __name__ == "__main__":
    app = Aplicacion()
    app.mainloop()
