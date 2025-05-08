
import pandas as pd

# 1. Construimos el diccionario de datos
datos = {
    'GB': [1, 2, 5, 10],
    'Precio': [5, 9, 20, 35]
}

# 2. Convertimos el diccionario en un DataFrame  de Pandas
df = pd.DataFrame(datos)

# 3. Calculamos el costo por GB
#    Creamos una nueva columna 'Costo_gb'
df['Costo_gb'] = df['GB'] / df['Precio']

# 4. Mostramos el DataFrame completo
print("=== DataFrame de recarga de datos móviles ===")
print(df)

# 5. Estadísticas descriptivas de la columna 'Costo_gb'
#    describe() devuelve conteo, media, std, min, percentiles y max
stats = df['Costo_gb'].describe()
print("\n=== Estadísticas de Costo_gb ===")
print(stats)

# 6. Imprimimos el paquete más económico en precio por GB
paquete_economico = stats['min']
indice_minimo = df['Costo_gb'].argmin()

print(f"\nEl paquete más económico en precio por GB fue el de {df['GB'][indice_minimo]} GB.")
print(f"Con un precio de {paquete_economico:.2f}.")