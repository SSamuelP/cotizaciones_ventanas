from ventana import Ventana

class Cotizacion:
    nro_cotizacion = 0

    def __init__(self, fecha, cliente, ventanas):
        Cotizacion.nro_cotizacion += 1
        self.fecha = fecha
        self.cliente = cliente
        self.ventanas = ventanas

    def calcular_total(self):
        total = sum(ventana.calcular_precio_total() for ventana in self.ventanas)

        suma_ventanas = sum(ventana.cantidad for ventana in self.ventanas)
        if suma_ventanas > 100:
            total *= 0.9  # Aplicar descuento del 10%
        return total
