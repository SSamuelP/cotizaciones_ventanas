# Requerimientos del Sistema de Cotización de Ventanas

Este documento especifica los requerimientos funcionales para el sistema de cotización de ventanas.

## Registro de Entidades
 
- El sistema debe permitir el registro de un estilo de ventana con los siguientes atributos: tipo de ventana (O, XO, OXXO, OXO), dimensiones (ancho y alto).
- El sistema debe permitir el registro de una nave con los atributos: tipo de nave (O o X), dimensiones (ancho y alto), tipo de vidrio, acabado, y, si aplica, si es esmerilado, así como la cantidad de ventanas de esa nave.
- El sistema debe permitir el registro de un tipo de vidrio con los atributos: tipo (transparente, bronce, azul) y precio por cm².
- El sistema debe permitir el registro de un acabado de aluminio con los atributos: tipo (pulido, lacado brillante, lacado mate, anodizado) y precio por metro lineal.
- El sistema debe hacer el calculo automatico de elementos adicionales con atributos: esquinas (precio por unidad) y chapas (precio por unidad), si la nave lo permite.
- El sistema debe permitir el registro de un cliente con los atributos: nombre cliente o razón social, telefono, dirección de correo.
- El sistema debe permitir el registro de una cotización con los atributos: fecha, número de cotización, cliente, listado de ventanas, y descuento si corresponde.

## Gestión de Precios

- El sistema debe calcular el costo de cada ventana teniendo en cuenta los siguientes elementos:
  - Precio del aluminio (por centímetro lineal) según el tipo de acabado.
  - Precio del vidrio (por cm²) y costo adicional si el vidrio es esmerilado.
  - Precio de las esquinas (cantidad por ventana).
  - Precio de la chapa si aplica (para naves tipo X).
- El sistema debe aplicar un descuento del 10% si la cantidad de ventanas solicitadas excede las 100 unidades.
Adición: El sistema debe permitir actualizar los precios de los estilos.

## Relaciones entre Entidades

- El sistema debe permitir asociar múltiples estilos de ventanas a un cliente.
- El sistema debe relacionar naves con ventanas, calculando automáticamente sus dimensiones basadas en el ancho y alto de la ventana completa.
- El sistema debe calcular automáticamente el número de esquinas y chapas necesarias para cada ventana según el tipo y cantidad de naves.
- El sistema debe calcular el total de la cotización por cliente.

## Validaciones

- El sistema debe verificar que las dimensiones de las naves sean coherentes con el ancho y alto de la ventana.
- El sistema debe garantizar que el vidrio sea siempre 1.5 cm más pequeño que la nave en cada lado.
- El sistema debe asegurar que el descuento solo se aplique para más de 100 ventanas del mismo diseño.
- El sistema debe garantizar que cada esquina tenga 4 cm en cada lado para un calculo coherente del aluminio y vidrio.

