class Dinosaurio:
    def __init__(self, nom, pes, lon):
        self.NOM = nom
        self.PES = pes
        self.LON = lon
        self.PESKIL = 0  
        self.LONMET = 0  

    def dinosaurio(self):
        
        self.PESKIL = self.PES / 2.20462  # 1 libra = 0.453592 kilogramos
        self.LONMET = self.LON * 0.3047  # 1 pie = 0.3047 metros

        
        print(f"Nombre del dinosaurio: {self.NOM}")
        print(f"Peso en kilogramos: {self.PESKIL:.2f} kg")
        print(f"Longitud en metros: {self.LONMET:.2f} m")


nombre_dino = input("Ingresa el nombre del dinosaurio: ")
peso_dino = float(input("Ingresa el peso del dinosaurio en libras: "))
longitud_dino = float(input("Ingresa la longitud del dinosaurio en pies: "))


dino_usuario = Dinosaurio(nombre_dino, peso_dino, longitud_dino)

#Bloque 
dino_usuario.dinosaurio()