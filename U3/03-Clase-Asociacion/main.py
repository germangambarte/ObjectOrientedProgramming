from Empleado import Empleado
from Programa_Capacitacion import Programa_Capacitacion
from Gestor_Empleados import Gestor_Empleados
from Gestor_Matriculas import Gestor_Matriculas
from Gestor_Programa_Capacitacion import Gestor_Programa_Capacitacion


class Test:
    def __init__(self) -> None:
        self.ge = Gestor_Empleados()
        self.gm = Gestor_Matriculas()
        self.gpc = Gestor_Programa_Capacitacion()
        self.carga()

    def carga(self):
        empleado_1 = Empleado("German Gambarte", 1, "administrativo")
        self.ge.agregar_empleado(empleado_1)
        empleado_2 = Empleado("Micaela Farias", 2, "administrativo")
        self.ge.agregar_empleado(empleado_2)
        empleado_3 = Empleado("Richard Molina", 3, "administrativo")
        self.ge.agregar_empleado(empleado_3)

        capacitacion_1 = Programa_Capacitacion("Tango Gestion", "1", 10)
        self.gpc.agregar_programa(capacitacion_1)
        capacitacion_2 = Programa_Capacitacion("Disenio Grafico", "2", 15)
        self.gpc.agregar_programa(capacitacion_2)

        empleado_1.agregar_matricula(self.gm, "2024-05-19", capacitacion_1)
        empleado_1.agregar_matricula(self.gm, "2024-05-20", capacitacion_2)
        empleado_2.agregar_matricula(self.gm, "2024-04-07", capacitacion_1)

    def mostrar_menu(self):
        print("\n----------Menu----------")
        print("[1] Informar duracion de programas matriculados.")
        print("[2] Mostrar Empleados matriculados en una capacitacion.")
        print("[3] Mostrar Empleados no matriculados.")


if __name__ == "__main__":
    ge = Gestor_Empleados()
    test = Test()
    test.carga()

    bandera = False

    while not bandera:
        test.mostrar_menu()
        opcion = input("\nIngrese una opcion: ")
        match opcion:
            case "0":
                print("Saliendo")
                bandera = True
                break
            case "1":
                id = int(input("\nIngrese el id de un empleado: "))
                indice = ge.buscar_empleado(id)
                if indice is None:
                    print("No se encontro el empleado")
                    break
                ge.informar_duraciones(indice)
            case "2":
                capacitacion = input("\nIngrese el nombre de la capacitacion: ")
                ge.mostrar_empleado_por_capacitacion(capacitacion)
            case "3":
                ge.mostrar_empleados_sin_capacitacion()
