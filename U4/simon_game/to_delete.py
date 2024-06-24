import random
from tkinter import *
from tkinter import Tk, ttk


class Tablero(ttk.Frame):
    __puntaje: IntVar

    def __init__(self, enviar_puntajes):
        super().__init__()
        self.enviar_puntajes = enviar_puntajes
        self.__puntaje = IntVar(value=0)

        self.config(padding=(5, 5), relief="flat")
        self.secuencia_maquina = []
        self.secuencia_jugador = []
        self.config_botones = ["#ff0000", "#00FF00", "#0000FF", "#FFFF00"]
        self.botones = {}

        for i, color in enumerate(self.config_botones):
            boton = Canvas(
                self,
                bg=color,
                width=100,
                height=150,
                state="disabled",
                cursor="hand2",
                relief="raised",
            )
            boton.bind("<Button-1>", lambda event, c=color: self.manejar_click(c))
            boton.grid(row=i // 2, column=i % 2, padx=5, pady=5)
            self.botones[color] = boton
        self.grid(row=1, column=0, sticky="nesw")

        self.boton_inicio = Button(
            self, text="Iniciar Partida", command=self.iniciar_juego
        )
        self.boton_inicio.grid(row=3, column=0, columnspan=2)

    def iniciar_juego(self):
        self.boton_inicio.config(state="disabled")
        self.secuencia_maquina = []
        self.secuencia_jugador = []
        self.__puntaje.set(0)
        self.proximo_nivel()

    def proximo_nivel(self):
        self.secuencia_jugador = []
        self.secuencia_maquina.append(random.choice(self.config_botones))
        self.reproducir_secuencia()

    def reproducir_secuencia(self):
        self.after(500, self.parpadear_boton, 0)

    def parpadear_boton(self, index):
        if index < len(self.secuencia_maquina):
            color = self.secuencia_maquina[index]
            self.botones[color].config(bg="white")
            self.after(500, lambda: self.restaurar_color(color))
            self.after(1000, self.parpadear_boton, index + 1)
        else:
            self.habilitar_colores()

    def restaurar_color(self, color):
        self.botones[color].config(bg=color)

    def manejar_click(self, color):
        self.secuencia_jugador.append(color)
        if (
            self.secuencia_jugador
            == self.secuencia_maquina[: len(self.secuencia_jugador)]
        ):
            # boton_cliqueado = self.botones[color]
            # boton_cliqueado.config(bg="green")
            # self.after(500, lambda: boton_cliqueado.config(relief="raised"))

            self.__puntaje.set(self.__puntaje.get() + 1)
            print(self.__puntaje.get())
            if self.secuencia_jugador == self.secuencia_maquina:
                self.deshabilitar_colores()
                self.after(1000, self.proximo_nivel)
        else:
            self.terminar_juego()

    def habilitar_colores(self):
        for boton in self.botones.values():
            color = boton["bg"]
            boton.bind("<Button-1>", lambda event, c=color: self.manejar_click(c))

    def deshabilitar_colores(self):
        for boton in self.botones.values():
            boton.unbind("<Button-1>")

    def terminar_juego(self):
        self.boton_inicio.config(state="normal")
        for boton in self.botones.values():
            boton.config(state="disabled")
        self.enviar_puntajes(self.__puntaje.get())
