from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.ventana import Ventana
from app.cotizacion import Cotizacion
from app.cliente import Cliente

console = Console()

# Lista para almacenar el historial de cambios
historial_cambios = []

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
    table.add_row("[red]2.[/red]", "Actualizar precio de tipo de vidrio o acabado")
    table.add_row("[red]3.[/red]", "Ver historial de cambios")
    table.add_row("[red]4.[/red]", "Salir")

    console.print(table)

def crear_cotizacion():
    # Implementación de crear cotización (se deja igual)
    pass

def actualizar_precios():
    console.print("\n[bold cyan]--- Actualización de Precios ---[/bold cyan]")
    
    # Mostrar las opciones manualmente
    console.print("[bold yellow]1.[/bold yellow] Tipo de Vidrio")
    console.print("[bold yellow]2.[/bold yellow] Acabado")
    
    opcion = Prompt.ask("¿Qué desea actualizar?", choices=["1", "2"])
    
    if opcion == "1":
        # Mostrar tipos de vidrio
        console.print("\n[bold yellow]Tipos de Vidrio Disponibles:[/bold yellow]")
        for tipo, precio in Ventana.precios_vidrio.items():
            console.print(f"- {tipo}: [bright_green]${precio:.2f}[/bright_green] por cm²")

        tipo_vidrio = Prompt.ask("Ingrese el tipo de vidrio que desea actualizar", choices=list(Ventana.precios_vidrio.keys()))
        nuevo_precio = float(Prompt.ask(f"Ingrese el nuevo precio para el vidrio {tipo_vidrio} (por cm²)"))
        
        # Guardar el precio anterior antes de actualizar
        precio_anterior = Ventana.precios_vidrio[tipo_vidrio]
        
        # Actualizar el precio
        Ventana.actualizar_precio_vidrio(tipo_vidrio, nuevo_precio)
        console.print(f"[green]Precio del vidrio {tipo_vidrio} actualizado a ${nuevo_precio:.2f} por cm².[/green]")
        
        # Añadir al historial
        historial_cambios.append({
            "tipo": "Vidrio",
            "nombre": tipo_vidrio,
            "precio_anterior": precio_anterior,
            "precio_nuevo": nuevo_precio
        })

    elif opcion == "2":
        # Mostrar tipos de acabados
        console.print("\n[bold yellow]Tipos de Acabados Disponibles:[/bold yellow]")
        for tipo, precio in Ventana.precios_acabado.items():
            console.print(f"- {tipo}: [bright_green]${precio:.2f}[/bright_green] por cm")

        tipo_acabado = Prompt.ask("Ingrese el tipo de acabado que desea actualizar", choices=list(Ventana.precios_acabado.keys()))
        nuevo_precio = float(Prompt.ask(f"Ingrese el nuevo precio para el acabado {tipo_acabado} (por cm)"))
        
        # Guardar el precio anterior antes de actualizar
        precio_anterior = Ventana.precios_acabado[tipo_acabado]
        
        # Actualizar el precio
        Ventana.actualizar_precio_acabado(tipo_acabado, nuevo_precio)
        console.print(f"[green]Precio del acabado {tipo_acabado} actualizado a ${nuevo_precio:.2f} por cm.[/green]")
        
        # Añadir al historial
        historial_cambios.append({
            "tipo": "Acabado",
            "nombre": tipo_acabado,
            "precio_anterior": precio_anterior,
            "precio_nuevo": nuevo_precio
        })

def ver_historial():
    if not historial_cambios:
        console.print("[yellow]No hay cambios en el historial aún.[/yellow]")
    else:
        # Crear una tabla para mostrar el historial
        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("Tipo", style="dim")
        table.add_column("Nombre")
        table.add_column("Precio Anterior")
        table.add_column("Precio Nuevo")

        for cambio in historial_cambios:
            table.add_row(
                cambio["tipo"],
                cambio["nombre"],
                f"${cambio['precio_anterior']:.2f}",
                f"${cambio['precio_nuevo']:.2f}"
            )

        console.print(table)

def main():
    while True:
        mostrar_menu()
        opcion = Prompt.ask("Seleccione una opción")
        if opcion == '1':
            crear_cotizacion()
        elif opcion == '2':
            actualizar_precios()
        elif opcion == '3':
            ver_historial()
        elif opcion == '4':
            console.print("[bold yellow]Saliendo del programa...[/bold yellow]")
            break
        else:
            console.print("[bold red]Opción inválida. Intente de nuevo.[/bold red]")

if __name__ == "__main__":
    main()
