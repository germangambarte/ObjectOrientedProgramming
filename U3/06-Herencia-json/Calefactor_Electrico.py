from Calefactor import Calefactor


class Calefactor_Electrico(Calefactor):
    __potencia_maxima: str

    def __init__(
        self,
        modelo: str,
        precio_lista: float,
        forma_pago: str,
        cant_cuotas: int,
        promocion: str,
        potencia_maxima: str,
    ) -> None:
        super().__init__(
            modelo,
            precio_lista,
            forma_pago,
            cant_cuotas,
            promocion,
        )
        self.__potencia_maxima = potencia_maxima

    def get_potencia_maxima(self):
        return self.__potencia_maxima

    def get_importe(self):
        base = super().get_precio_lista()
        importe_total = base
        if super().get_promocion().lower() == "si":
            importe_total -= base * 0.15
        potencia = self.__potencia_maxima.rsplit("w")[0]
        if int(potencia) > 1000:
            importe_total += base * 0.01
        if super().get_cant_cuotas() > 1:
            importe_total += base * 0.3
        return importe_total

    def toJSON(self) -> dict:
        return dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(
                modelo=super().get_modelo(),
                precio_lista=super().get_precio_lista(),
                forma_pago=super().get_forma_pago(),
                cant_cuotas=super().get_cant_cuotas(),
                promocion=super().get_promocion(),
                potencia_maxima=self.__potencia_maxima,
            ),
        )
