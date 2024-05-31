from Empleado import Empleado


class Gestor_Empleados:
    __empleados: list[Empleado]

    def __init__(self) -> None:
        self.__empleados = []

    def agregar_empleado(self, empleado: Empleado):
        self.__empleados.append(empleado)

    def get_empleados(self):
        return self.__empleados

    def buscar_empleado(self, id: int):
        valor_retorno = None
        i = 0
        encontrado = False
        while not encontrado:
            if self.__empleados[i].get_id() == id:
                valor_retorno = i
                encontrado = True
            else:
                i += 1
        return valor_retorno

    def informar_duraciones(self, indice: int):
        for matricula in self.__empleados[indice].get_matriculas():
            capacitacion = matricula.get_capacitacion()
            print(f"{capacitacion.get_nombre()} dura {capacitacion.get_duracion()}hs")

    def mostrar_empleado_por_capacitacion(self, capacitacion):
        print("\nLos empleados inscriptos son:")
        for empleado in self.__empleados:
            matriculas = empleado.get_matriculas()
            for matricula in matriculas:
                if matricula.get_capacitacion().get_nombre() == capacitacion:
                    print(f"{empleado.get_nombre_apellido()}")

    def mostrar_empleados_sin_capacitacion(self):
        print("\nEmpleados sin capacitacion: ")
        for empleado in self.__empleados:
            if len(empleado.__matriculas) == 0:
                print(f"{empleado.get_nombre_apellido()}")
