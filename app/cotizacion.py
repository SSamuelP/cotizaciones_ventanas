class Cotizacion:
    def __init__(self, cliente, ventanas):
        self.cliente = cliente
        self.ventanas = ventanas

    def calcular_total(self):
        total = sum(ventana.calcular_costo_total() for ventana in self.ventanas)
        if self.cliente.cantidad_ventanas > 100:
            total *= 0.9  # Apply 10% discount
        return total
