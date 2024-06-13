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
        self.__ventana.title("Login Pack")

        # crear labels
        fuente = font.Font(weight="bold")
        self.label_usuario = ttk.Label(self.__ventana, text="Usuario", font=fuente)
        self.label_clave = ttk.Label(self.__ventana, text="Contraseña", font=fuente)

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
        self.label_usuario.pack(side=TOP, fill=X, padx=5, pady=5)
        self.input_usuario.pack(side=TOP, fill=X, padx=5, pady=5)

        self.label_clave.pack(side=TOP, fill=X, padx=5, pady=5)
        self.input_clave.pack(side=TOP, fill=X, padx=5, pady=5)

        self.separador.pack(side=TOP, fill=X, padx=10, pady=10)

        self.boton_aceptar.pack(side=LEFT, fill=BOTH, expand=True, padx=5, pady=5)
        self.boton_cancelar.pack(side=RIGHT, fill=BOTH, expand=True, padx=5, pady=5)

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
