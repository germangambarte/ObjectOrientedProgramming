from GestorCuentas import GestorCuenta
from GestorTransacciones import GestorTransacciones


def mostrar_menu():
    print("\n--------Menu--------")
    print("[1] Mostrar datos por de un cliente")
    print("[2] Modificar porcentaje anual del rendimiento")
    print("[3] Actualizar saldo de los clientes")
    print("[4] Procesar transacciones")
    print("[5] Exportar cuentas")
    print("[6] Mostrar cuentas")
    print("[7] Mostrar transacciones")

    print("[0] Salir")


if __name__ == "__main__":
    gc = GestorCuenta()
    gt = GestorTransacciones()
    salir = False
    while not salir:
        mostrar_menu()

        opcion = input("\nIngresar una opcion: ")

        match opcion:
            case "0":
                print("Saliendo...")
                salir = True
                break
            case "1":
                dni = input("DNI del cliente: ")
                pass
            case "2":
                pass
            case "3":
                pass
            case "4":
                pass
            case "5":
                pass
            case "6":
                pass
            case "7":
                pass
