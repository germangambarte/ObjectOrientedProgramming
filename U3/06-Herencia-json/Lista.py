from typing import Optional

from Calefactor_Electrico import Calefactor_Electrico
from Calefactor_Gas import Calefactor_Gas
from Nodo import Nodo


class Lista:
    __comienzo: Optional[Nodo]
    __actual: Optional[Nodo]
    __indice: int
    __tope: int

    def __init__(self) -> None:
        self.__comienzo = None
        self.__actual = None
        self.__tope = 0
        self.__indice = 0
        pass

    def __iter__(self):
        return self

    def __next__(self):
        if self.__indice == self.__tope:
            self.__actual = self.__comienzo
            self.__indice = 0
            raise StopIteration
        else:
            self.__indice += 1
            if isinstance(self.__actual, Nodo):
                calefactor = self.__actual.get_calefactor()
                self.__actual = self.__actual.get_siguiente()
                return calefactor

    def toJSON(self):
        calefactores = []
        for calefactor in self:
            if calefactor is not None:
                calefactores.extend([calefactor.toJSON()])

        return dict(
            __class__=self.__class__.__name__,
            calefactores=calefactores,
        )

    def agregar_calefactor(self, calefactor: Calefactor_Gas | Calefactor_Electrico):
        nodo = Nodo(calefactor)
        nodo.set_siguiente(self.__comienzo)
        self.__comienzo = nodo
        self.__actual = nodo
        self.__tope += 1

    def agregar_nodo_por_indice(self, nodo: Nodo, indice):
        try:
            if indice > self.__tope:
                raise IndexError
            nodo_actual = self.__comienzo
            aux = None
            i = 0
            bandera = False
            while nodo_actual is not None and not bandera:
                if i == indice:
                    aux = nodo_actual
                    nodo_actual = nodo
                    nodo.set_siguiente(aux)
                else:
                    i += 1
                    nodo_actual = nodo_actual.get_siguiente()
        except IndexError:
            print("\nEl indice ingresado no es valido")
        except:
            print("\nAlgo salio mal")

    def mostrar_nodo_por_indice(self, indice):
        try:
            if indice > self.__tope:
                raise IndexError
            nodo_actual = self.__comienzo
            i = 0
            encontrado = False
            while nodo_actual is not None and not encontrado:
                if i == indice:
                    if isinstance(nodo_actual.get_calefactor(), Calefactor_Electrico):
                        print(f"La posicion {indice} contiene un calefactor electrico")
                    else:
                        print(f"La posicion {indice} contiene un calefactor a gas")
                    encontrado = True
                else:
                    i += 1
                    nodo_actual = nodo_actual.get_siguiente()
        except IndexError:
            print("\nEl indice ingresado no es valido")
        except:
            print("\nAlgo salio mal")

    def buscar_menor_precio_a_gas(self):
        min = 9999999999
        indice = None
        i = 0
        if self is None:
            print("La lista esta vacia")
            return

        for calefactor in self:
            if isinstance(calefactor, Calefactor_Gas):
                if calefactor.get_importe() < min:
                    min = calefactor.get_importe()
                    indice = i
            i += 1
        return indice

    def mostrar_menor_precio(self, indice):
        encontrado = False
        i = 0
        actual = self.__comienzo

        if actual is None:
            print("La lista esta vacia")
            return

        while not encontrado:
            calefactor = actual.get_calefactor()
            if i == indice and isinstance(calefactor, Calefactor_Gas):
                print(
                    f"Marca: {calefactor.get_modelo()}, calorias: {calefactor.get_calorias()}"
                )

    def crear_nodo(self, calefactor: Calefactor_Electrico | Calefactor_Gas):
        nodo = Nodo(calefactor)
        nodo.set_siguiente(self.__comienzo)
        self.__comienzo = nodo
        self.__actual = nodo
        self.__tope += 1
        return nodo

    def crear_calefactor(self):
        calefactor = None
        print("Que tipo de calefactor desea agregar?")
        print("[1] Calefactor Electrico.")
        print("[2] Calefactor A Gas.")
        tipo = input("Ingrese una opcion: ")
        modelo = input("Modelo: ")
        precio_lista = float(input("Precio de Lista: "))
        forma_pago = input("Forma de Pago ('Contado', 'Cuotas'): ")
        cant_cuotas = 1
        if forma_pago.lower() == "Cuotas":
            cant_cuotas = int(input("Cantidad de cuotas: "))
        promocion = input("Aplica promocion?('Si','No'): ")
        if tipo == "1":
            calorias = input("Potencia maxima: ")
            calefactor = Calefactor_Electrico(
                modelo,
                precio_lista,
                forma_pago,
                cant_cuotas,
                promocion,
                calorias,
            )
        else:
            calorias = input("Calorias: ")
            calefactor = Calefactor_Gas(
                modelo,
                precio_lista,
                forma_pago,
                cant_cuotas,
                promocion,
                calorias,
            )
        return calefactor
