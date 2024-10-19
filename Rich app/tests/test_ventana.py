import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from app.ventana import Ventana

@pytest.fixture
def ventana_base():
    return Ventana(estilo="XO", ancho=120, alto=150, tipo_vidrio="Transparente", acabado="Pulido", cantidad=2, esmerilado=False)

def test_calcular_ancho_naves(ventana_base):
    # Caso base: estilo XO, debería dividir en 2 naves
    ancho_nave, naves = ventana_base.calcular_ancho_naves()
    assert naves == 2
    assert ancho_nave == 60  # 120/2

def test_calcular_area_nave(ventana_base):
    # El área de la nave debería calcularse correctamente
    area_nave = ventana_base.calcular_area_nave()
    # (ancho_nave - 3) * (alto - 3) = (60 - 3) * (150 - 3) = 57 * 147
    assert area_nave == 57 * 147

def test_calcular_perimetro_nave(ventana_base):
    # Perímetro fijo con el cálculo ajustado
    perimetro_nave = ventana_base.calcular_perimetro_nave()
    assert perimetro_nave == 2 * (6 + 9)  # 2*(6 + 9) cm fijo

def test_calcular_costo_vidrio(ventana_base):
    # Costo del vidrio transparente
    costo_vidrio = ventana_base.calcular_costo_vidrio()
    area_total = ventana_base.calcular_area_nave() * ventana_base.calcular_ancho_naves()[1]
    costo_por_cm2_transparente = 8.25
    assert costo_vidrio == area_total * costo_por_cm2_transparente

def test_calcular_costo_vidrio_esmerilado():
    ventana = Ventana(estilo="XO", ancho=120, alto=150, tipo_vidrio="Transparente", acabado="Pulido", cantidad=1, esmerilado=True)
    costo_vidrio = ventana.calcular_costo_vidrio()
    area_total = ventana.calcular_area_nave() * ventana.calcular_ancho_naves()[1]
    costo_por_cm2_transparente = 8.25
    # Costo adicional de esmerilado es 5.20 por cm2
    assert costo_vidrio == (area_total * costo_por_cm2_transparente) + (area_total * 5.20)

def test_calcular_costo_acabado(ventana_base):
    # Costo del acabado (Pulido) por cm lineal
    costo_acabado = ventana_base.calcular_costo_acabado()
    perimetro_total = ventana_base.calcular_perimetro_nave() * ventana_base.calcular_ancho_naves()[1]
    costo_por_cm_lineal_pulido = 50700 / 100
    assert costo_acabado == perimetro_total * costo_por_cm_lineal_pulido

def test_calcular_costo_esquinas(ventana_base):
    # Cada nave tiene 4 esquinas, y hay 2 naves en este caso
    costo_esquinas = ventana_base.calcular_costo_esquinas()
    assert costo_esquinas == 4310 * 4

def test_calcular_precio_chapa(ventana_base):
    # El estilo "XO" tiene una "X", así que debería haber una chapa
    costo_chapa = ventana_base.calcular_precio_chapa()
    assert costo_chapa == 16200

def test_calcular_precio_chapa_sin_X():
    # Estilo "O" no debería requerir chapa
    ventana = Ventana(estilo="O", ancho=120, alto=150, tipo_vidrio="Transparente", acabado="Pulido", cantidad=1)
    costo_chapa = ventana.calcular_precio_chapa()
    assert costo_chapa == 0

def test_calcular_precio_total(ventana_base):
    # Test completo para el precio total de una ventana
    precio_total = ventana_base.calcular_precio_total()
    costo_vidrio = ventana_base.calcular_costo_vidrio()
    costo_acabado = ventana_base.calcular_costo_acabado()
    costo_esquinas = ventana_base.calcular_costo_esquinas()
    costo_chapa = ventana_base.calcular_precio_chapa()
    assert precio_total == (costo_acabado + costo_vidrio + costo_esquinas + costo_chapa) * ventana_base.cantidad
