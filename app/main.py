from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt

from ventana import Ventana
from cotizacion import Cotizacion
from cliente import Cliente

console = Console()

def mostrar_menu():
    menu = Panel(
        "[bold white]--- Menú ---[/bold white]",
        title="Opciones",
        border_style="blue",
    )
    console.print(menu)

    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Opción", style="dim")
    table.add_column("Descripción")

    table.add_row("[red]1.[/red]", "Crear cotización")
    table.add_row("[red]2.[/red]", "Salir")

    console.print(table)

def crear_cotizacion():
    try:
        nombre_cliente = Prompt.ask("Ingrese el nombre del cliente")
        telefono_cliente = Prompt.ask("Ingrese el teléfono del cliente")
        correo_cliente = Prompt.ask("Ingrese el correo del cliente")

        cantidad_ventanas = int(Prompt.ask("Ingrese la cantidad de ventanas"))
        cliente = Cliente(nombre_cliente, telefono_cliente, correo_cliente)

        ventanas = []
        for i in range(cantidad_ventanas):
            console.print(f"\n[bold cyan]Ventana {i + 1}:[/bold cyan]")
            estilo = Prompt.ask("Ingrese el estilo de la ventana (O, XO, OXXO, OXO)").upper()
            if estilo not in ["O", "XO", "OXO", "OXXO"]:
                raise ValueError("Estilo de ventana inválido.")

            ancho = float(Prompt.ask("Ingrese el ancho de la ventana (cm)"))
            alto = float(Prompt.ask("Ingrese el alto de la ventana (cm)"))

            acabado = Prompt.ask("Ingrese el tipo de acabado (Pulido, Lacado Brillante, Lacado Mate, Anodizado)")
            if acabado not in ["Pulido", "Lacado Brillante", "Lacado Mate", "Anodizado"]:
                raise ValueError("Tipo de acabado inválido.")

            tipo_vidrio = Prompt.ask("Ingrese el tipo de vidrio (Transparente, Bronce, Azul)")
            if tipo_vidrio not in ["Transparente", "Bronce", "Azul"]:
                raise ValueError("Tipo de vidrio inválido.")

            esmerilado = Prompt.ask("¿Esmerilado (S/N)?", choices=["S", "N"]).lower() == 's'
            cantidad = int(Prompt.ask("¿Cuántas ventanas de este estilo va a comprar?"))

            # Crear instancia de la ventana
            ventana = Ventana(estilo, ancho, alto, tipo_vidrio, acabado, cantidad, esmerilado)
            ventanas.append(ventana)

        # Crear la cotización
        cotizacion = Cotizacion(fecha="2024-10-19", cliente=cliente, ventanas=ventanas)
        total= cotizacion.calcular_total()

        # Construye los detalles individuales de cada ventana
        detalles_ventanas = ""
        for i, ventana in enumerate(cotizacion.ventanas, start=1):
            precio_individual = ventana.calcular_precio_total()
            detalles_ventanas += f"Ventana {i}: Estilo [bold blue]{ventana.estilo}[/bold blue] | " \
                                f"Cantidad: [light_cyan1]{ventana.cantidad}[/light_cyan1] | Precio: [bold red]${precio_individual:,.2f}[/bold red]\n"

        # Crear el panel con los detalles de la cotización y las ventanas individuales
        resultado = Panel(
            f"Fecha [bold green]{cotizacion.fecha}[/bold green] \n"
            f"Cotización para [bold green]{cliente.nombre}[/bold green]             | Cotización Nro. [bold yellow]{cotizacion.nro_cotizacion}[/bold yellow]|\n"
            f"Teléfono: {cliente.telefono} | Correo: {cliente.correo}\n\n"
            f"[underline]Detalle de Ventanas:[/underline]\n"
            f"{detalles_ventanas}\n"  
            f"El costo total de la cotización es: [bold red]${total:,.2f}[/bold red]",
            title="Resultado de la Cotización",
            border_style="green",
        )

        # Imprimir el resultado
        console.print(resultado)


    except ValueError as e:
        console.print(f"[bold red]Error:[/bold red] {e}. Por favor, intente de nuevo.")
    except Exception as e:
        console.print(f"[bold red]Error inesperado:[/bold red] {e}")

def main():
    while True:
        mostrar_menu()
        opcion = Prompt.ask("Seleccione una opción")
        if opcion == '1':
            crear_cotizacion()
        elif opcion == '2':
            console.print("[bold yellow]Saliendo del programa...[/bold yellow]")
            break
        else:
            console.print("[bold red]Opción inválida. Intente de nuevo.[/bold red]")

if __name__ == "__main__":
    main()
