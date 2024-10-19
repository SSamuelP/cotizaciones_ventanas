from rich import print

class Cotizacion:
    nro_cotizacion = 0

    def __init__(self, fecha, cliente, ventanas):
        Cotizacion.nro_cotizacion += 1
        self.fecha = fecha
        self.cliente = cliente
        self.ventanas = ventanas

    def calcular_total(self):
        total = 0

        # Mostrar el costo individual de cada ventana
        precio_ind = []
        for ventana in self.ventanas:
            precio_individual = ventana.calcular_precio_total()
            precio_ind.append(precio_individual)

        total = sum(precio_ind)
        precio_ind.append(total)

        # Verificar si hay descuento
        suma_ventanas = sum(ventana.cantidad for ventana in self.ventanas)
        if suma_ventanas > 100:
            total *= 0.9  # Aplicar descuento del 10%
            print("[orange_red1]Se ha aplicado un descuento del 10% por comprar más de 100 ventanas.[/orange_red1]")


        return total
