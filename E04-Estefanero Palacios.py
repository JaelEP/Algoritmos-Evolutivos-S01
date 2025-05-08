
import pandas as pd

# 1. Construimos el diccionario de datos
datos = {
    'Dia': ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes'],
    'Gasto': [4.0, 3.5, 5.0, 4.2, 3.8]
}

# 2. Convertimos el diccionario en un DataFrame  de Pandas
df = pd.DataFrame(datos)

# 3. Mostramos el DataFrame completo
print("=== DataFrame de gasto de almuerzo semanal ===")
print(df)

# 4. Estadísticas descriptivas de la columna 'Gasto'
#    describe() devuelve conteo, media, std, min, percentiles y max
stats = df['Gasto'].describe()
print("\n=== Estadísticas de Gasto ===")
print(stats)

# 5. Calcular el gasto promedio y gasto total semanal
gasto_promedio = stats['mean']
gasto_total = df['Gasto'].sum()


# 6. Filtramos los dias que gastó más que el promedio
#    Creamos un DataFrame con la condición df['gasto_total'] > df['gasto_promedio']
df_mayor_promedio = df[df['Gasto'] > gasto_promedio]

# 7. Imprimimos el gasto promedio, gasto toal y la lista de los dias que gastó más que el promedio
lista_altos = df_mayor_promedio['Dia'].tolist()

print(f"\nEl gasto promedio semanal fue de S/ {gasto_promedio:.2f}.")
print(f"El gasto total semanal fue de S/ {gasto_total:.2f}.")
print(f"Dias en los que se gastó más que el promedio (S/ {gasto_promedio:.2f}):")
for alumno in lista_altos:
    print(f" - {alumno}")