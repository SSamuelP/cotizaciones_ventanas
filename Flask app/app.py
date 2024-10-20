from flask import Flask, render_template, request
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from ventana import Ventana
from cliente import Cliente
from cotizacion import Cotizacion

app = Flask(__name__)

# Lista para almacenar el historial de precios
historial_precios = []

# Home page where users can input data for quotation
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle form submission and calculate the quotation
@app.route('/cotizacion', methods=['POST'])
def cotizacion():
    # Collecting client data
    nombre = request.form['nombre']
    telefono = request.form['telefono']
    correo = request.form['correo']
    cliente = Cliente(nombre, telefono, correo)

    # Collecting window data
    ventanas = []
    estilos = request.form.getlist('estilo[]')
    anchos = request.form.getlist('ancho[]')
    altos = request.form.getlist('alto[]')
    tipos_vidrio = request.form.getlist('tipo_vidrio[]')
    acabados = request.form.getlist('acabado[]')
    cantidades = request.form.getlist('cantidad[]')
    esmerilado = request.form.getlist('esmerilado[]')

    for i in range(len(estilos)):
        estilo = estilos[i]
        ancho = float(anchos[i])
        alto = float(altos[i])
        tipo_vidrio = tipos_vidrio[i]
        acabado = acabados[i]
        cantidad = int(cantidades[i])
        esmerilado = esmerilado[i].lower() == "si"

        ventana = Ventana(estilo, ancho, alto, tipo_vidrio, acabado, cantidad, esmerilado)
        ventanas.append(ventana)

    # Calculating the quotation
    cotizacion = Cotizacion(fecha='2024-10-19', cliente=cliente, ventanas=ventanas)
    total = cotizacion.calcular_total()

    # Render the result page with total and breakdown
    return render_template('resultados.html', cliente=cliente, ventanas=ventanas, total=total)

@app.route('/actualizar_precios', methods=['GET', 'POST'])
def actualizar_precios():
    if request.method == 'POST':
        # Actualizar precios de los vidrios solo si el campo no está vacío
        tipo_vidrio = request.form['tipo_vidrio']
        nuevo_precio_vidrio = request.form.get('nuevo_precio_vidrio')
        if nuevo_precio_vidrio:  # Si no está vacío
            precio_anterior_vidrio = Ventana.precios_vidrio[tipo_vidrio]
            Ventana.actualizar_precio_vidrio(tipo_vidrio, float(nuevo_precio_vidrio))
            historial_precios.append({'tipo': 'Vidrio', 'nombre': tipo_vidrio, 'anterior': precio_anterior_vidrio, 'nuevo': float(nuevo_precio_vidrio)})

        # Actualizar precios de los acabados solo si el campo no está vacío
        tipo_acabado = request.form['tipo_acabado']
        nuevo_precio_acabado = request.form.get('nuevo_precio_acabado')
        if nuevo_precio_acabado:  # Si no está vacío
            precio_anterior_acabado = Ventana.precios_acabado[tipo_acabado]
            Ventana.actualizar_precio_acabado(tipo_acabado, float(nuevo_precio_acabado))
            historial_precios.append({'tipo': 'Acabado', 'nombre': tipo_acabado, 'anterior': precio_anterior_acabado, 'nuevo': float(nuevo_precio_acabado)})

        return render_template('precios_exitosos.html')

    return render_template('actualizar_precios.html')

@app.route('/historial_precios')
def ver_historial_precios():
    return render_template('historial_precios.html', historial=historial_precios)

if __name__ == '__main__':
    app.run(debug=True)
