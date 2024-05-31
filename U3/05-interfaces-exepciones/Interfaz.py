from zope.interface import Interface


class IFoo(Interface):
    def insertar_elemento(self):
        pass

    def agregar_elemento(self):
        pass

    def mostrar_elemento(self):
        pass


if __name__ == "__main__":
    print(type(IFoo))
