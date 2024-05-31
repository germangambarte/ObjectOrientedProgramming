import json

from Calefactor_Electrico import Calefactor_Electrico
from Calefactor_Gas import Calefactor_Gas
from Lista import Lista

# from pathlib import Path


class ObjectEncoder:
    def decodificador_dict(self, d):
        if "__class__" not in d:
            return d
        else:
            class_name = d["__class__"]
            lista_class = globals().get(class_name)
            if lista_class is None:
                raise ValueError(f"Clase '{class_name}' no definida")
            if class_name == "Lista":
                calefactores = d["calefactores"]
                manejador = lista_class()
                for i in range(len(calefactores)):
                    d_calefactor = calefactores[i]
                    calefactor_class_name = d_calefactor.pop("__class__")
                    calefactor_class = globals().get(calefactor_class_name)
                    if calefactor_class is None:
                        raise ValueError(f"Clase '{calefactor_class_name}' no definida")

                    atributos = d_calefactor["__atributos__"]
                    calefactor = calefactor_class(**atributos)
                    manejador.agregar_calefactor(calefactor)
                return manejador

    def exportar_archivo(self, diccionario):
        with open("exportado.json", "w") as archivo:
            json.dump(diccionario, archivo, indent=4)

    def leer_archivo(self):
        diccionario = None
        with open("calefactores.json", encoding="UTF-8") as archivo:
            diccionario = json.load(archivo)
        return diccionario

    def texto_a_dict(self, texto):
        return json.loads(texto)
