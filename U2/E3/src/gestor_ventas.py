import numpy as np


class Gestor_Ventas:
    __ventas = []

    def __init__(self):
        self.__ventas = np.zeros((5, 7))
        correr_programa = True
        while correr_programa:
            self.mostrar_menu()
            opcion = input("Opcion: ")
            match opcion:
                case "0":
                    correr_programa = False
                    break
                case "1":
                    self.agregar_venta()
                case "2":
                    self.total_por_sucursal()
                case "3":
                    self.maxima_facturacion_por_dia()
                case "4":
                    self.minima_facturacion_por_semana()
                case "5":
                    self.facturacion_total()

    def mostrar_menu(self):
        print("\n-----Seleccione una opcion-----")
        print("0. Finalizar")
        print("1. Agregar nueva venta")
        print("2. Obtener facturación de una sucursal")
        print("3. Obtener sucursal que mas facturo")
        print("4. Obtener dia en el que menos se facturo")
        print("5. Obtener facturacion total")

    def agregar_venta(self):
        dia = int(input("\nDia:"))
        sucursal = int(input("Sucursal:"))
        importe = float(input("Importe:"))

        self.__ventas[sucursal - 1][dia - 1] += importe

        print("\nVenta agregada")

    def total_por_sucursal(self):
        sucursal = int(input("\nSucursal:"))
        sum = 0.0

        for i in range(7):
            sum += self.__ventas[sucursal - 1][i]

        print(f"La sucursal {sucursal} facturo ${sum}")

    def maxima_facturacion_por_dia(self):
        dia = int(input("\nDia:"))
        max = 0.0
        sucursal = None

        for i in range(5):
            venta = self.__ventas[i][dia - 1]
            if venta > max:
                max = venta
                sucursal = i + 1

        print(f"\nMayor facturacion: ${max}")
        print(f"Sucursal: ${sucursal}")

    def minima_facturacion_por_semana(self):
        min = 99999999.9
        sucursal = None

        for i in range(5):
            for j in range(7):
                venta = self.__ventas[i][j]
                if min > venta and venta != 0:
                    min = venta
                    sucursal = i + 1

        print(f"\nMinima facturacion: ${min}")
        print(f"Sucursal: {sucursal}")

    def facturacion_total(self):
        sum = 0.0

        for i in range(5):
            for j in range(7):
                sum += self.__ventas[i][j]

        print(f"\nFacturacion total: ${sum}")
