# main.py
from ventana import Ventana
from cotizacion import Cotizacion
from cliente import Cliente

def mostrar_menu():
    print("\n--- Menú ---")
    print("1. Crear cotización")
    print("2. Salir")

def crear_cotizacion():
    try:
        nombre_cliente = input("Ingrese el nombre del cliente: ")
        telefono_cliente = input("Ingrese el teléfono del cliente: ")
        correo_cliente = input("Ingrese el correo del cliente: ")

        cantidad_ventanas = int(input("Ingrese la cantidad de ventanas: "))
        cliente = Cliente(nombre_cliente, telefono_cliente, correo_cliente)

        ventanas = []
        for i in range(cantidad_ventanas):
            print(f"\nVentana {i+1}:")
            estilo = input("Ingrese el estilo de la ventana (O, XO, OXXO, OXO): ").upper()
            if estilo not in ["O", "XO", "OXO", "OXXO"]:
                raise ValueError("Estilo de ventana inválido.")

            ancho = float(input("Ingrese el ancho de la ventana (cm): "))
            alto = float(input("Ingrese el alto de la ventana (cm): "))

            acabado = input("Ingrese el tipo de acabado (Pulido, Lacado Brillante, Lacado Mate, Anodizado): ")
            if acabado not in ["Pulido", "Lacado Brillante", "Lacado Mate", "Anodizado"]:
                raise ValueError("Tipo de acabado inválido.")

            tipo_vidrio = input("Ingrese el tipo de vidrio (Transparente, Bronce, Azul): ")
            if tipo_vidrio not in ["Transparente", "Bronce", "Azul"]:
                raise ValueError("Tipo de vidrio inválido.")

            esmerilado = input("¿Esmerilado (S/N)? ").lower() == 's'

            # Crear instancia de la ventana
            ventana = Ventana(estilo, ancho, alto, tipo_vidrio, acabado, 1, esmerilado)
            ventanas.append(ventana)

        # Crear la cotización
        cotizacion = Cotizacion(fecha="2024-10-19", cliente=cliente, ventanas=ventanas)
        total = cotizacion.calcular_total()

        # Mostrar resultado
        print(f"\nCotización para {cliente.nombre}")
        print(f"Teléfono: {cliente.telefono} | Correo: {cliente.correo}")
        print(f"El costo total de la cotización es: ${total:.2f}")

    except ValueError as e:
        print(f"Error: {e}. Por favor, intente de nuevo.")
    except Exception as e:
        print(f"Error inesperado: {e}")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            crear_cotizacion()
        elif opcion == '2':
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    main()
