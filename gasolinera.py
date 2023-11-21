class Gasolinera:
    def __init__(self, gal):
        self.GAL = gal
        self.TOTAL = 0  

    def gasolina(self):
        
        litros_surtidos = self.GAL * 3.785  # 1 galón = 3.785 litros
        self.TOTAL = litros_surtidos * 8.20  # Precio por litro: $8.20

       
        print(f"Galones surtidos: {self.GAL} galones")
        print(f"Total a pagar: ${self.TOTAL:.2f}")

#Bloque
galones_surtidos_ejemplo = 15.90
cliente1 = Gasolinera(galones_surtidos_ejemplo)
cliente1.gasolina()