from GestorEquipo import GestorEquipo
from GestorFechaFutbol import GestorFechaFutbol


def mostrar_menu():
    print("\n-----Opciones-----")
    print("[1] Cargar equipos por archivo.")
    print("[2] Cargar fechas por archivo.")
    print("[3] Obtener fechas de un equipo.")
    print("[4] Actualizar tabla de posiciones.")
    print("[5] Ordenar tabla de posiciones.")
    print("[6] Exportar tabla de posiciones.")

    print("[0] Salir.")


if __name__ == "__main__":
    ge = GestorEquipo()
    gf = GestorFechaFutbol()

    finaliza = False
    while not finaliza:
        mostrar_menu()
        opcion = input("\nIngrese una opcion: ")
        match opcion:
            case "0":
                print("\nFinalizo el programa.")
                finaliza = True
            case "1":
                ge.carga_equipos_por_archivo()
                print("\nSe cargaron los equipos.")
            case "2":
                gf.carga_fechas_por_archivo()
                print("\nSe cargaron las fechas jugadas.")
            case "3":
                nombre = input("\nNombre del equipo: ")
                indice = ge.obtener_indice_por_nombre(nombre)
                if indice is None:
                    print("No se encontro un equipo")
                    finaliza = True
                    break
                equipo = ge.get_equipos()[indice]
                gf.mostrar_fechas_por_equipo(equipo)
            case "4":
                fechas = gf.get_fechas()
                ge.actualizar_tabla(fechas)
                print("\nTabla de posiciones actualizada:")
                ge.mostrar_equipos()
            case "5":
                ge.ordenar_equipos()
                print("\nTabla de posiciones ordenada:")
                ge.mostrar_equipos()
            case "6":
                ge.exportar_datos()
