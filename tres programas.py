class Tres_programas:
    def __init__(self, monto_compra):
        self.monto_compra = monto_compra

    def descuento_clientes(self):
        if self.monto_compra < 500:
            descuento = 0
            tipo_descuento = "Sin descuento"
        elif 500 <= self.monto_compra <= 1000:
            descuento = 0.05
            tipo_descuento = "5% de descuento"
        elif 1000 < self.monto_compra <= 7000:
            descuento = 0.11
            tipo_descuento = "11% de descuento"
        elif 7000 < self.monto_compra <= 15000:
            descuento = 0.18
            tipo_descuento = "18% de descuento"
        else:
            descuento = 0.25
            tipo_descuento = "25% de descuento"

        monto_descuento = self.monto_compra * descuento
        monto_final = self.monto_compra - monto_descuento

        print(f"Monto de compra: ${self.monto_compra}")
        print(f"Descuento aplicado: {tipo_descuento}")
        print(f"Monto descontado: ${monto_descuento}")
        print(f"Monto final después del descuento: ${monto_final}")

#Bloque
monto_compra_ejemplo = 20000
compra = Tres_programas(monto_compra_ejemplo)
compra.descuento_clientes()