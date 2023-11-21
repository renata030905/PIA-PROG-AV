class Utilidades:
    def __init__(self, nombre_archivo):
        self.nombre_archivo = nombre_archivo

    def archivos_texto(self, contenido=None):
        if contenido is not None:
           
            with open(self.nombre_archivo, 'w') as archivo:
                archivo.write(contenido)

       
        with open(self.nombre_archivo, 'r') as archivo:
            contenido_leido = archivo.read()

        return contenido_leido

    def descuento_clientes(self, monto_compra):
        if monto_compra < 500:
            descuento = 0
        elif 500 <= monto_compra <= 1000:
            descuento = 0.05
        elif 1000 < monto_compra <= 7000:
            descuento = 0.11
        elif 7000 < monto_compra <= 15000:
            descuento = 0.18
        else:
            descuento = 0.25

        monto_descuento = monto_compra * descuento
        monto_final = monto_compra - monto_descuento

        return {
            "monto_compra": monto_compra,
            "descuento_aplicado": descuento,
            "monto_descuento": monto_descuento,
            "monto_final": monto_final
        }

    def dinosaurio(self, nom, pes, lon):
        pes_kil = pes / 2.20462
        lon_met = lon * 0.3047

        return {
            "nombre": nom,
            "peso_kilogramos": pes_kil,
            "longitud_metros": lon_met
        }

    def gasolina(self, gal):
        litros_surtidos = gal * 3.785
        total_pagar = litros_surtidos * 8.20

        return {
            "galones_surtidos": gal,
            "total_pagar": total_pagar
        }
    
utilidades = Utilidades("archivo_ejemplo.txt")


resultado_descuento = utilidades.descuento_clientes(8000)
print("Resultado del método descuento_clientes:", resultado_descuento)

# dinosaurio
resultado_dinosaurio = utilidades.dinosaurio("T-Rex", 2000, 30)
print("Resultado del método dinosaurio:", resultado_dinosaurio)

# gasolina
resultado_gasolina = utilidades.gasolina(15.90)
print("Resultado del método gasolina:", resultado_gasolina)

# archivos_texto
contenido_a_escribir = "Contenido de prueba para el archivo."
resultado_archivos_texto = utilidades.archivos_texto(contenido_a_escribir)
print("Resultado del método archivos_texto:", resultado_archivos_texto)