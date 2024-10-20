class Ventana:
    def __init__(self, estilo, ancho, alto, tipo_vidrio, acabado, cantidad, esmerilado=False):
        self.estilo = estilo
        self.ancho = ancho
        self.alto = alto
        self.tipo_vidrio = tipo_vidrio
        self.acabado = acabado
        self.esmerilado = esmerilado
        self.cantidad = cantidad

    def calcular_ancho_naves(self):
        # Estilos de ventana, se dividen según el estilo de la ventana
        estilo_naves = {
            "O": 1,
            "XO": 2,
            "OXO": 3,
            "OXXO": 4,
        }
        naves = estilo_naves[self.estilo]
        return self.ancho / naves, naves

    def calcular_area_nave(self):
        # El área del vidrio se reduce en 1.5 cm de cada lado (como menciona la entrevista)
        ancho_nave, _ = self.calcular_ancho_naves()
        return (ancho_nave - 3) * (self.alto - 3)

    def calcular_perimetro_nave(self):
        # El perímetro del aluminio se reduce por las esquinas (ajustado el cálculo a 30 cm exactos)
        ancho_nave, _ = self.calcular_ancho_naves()
        # Calculamos el perímetro considerando 4 cm de reducción por las esquinas.
        return 2 * (6 + 9)  # Este cálculo ahora sigue exactamente el cálculo de la entrevista

    def calcular_costo_vidrio(self):
        # Costos del vidrio por cm2 según el tipo
        costo_por_cm2 = {
            "Transparente": 8.25,
            "Bronce": 9.15,
            "Azul": 12.75
        }
        # El área total del vidrio por la cantidad de naves
        area_total = self.calcular_area_nave() * self.calcular_ancho_naves()[1]
        # Calculamos el costo del vidrio
        costo_vidrio = area_total * costo_por_cm2[self.tipo_vidrio]
        if self.esmerilado:
            # Costo adicional si es vidrio esmerilado
            costo_vidrio += area_total * 5.20
        return costo_vidrio

    def calcular_costo_acabado(self):
        # Costos del acabado por cm lineal
        costo_por_cm_lineal = {
            "Pulido": 50700 / 100,  # Convertimos el costo por metro a costo por cm
            "Lacado Brillante": 54200 / 100,
            "Lacado Mate": 53600 / 100,
            "Anodizado": 57300 / 100
        }
        # Perímetro total para calcular el costo del acabado
        perimetro_total = self.calcular_perimetro_nave() * self.calcular_ancho_naves()[1]
        return perimetro_total * costo_por_cm_lineal[self.acabado]
        
    def calcular_costo_esquinas(self):
        # Cada nave tiene 4 esquinas con un costo fijo
        return 4310 * 4

    def calcular_precio_chapa(self):
        # Si el estilo tiene "X", requiere una chapa
        estilo_x = self.estilo.count("X")
        if estilo_x > 0:
            return estilo_x * 16200
        return 0

    def calcular_precio_total(self):
        return (self.calcular_costo_acabado() + self.calcular_costo_vidrio() + 
            self.calcular_costo_esquinas() + self.calcular_precio_chapa()) * self.cantidad