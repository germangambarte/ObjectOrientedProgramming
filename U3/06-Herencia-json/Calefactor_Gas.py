from Calefactor import Calefactor


class Calefactor_Gas(Calefactor):
    __calorias: str

    def __init__(
        self,
        modelo: str,
        precio_lista: float,
        forma_pago: str,
        cant_cuotas: int,
        promocion: str,
        calorias: str,
    ) -> None:
        super().__init__(
            modelo,
            precio_lista,
            forma_pago,
            cant_cuotas,
            promocion,
        )
        self.__calorias = calorias

    def get_calorias(self):
        return self.__calorias

    def get_importe(self):
        base = super().get_precio_lista()
        importe_total = base
        if super().get_promocion().lower() == "si":
            importe_total -= base * 0.15
        calorias = self.__calorias.rsplit("k")[0]
        if int(calorias) > 3000:
            importe_total += base * 0.01
        if super().get_cant_cuotas() > 1:
            importe_total += base * 0.4
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
                calorias=self.__calorias,
            ),
        )
