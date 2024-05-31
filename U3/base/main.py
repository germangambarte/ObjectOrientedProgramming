from Menu import Menu

if __name__ == "__main__":
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
                pass
            case "2":
                pass
            case "3":
                pass
            case "4":
                pass
