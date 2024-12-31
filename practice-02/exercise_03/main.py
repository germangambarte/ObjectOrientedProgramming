from SalesManager import SalesManager


def menu():
    print("Menu:\n")
    print("\t1. Agregar nueva factura.")
    print("\t2. Calcular facturación por sucursal.")
    print("\t3. Obtener máxima facturación semanal por día.")
    print("\t4. Obtener menor facturación semanal.")
    print("\t5. Obtener facturación semanal.")
    print("\t6. Salir.")
    print("\n")


def test():
    sl = SalesManager()
    option = int(input("Elija una opción.\n"))

    while option:
        menu()

        if option == 1:
            print("\n")
            day = int(input("Día: "))
            branch = int(input("Sucursal: "))
            amount = float(input("Importe de la factura: "))
            if 0 < day < 7:
                print("Dia, no válido.")
            elif 0 < branch < 5:
                print("Sucursal, no válida.")
            elif amount < 0:
                print("El importe debe ser mayor a $0")
            else:
                sl.add_bill(day, branch, amount)
        if option == 2:
            print("\n")
            branch = int(input("Sucursal: "))
            if 0 < branch < 5:
                print("Sucursal, no válida.")
            else:
                total_billed = sl.total_billing_by_branch(branch)
                print(f"La sucursal {branch} facturó: ${total_billed}\n")
        if option == 3:
            print("\n")
            day = int(input("Día: "))
            if 0 < day < 7:
                print("Dia, no válido.")
            else:
                branch = sl.get_max_billed_branch_by_day(day)
                print(f"La sucursal que más facturó es la número: {branch}")
        if option == 4:
            pass
        if option == 5:
            sl.get_min_bil_by_week()
        if option == 6:
            print("saliendo...")
            return

        option = int(input("Elija una opción.\n"))


if __name__ == '__main__':
    pass
