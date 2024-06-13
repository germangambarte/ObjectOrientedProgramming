import tkinter as tk
from tkinter import *
from tkinter import ttk


class Simon_Game(tk.Tk):
    __puntaje: IntVar
    __jugador: StringVar
    __dialogo: Toplevel

    def __init__(self):
        super().__init__()
        self.title("Simon Dice")
        self.__jugador = StringVar(value="Puntaje")
        self.__puntaje = IntVar(value=0)

        contenedor_puntaje = ttk.Frame(self, padding=(5, 5), relief=GROOVE)

        tk.Label(contenedor_puntaje, text=self.__jugador.get()).pack(
            side="left", expand=True
        )

        tk.Label(contenedor_puntaje, textvariable=self.__puntaje).pack(
            side="left", expand=True
        )
        contenedor_puntaje.grid(row=0, column=0, sticky="nesw")

        # -----------------------------------

        contenedor_colores = ttk.Frame(self, padding=(5, 5), relief=GROOVE)

        boton_rojo = tk.Canvas(
            contenedor_colores, bg="#ff0000", width=100, height=150, cursor="hand2"
        )
        boton_rojo.grid(column=0, row=0, padx=5, pady=5, sticky="nesw")

        boton_verde = tk.Canvas(
            contenedor_colores, bg="#00ff00", width=100, height=150, cursor="hand2"
        )
        boton_verde.grid(column=1, row=0, padx=5, pady=5, sticky="nesw")

        boton_azul = tk.Canvas(
            contenedor_colores, bg="#0000ff", width=100, height=150, cursor="hand2"
        )
        boton_azul.grid(column=0, row=1, padx=5, pady=5, sticky="nesw")

        boton_amarillo = tk.Canvas(
            contenedor_colores, bg="#ffff00", width=100, height=150, cursor="hand2"
        )
        boton_amarillo.grid(column=1, row=1, padx=5, pady=5, sticky="nesw")

        contenedor_colores.grid(row=1, column=0)

        # -----------------------------------

        menu_barra = Menu(self)
        menu_puntajes = Menu(menu_barra, tearoff=0)
        menu_puntajes.add_command(
            label="Ver Puntajes", command=self.mostrar_puntajes, accelerator="Ctrl+p"
        )
        menu_puntajes.add_command(label="Salir", command=self.destroy)
        self.config(menu=menu_barra)

        # -----------------------------------
        self.__jugador.set("")

        self.__dialogo = Toplevel()
        dialogo_frame = ttk.LabelFrame(
            self.__dialogo, text="Datos del Jugador", relief="raised"
        )
        ttk.Label(dialogo_frame, text="Jugador:").grid(column=0, row=0, pady=5, padx=5)
        ttk.Entry(dialogo_frame, textvariable=self.__jugador).grid(
            column=1, row=0, padx=5
        )
        ttk.Button(
            dialogo_frame, text="Iniciar Juego", command=self.manejador_nombre_jugador
        ).grid(row=2, column=0, columnspan=2, pady=5)

        dialogo_frame.pack()

        self.__dialogo.transient(master=self)
        self.__dialogo.grab_set()
        self.wait_window(self.__dialogo)

    def manejador_nombre_jugador(self):
        print(self.__jugador.get())

    def mostrar_puntajes(self):
        pass


if __name__ == "__main__":
    app = Simon_Game()
    app.mainloop()
