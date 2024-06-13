from tkinter import *
from tkinter import font, ttk

from Color_Palette import Color_Palette


class Aplicacion:
    __ventana: Tk
    __usuario: StringVar
    __clave: StringVar

    def __init__(self):
        super().__init__()
        self.__ventana = Tk()
        palette = Color_Palette()

        # Configuración de ventana
        self.__ventana.title("Login Pack")
        self.__ventana.configure(bg=palette.get_bg())
        self.__ventana.geometry("300x200")
        self.__ventana.resizable(width=False, height=False)

        # crear labels
        fuente = font.Font(weight="bold")
        self.label_usuario = ttk.Label(
            self.__ventana,
            text="Usuario:",
            font=fuente,
            background=palette.get_bg(),
            foreground=palette.get_fg(),
        )
        self.label_clave = ttk.Label(
            self.__ventana,
            text="Contraseña:",
            font=fuente,
            background=palette.get_bg(),
            foreground=palette.get_fg(),
        )

        # setear estado
        self.__usuario = StringVar()
        self.__clave = StringVar()
        self.__usuario.set("")

        # crear inputs
        self.input_usuario = ttk.Entry(
            self.__ventana, textvariable=self.__usuario, width=30
        )
        self.input_clave = ttk.Entry(
            self.__ventana, textvariable=self.__clave, width=30, show="*"
        )

        # padding
        self.separador = ttk.Separator(self.__ventana, orient=HORIZONTAL)

        # botones
        self.boton_aceptar = ttk.Button(
            self.__ventana, text="Aceptar", command=self.aceptar
        )
        self.boton_cancelar = ttk.Button(self.__ventana, text="Cancelar", command=quit)

        # organizar widgets
        self.label_usuario.place(relx=0.1, rely=0.1)
        self.input_usuario.place(relx=0.1, rely=0.2)

        self.label_clave.place(relx=0.1, rely=0.4)
        self.input_clave.place(relx=0.1, rely=0.5)

        self.boton_aceptar.place(relx=0.1, rely=0.7)
        self.boton_cancelar.place(relx=0.6, rely=0.7)

        # set focus al primer input
        self.input_usuario.focus_set()

        self.__ventana.mainloop()

    def aceptar(self):
        if self.__clave.get() == "tkinter":
            print("acceso permitido")
            print(f"Usuario: {self.input_usuario.get()}")
            print(f"Clave: {self.input_clave.get()}")
        else:
            print("Acceso denegado")
            self.__clave.set("")
            self.input_clave.focus_set()


if __name__ == "__main__":
    app = Aplicacion()
