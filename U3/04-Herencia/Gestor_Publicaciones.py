from Audiolibro import Audiolibro
from Libro import Libro


class Gestor_Publicaciones:
    __publicaciones: list[Libro | Audiolibro]

    def __init__(self):
        self.__publicaciones = []
        self.__publicaciones.append(Libro("El Gran Libro","Comendia",500.0,"Juan Perez",2010,300))
        self.__publicaciones.append(Audiolibro("El Gran Audiolibro","Comendia",500.0,300,"Juan Perez"))

    def crear_publicacion(self,tipo):
        titulo = input("Titulo: ")
        categoria = input("Categoria: ")
        precio_base = input("Precio base: ")
        if tipo=="1":
            autor = input("Autor: ")
            fecha_edicion = input("Fecha de edicion(dd/mm/aaaa): ")
            cant_paginas = input("Cantidad de paginas: ")
            libro = Libro(titulo,categoria,float(precio_base),autor,int(fecha_edicion),int(cant_paginas))
            self.carga(libro)
        if tipo == "2":
            duracion = input("Duracion: ")
            narrador = input("Narrador: ")
            audiolibro = Audiolibro(titulo,categoria,float(precio_base),int(duracion),narrador)
            self.carga(audiolibro)

    def carga(self, publicacion: Libro | Audiolibro):
        self.__publicaciones.append(publicacion)
        print("\nCarga realizada corractamente")

    def mostrar_tipo(self, indice: int):
        if isinstance(self.__publicaciones[indice], Libro):
            print(f"\nEn la posicion {indice}, se almacena un libro")
        if isinstance(self.__publicaciones[indice], Audiolibro):
            print(f"\nEn la posicion {indice}, se almacena un audiolibro")

    def mostrar_cantidad_por_tipo(self):
        cant_libros = 0
        cant_audiolibros = 0
        for publicacion in self.__publicaciones:
            if isinstance(publicacion, Libro):
                cant_libros += 1
            if isinstance(publicacion, Audiolibro):
                cant_audiolibros += 1
        print("\nSe encuentran almacenados: ")
        print(f"- {cant_libros} libros")
        print(f"- {cant_audiolibros} audiolibros")

    def mostrar_publicaciones(self):
        print("\nLista de publicaciones: ")
        for publicacion in self.__publicaciones:
            if isinstance(publicacion, Libro):
                print(
                    f"Titulo: {publicacion.get_titulo()}, Categoria del libro: {publicacion.get_categoria()}, Precio: {publicacion.get_precio_final()}"
                )
            if isinstance(publicacion, Audiolibro):
                print(
                    f"Titulo: {publicacion.get_titulo()}, Categoria del audiolibro: {publicacion.get_categoria()}, Precio: {publicacion.get_precio_final()}"
                )
