from Calefactor_Electrico import Calefactor_Electrico
from Calefactor_Gas import Calefactor_Gas
from Lista import Lista
from ObjectEncoder import ObjectEncoder

if __name__ == "__main__":
    oe = ObjectEncoder()
    lista = Lista()
    diccionario = oe.leer_archivo()
    lista = oe.decodificador_dict(diccionario)
    # print(type(lista))
    if isinstance(lista, Lista):
        # diccionario = lista.toJSON()
        # oe.exportar_archivo(diccionario)
        lista.mostrar_nodo_por_indice(1)
        lista.mostrar_nodo_por_indice(2)
