import json
from datetime import datetime

from Jugador import Jugador


class Gestor_Jugadores:
    __lista: list[Jugador]

    def __init__(self) -> None:
        self.__lista = []

    def resetear_lista(self):
        self.__lista = []

    def ordenar_lista(self):
        self.__lista = sorted(
            self.__lista,
            reverse=True,
            key=lambda jugador: jugador.get_puntaje(),
        )

    def cargar_desde_archivo(self):
        diccionario = self.leer_archivo()
        self.decodificar_dicccionario(diccionario)

    def leer_archivo(self):
        diccionario = None
        with open("pysimonpuntajes.json", encoding="UTF-8") as archivo:
            diccionario = json.load(archivo)
        return diccionario

    def decodificar_dicccionario(self, d):
        if "__class__" not in d:
            return d
        else:
            class_name = d["__class__"]
            if class_name == "Gestor_Jugadores":
                jugadores = d["jugadores"]
                for i in range(len(jugadores)):
                    d_jugador = jugadores[i]
                    atributos = d_jugador["__atributos__"]
                    jugador = Jugador(**atributos)
                    self.agregar_jugador_desde_json(jugador)

    def actualizar_archivo(self):
        diccionario = self.codificar_lista()
        with open("pysimonpuntajes.json", "w") as archivo:
            json.dump(diccionario, archivo, indent=4)

    def codificar_lista(self):
        return dict(
            __class__=self.__class__.__name__,
            jugadores=[j.tojson() for j in self.__lista],
        )

    def agregar_jugador_desde_json(self, jugador):
        self.__lista.append(jugador)

    def agregar_jugador_nuevo(self, nombre, puntaje):
        hoy = datetime.now()
        fecha = hoy.strftime("%d/%m/%Y")
        hora = hoy.strftime("%H:%M")
        self.__lista.append(Jugador(nombre, fecha, hora, puntaje))

    def get_lista(self):
        return self.__lista
