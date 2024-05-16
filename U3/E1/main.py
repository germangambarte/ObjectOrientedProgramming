from GestorEdificios import GestorEdificio
from Menu import Menu


if __name__ == "__main__":
    ge = GestorEdificio()
    menu = Menu()
    finaliza = False
    while not finaliza:
        menu.mostrar_menu()
        opcion = input("\nIngrese una opcion: ")

        match opcion:
            case "0":
                finaliza = True
                break
            case "1":
                nombre_edificio = input("\nIngrese nombre de edificio: ")
                indice_edificio = ge.buscar_edificio_por_nombre(nombre_edificio)
                if indice_edificio is None:
                    print("No se encontro el edificio")
                    break
                ge.mostrar_propietarios(indice_edificio)
            case "2":
                nombre_edificio = input("\nIngrese nombre de edificio: ")
                indice_edificio = ge.buscar_edificio_por_nombre(nombre_edificio)
                if indice_edificio is None:
                    print("No se encontro el edificio")
                    break
                ge.calcular_sup_total(indice_edificio)
            case "3":
                nombre_propiertario = input("\nIngrese nombre de propiertario: ")
                indice_edificio = ge.buscar_edificio_por_nombre_propietario(
                    nombre_propiertario
                )
                if indice_edificio is None:
                    print("No se encontro el propietario")
                    break
                indice_propiertario = ge.buscar_depto_por_nombre_propietario(
                    indice_edificio, nombre_propiertario
                )
                if indice_propiertario is None:
                    print("No se encontro el propietario")
                    break
                ge.mostrar_sup_por_propietario(indice_edificio, indice_propiertario)
            case "4":
                nombre_edificio = input("\nIngrese nombre de edificio: ")
                indice_edificio = ge.buscar_edificio_por_nombre(nombre_edificio)
                if indice_edificio is None:
                    print("No se encontro el edificio")
                    break
                nro_piso = int(input("\nIngrese numero de piso: "))
                print("holis")
                ge.contar_deptos(indice_edificio, nro_piso)
