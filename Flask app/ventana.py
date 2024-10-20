class Ventana:
    # Diccionarios para almacenar los precios de los acabados y tipos de vidrio
    precios_vidrio = {
        "Transparente": 8.25,
        "Bronce": 9.15,
        "Azul": 12.75
    }

    precios_acabado = {
        "Pulido": 50700 / 100,  # Convertimos el costo por metro a costo por cm
        "Lacado Brillante": 54200 / 100,
        "Lacado Mate": 53600 / 100,
        "Anodizado": 57300 / 100
    }

    def __init__(self, estilo, ancho, alto, tipo_vidrio, acabado, cantidad, esmerilado=False):
        self.estilo = estilo
        self.ancho = ancho
        self.alto = alto
        self.tipo_vidrio = tipo_vidrio
        self.acabado = acabado
        self.esmerilado = esmerilado
        self.cantidad = cantidad

    def calcular_ancho_naves(self):
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
        return (ancho_nave - 3) * (self.alto - 3)

    def calcular_perimetro_nave(self):
        ancho_nave, _ = self.calcular_ancho_naves()
        return 2 * ((ancho_nave - 6) + (self.alto - 6))  
    
    def calcular_costo_vidrio(self):
        area_total = self.calcular_area_nave() * self.calcular_ancho_naves()[1]
        costo_vidrio = area_total * self.precios_vidrio[self.tipo_vidrio]
        if self.esmerilado:
            costo_vidrio += area_total * 5.20
        return costo_vidrio

    def calcular_costo_acabado(self):
        perimetro_total = self.calcular_perimetro_nave() * self.calcular_ancho_naves()[1]
        return perimetro_total * self.precios_acabado[self.acabado]
        
    def calcular_costo_esquinas(self):
        return 4310 * 4

    def calcular_precio_chapa(self):
        estilo_x = self.estilo.count("X")
        return estilo_x * 16200 if estilo_x > 0 else 0

    def calcular_precio_total(self):
        return (self.calcular_costo_acabado() + self.calcular_costo_vidrio() + 
                self.calcular_costo_esquinas() + self.calcular_precio_chapa()) * self.cantidad

    @classmethod
    def actualizar_precio_vidrio(cls, tipo_vidrio, nuevo_precio):
        if tipo_vidrio in cls.precios_vidrio:
            cls.precios_vidrio[tipo_vidrio] = nuevo_precio

    @classmethod
    def actualizar_precio_acabado(cls, tipo_acabado, nuevo_precio):
        if tipo_acabado in cls.precios_acabado:
            cls.precios_acabado[tipo_acabado] = nuevo_precio
