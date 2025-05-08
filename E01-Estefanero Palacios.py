
# Ejercicio 1:

import numpy as np

# 1. Definimos el presupuesto disponible (S/ 8)

presupuesto = 8.00

# 2. Creamos un array con los precios de café en cada cafetería

#    A: 0.10, B: 0.12, C: 0.08

precios = np.array([0.10, 0.12, 0.08])

# 3. Calculamos cuántas páginas puede fotocopiar en cada copistería

#    np.floor realiza la división y redondea hacia abajo al entero más próximo

max_copias = np.floor(presupuesto / precios)

# 4. Encontramos la mayor cantidad de fotocopias posibles

#    max_copias.max() devuelve el valor máximo de cafés

#    max_copias.argmax() devuelve el índice (0-3) donde se alcanza ese máximo

cantidad_max = int(max_copias.max())

indice_max = int(max_copias.argmax())

# 5. Determinamos el precio mínimo y su índice

precio_min = precios.min()

indice_precio_min = int(precios.argmin())

# 6. Mapeo de índices a nombres de cafetería

nombres = ['A', 'B', 'C']

# 7. Imprimimos los resultados

print("=== Resultados Ejercicio Fotocopias ===")

for i, nombre in enumerate(nombres):

    print(f"Copistería {nombre}: precio S/ {precios[i]:.2f} → puede sacar {int(max_copias[i])} fotocopias")

print(f"\nCon S/ {presupuesto:.2f} obtienes la mayor cantidad de fotocopias ({cantidad_max}) en la copistería {nombres[indice_max]}.")

print(f"El precio más bajo es S/ {precio_min:.2f} en la copistería {nombres[indice_precio_min]}.")