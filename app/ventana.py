# ventana.py
class Ventana:
    def __init__(self, estilo, ancho, alto, tipo_vidrio, acabado, cantidad, esmerilado=False):
        self.estilo = estilo  # Atributo estilo
        self.ancho = ancho
        self.alto = alto
        self.tipo_vidrio = tipo_vidrio
        self.acabado = acabado
        self.esmerilado = esmerilado
        self.cantidad = cantidad

    def calcular_ancho_naves(self):
        # Número de naves por estilo
        estilo_naves = {
            "O": 1,
            "XO": 2,
            "OXO": 3,
            "OXXO": 4,
        }
        naves = estilo_naves[self.estilo]
        return self.ancho / naves, naves

    def calcular_area_nave(self):
        ancho_nave, _ = self.calcular_ancho_naves()
        # Área del vidrio por nave, reduciendo 1.5 cm de cada lado
        return (ancho_nave - 1.5) * (self.alto - 1.5)

    def calcular_perimetro_nave(self):
        ancho_nave, _ = self.calcular_ancho_naves()
        # El perímetro se calcula como la suma de los lados de la nave menos 4 cm por las esquinas
        return 2 * (ancho_nave + self.alto) - 4 * 4  # Menos 4 cm por las esquinas

    def calcular_costo_vidrio(self):
        # Costos del vidrio por cm2
        costo_por_cm2 = {
            "Transparente": 8.25,
            "Bronce": 9.15,
            "Azul": 12.75
        }
        # Área total del vidrio considerando la cantidad de naves
        area_total = self.calcular_area_nave() * self.calcular_ancho_naves()[1]
        costo_vidrio = area_total * costo_por_cm2[self.tipo_vidrio]
        if self.esmerilado:
            costo_vidrio += area_total * 5.20  # Costo adicional por esmerilado
        return costo_vidrio

    def calcular_costo_acabado(self):
        # Costo del acabado por cm lineal
        costo_por_cm_lineal = {
            "Pulido": 50700 / 100,
            "Lacado Brillante": 54200 / 100,
            "Lacado Mate": 53600 / 100,
            "Anodizado": 57300 / 100
        }
        # Perímetro total del aluminio multiplicado por el número de naves
        perimetro_total = self.calcular_perimetro_nave() * self.calcular_ancho_naves()[1]
        return perimetro_total * costo_por_cm_lineal[self.acabado]

    def calcular_costo_esquinas(self):
        # Cuatro esquinas por nave
        return 4310 * 4

    def calcular_precio_chapa(self):
        # Cada "X" en el estilo representa una nave que necesita chapa
        estilo_x = self.estilo.count("X")
        if estilo_x > 0:
            return estilo_x * 16200  # Costo por chapa
        return 0

    def calcular_precio_total(self):
        # Sumar todos los costos y multiplicar por la cantidad de ventanas
        return (self.calcular_costo_acabado() + self.calcular_costo_vidrio() + 
                self.calcular_costo_esquinas() + self.calcular_precio_chapa()) * self.cantidad
