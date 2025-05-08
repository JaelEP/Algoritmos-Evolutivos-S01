# Importamos la librería NumPy

import numpy as np

# Definimos el presupuesto disponible

presupuesto = 15.00

# Creamos un array con los precios del pasaje por cada medio

precios = np.array([2.50, 3.00, 1.80])

# Calculamos cuántos viajes puede pagar con cada medio

max_viajes = np.floor(presupuesto / precios)

# Identificamos la mayor cantidad de cafés y su índice

cantidad_max = int(max_viajes.max())

indice_max = int(max_viajes.argmax())

# Encontramos el precio mínimo y su índice

precio_min = precios.min()

indice_precio_min = int(precios.argmin())

# Nombres de las cafeterías

nombres = ['Bus', 'Combi', 'Tren']

# Imprimimos los resultados

print("=== Resultados Ejercicio Transporte ===")

for i, nombre in enumerate(nombres):

    print(f"Medio de transporte {nombre}: precio S/ {precios[i]:.2f} → puede pagar {int(max_viajes[i])} viajes")

print(f"\nCon {presupuesto:.2f} puedo pagar como máximo {cantidad_max} viajes con el medio {nombres[indice_max]} (precio mínimo S/ {precio_min:.2f} del medio {nombres[indice_precio_min]}).")