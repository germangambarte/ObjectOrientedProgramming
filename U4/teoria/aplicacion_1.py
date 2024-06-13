from tkinter import *
from tkinter import ttk

from Color_Palette import Color_Palette


class Aplicacion:
    def __init__(self) -> None:
        # crear una ventana
        ventana = Tk()
        palette = Color_Palette()
        # asignar una medida de ventana
        ventana.geometry("300x200")
        # asignar color de fondo
        ventana.configure(bg=palette.get_bg())
        # asignar titulo a la ventana
        ventana.title("Primera Aplicacion")
        # agregar un boton para cerrar la ventana
        ttk.Button(ventana, text="Salir", command=ventana.destroy).pack(side=BOTTOM)
        # mantiene la ventana abierta
        ventana.mainloop()


if __name__ == "__main__":
    app = Aplicacion()
