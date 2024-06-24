import random
import time
from tkinter import *
from tkinter import Tk, ttk


class Tablero(ttk.Frame):
    __puntaje: IntVar

    def __init__(self, padre, actulizar_puntaje, guardar_puntaje):
        super().__init__(padre)
        self.actualizar_puntaje = actulizar_puntaje
        self.guardar_puntaje = guardar_puntaje
        self.__puntaje = IntVar(value=0)

        self.config(padding=(5, 5), relief="flat")
        self.secuencia_maquina = []
        self.secuencia_jugador = []
        self.config_botones = [
            ("#c0392b", "#641e16", 0, 0),
            ("#2980b9", "#1b4f72", 0, 1),
            ("#16a085", "#0b5345", 1, 0),
            ("#f1c40f", "#7d6608", 1, 1),
        ]
        self.botones = {}

        for bg_activo, bg_inactivo, fila, columna in self.config_botones:
            boton = Canvas(
                self,
                bg=bg_activo,
                width=100,
                height=150,
                cursor="hand2",
                relief="raised",
            )
            boton.bind("<Button-1>", lambda event, c=bg_activo: self.manejar_click(c))
            boton.grid(row=fila, column=columna, padx=5, pady=5)
            self.botones[bg_activo] = (boton, bg_inactivo)
        self.grid(row=1, column=0, sticky="nesw")

        self.boton_inicio = Button(
            self, text="Iniciar Partida", command=self.iniciar_juego
        )
        self.boton_inicio.grid(row=3, column=0, columnspan=2)

    def iniciar_juego(self):
        self.boton_inicio.config(state="disabled")
        self.deshabilitar_colores()
        self.secuencia_maquina = []
        self.secuencia_jugador = []
        self.__puntaje.set(0)
        self.proximo_nivel()

    def proximo_nivel(self):
        self.secuencia_jugador = []
        self.secuencia_maquina.append(
            random.choice([cb[0] for cb in self.config_botones])
        )
        self.reproducir_secuencia()

    def reproducir_secuencia(self):
        self.after(500, self.parpadear_boton, 0)

    def parpadear_boton(self, index):
        if index < len(self.secuencia_maquina):
            color = self.secuencia_maquina[index]
            boton, bg_inactivo = self.botones[color]
            boton.config(bg=color)
            self.after(500, lambda: boton.config(bg=bg_inactivo))
            self.after(1000, self.parpadear_boton, index + 1)
        else:
            self.habilitar_colores()

    def manejar_click(self, color):
        self.secuencia_jugador.append(color)
        self.retroalimentacion(color)
        if (
            self.secuencia_jugador
            == self.secuencia_maquina[: len(self.secuencia_jugador)]
        ):
            self.__puntaje.set(self.__puntaje.get() + 1)
            self.actualizar_puntaje(self.__puntaje.get())

            if self.secuencia_jugador == self.secuencia_maquina:
                self.after(100, self.deshabilitar_colores)
                self.after(1000, self.proximo_nivel)
        else:
            self.terminar_juego()

    def retroalimentacion(self, color):
        boton, bg_inactivo = self.botones[color]
        boton.config(bg=bg_inactivo)
        self.after(100, lambda: boton.config(bg=color))

    def habilitar_colores(self):
        for bg_activo, (boton, _) in self.botones.items():
            boton.config(bg=bg_activo)
            boton.bind("<Button-1>", lambda event, c=bg_activo: self.manejar_click(c))

    def deshabilitar_colores(self):
        for boton, bg_inactivo in self.botones.values():
            boton.config(bg=bg_inactivo)
            boton.unbind("<Button-1>")

    def terminar_juego(self):
        self.boton_inicio.config(state="normal")
        self.guardar_puntaje()
