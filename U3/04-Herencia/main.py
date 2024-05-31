from Gestor_Publicaciones import Gestor_Publicaciones
from Menu import Menu

if __name__ == "__main__":
    gp = Gestor_Publicaciones()
    menu = Menu()
    finaliza = False
    while not finaliza:
        menu.mostrar_menu()
        opcion = input("\nIngrese una opcion: ")

        match opcion:
            case "0":
                print("Saliendo...")
                finaliza = True
                break
            case "1":
                print("\nQue desea publicar?")
                print("[1] Libro")
                print("[2] Audiolibro")
                tipo = input("\nIngrese una opcion: ")
                gp.crear_publicacion(tipo)
            case "2":
                indice = input("Ingrese una posicion: ")
                gp.mostrar_tipo(int(indice))
            case "3":
                gp.mostrar_cantidad_por_tipo()
            case "4":
                gp.mostrar_publicaciones()
