from tkinter import *
from tkinter import font, ttk


class Aplicacion:
    __ventana: Tk
    __usuario: StringVar
    __clave: StringVar

    def __init__(self):
        super().__init__()
        # Configuración de ventana
        self.__ventana = Tk()
        self.__ventana.title("Login Grid")

        # configuracion base
        fuente = font.Font(weight="bold")
        self.marco = ttk.Frame(
            self.__ventana, borderwidth=2, relief="raised", padding=(10, 10)
        )

        # crear labels
        self.label_usuario = ttk.Label(
            self.marco,
            text="Usuario:",
            font=fuente,
            padding=(0, 5),
        )
        self.label_clave = ttk.Label(
            self.marco,
            text="Contraseña:",
            font=fuente,
            padding=(0, 5),
        )

        # setear estado
        self.__usuario = StringVar()
        self.__clave = StringVar()
        self.__usuario.set("")

        # crear inputs
        self.input_usuario = ttk.Entry(
            self.marco, textvariable=self.__usuario, width=30
        )
        self.input_clave = ttk.Entry(
            self.marco,
            textvariable=self.__clave,
            width=30,
            show="*",
        )

        # padding
        self.separador = ttk.Separator(self.marco, orient=HORIZONTAL)

        # botones
        self.boton_aceptar = ttk.Button(
            self.marco, text="Aceptar", command=self.aceptar, padding=(5, 5)
        )
        self.boton_cancelar = ttk.Button(
            self.marco, text="Cancelar", command=quit, padding=(5, 5)
        )

        # organizar widgets
        self.marco.grid(row=0, column=0)

        self.label_usuario.grid(row=0, column=0, sticky=W)

        self.input_usuario.grid(row=1, column=0, columnspan=2)

        self.label_clave.grid(row=2, column=0, sticky=W)
        self.input_clave.grid(row=3, column=0, columnspan=2)

        self.separador.grid(
            row=4, column=0, columnspan=2, pady=10, padx=10, sticky="ew"
        )

        self.boton_aceptar.grid(row=5, column=0, sticky="ew")
        self.boton_cancelar.grid(row=5, column=1, sticky="ew")

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
