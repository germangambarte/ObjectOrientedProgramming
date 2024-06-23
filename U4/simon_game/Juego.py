from tkinter import *
from tkinter import Tk, ttk

from Gestor_Jugadores import Gestor_Jugadores
from Tablero_2 import Tablero


class Juego(Tk):
    __nombre_jugador: StringVar

    def __init__(self):
        super().__init__()
        self.gj = Gestor_Jugadores()
        self.title("Py Simon Game")
        self.puntaje = IntVar(value=0)
        self.__nombre_jugador = StringVar(value="")

        Tablero(self, self.actualizar_puntaje, self.guardar_puntaje)
        self.crear_menu_barra()
        self.crear_prompt_inicial()
        self.crear_seccion_puntaje()

    def crear_menu_barra(self):
        menu_barra = Menu()

        menu_puntajes = Menu(menu_barra, tearoff=False)
        menu_puntajes.add_command(
            label="Ver Puntajes", command=self.mostrar_puntajes, accelerator="Ctrl+p"
        )

        self.bind("<Control-p>", self.mostrar_puntajes)

        menu_puntajes.add_command(label="Salir", command=self.destroy)

        menu_barra.add_cascade(menu=menu_puntajes, label="Puntajes")
        self.config(menu=menu_barra)

    def mostrar_puntajes(self, event=None):
        self.gj.resetear_lista()
        self.gj.cargar_desde_archivo()
        self.gj.ordenar_lista()
        ventana = Toplevel(self)
        ventana.title("Ver Puntajes")
        contenedor_tabla = ttk.Frame(ventana, padding=(5, 5), relief="groove")
        titulos = ("Nombre", "Fecha", "Hora", "Puntaje")
        tabla = ttk.Treeview(contenedor_tabla, columns=titulos, show="headings")

        for titulo in titulos:
            tabla.heading(titulo, text=titulo)
        for jugador in self.gj.get_lista():
            tabla.insert(
                "",
                "end",
                values=(
                    jugador.get_nombre(),
                    jugador.get_fecha(),
                    jugador.get_hora(),
                    jugador.get_puntaje(),
                ),
            )

        tabla.pack(fill="both", expand=True)

    def crear_prompt_inicial(self):
        self.__dialogo = Toplevel()
        dialogo_frame = LabelFrame(
            self.__dialogo, text="Datos del Jugador", relief="raised"
        )
        Label(dialogo_frame, text="Jugador:").grid(column=0, row=0, pady=5, padx=5)
        Entry(dialogo_frame, textvariable=self.__nombre_jugador).grid(
            column=1, row=0, padx=5
        )
        Button(
            dialogo_frame, text="Iniciar Juego", command=self.__dialogo.destroy
        ).grid(row=2, column=0, columnspan=2, pady=5)

        dialogo_frame.pack()

        self.__dialogo.transient(master=self)
        self.__dialogo.grab_set()
        self.wait_window(self.__dialogo)

    def crear_seccion_puntaje(self):
        contenedor_puntaje = ttk.Frame(self, padding=(5, 5), relief="groove")

        Label(contenedor_puntaje, text=self.__nombre_jugador.get()).pack(
            side="left",
            expand=True,
        )
        Label(contenedor_puntaje, textvariable=self.puntaje).pack(
            side="left",
            expand=True,
        )

        contenedor_puntaje.grid(
            row=0,
            column=0,
            sticky="nesw",
        )

    def actualizar_puntaje(self, puntaje: int):
        self.puntaje.set(puntaje)

    def guardar_puntaje(self):
        self.gj.agregar_jugador_nuevo(self.__nombre_jugador.get(), self.puntaje.get())
