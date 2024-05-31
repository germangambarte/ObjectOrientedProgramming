from GestorLadrillo import Gestor_Ladrillo
from GestorMaterial import Gestor_Material


class Menu:
    def mostrar(self):
        print("\n----------Menu----------")
        print("[1] Detallar datos del material.")
        print("[2] Mostrar costo de fabricacion de los ladrillos.")
        print("[3] Mostrar tabla de productos.")


if __name__ == "__main__":
    menu = Menu()
    gl = Gestor_Ladrillo()
    gm = Gestor_Material()
    bandera = False
    while not bandera:
        menu.mostrar()

        opcion = input("\nIngrese una opcion: ")

        match opcion:
            case "0":
                print("\nSaliendo...")
                bandera = True
                break
            case "1":
                id = int(input("\nIngrese el id del ladrillo: "))
                indice = gl.buscar_ladrillo_por_id(id)
                if indice is None:
                    print("No se encontro el ladrillo")
                    break
                gl.mostrar_datos_material(indice)
            case "2":
                pass
