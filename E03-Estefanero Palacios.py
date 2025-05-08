
import pandas as pd

# 1. Construimos el diccionario de datos
datos = {
    'Estudiante': ['Rosa', 'David', 'Elena', 'Mario', 'Paula'],
    'Dias_prestamo': [7, 10, 5, 12, 3]
}

# 2. Convertimos el diccionario en un DataFrame  de Pandas
df = pd.DataFrame(datos)

# 3. Mostramos el DataFrame completo
print("=== DataFrame de Uso de Préstamo de Libros en la Biblioteca ===")
print(df)

# 4. Estadísticas descriptivas de la columna 'Dias_prestamo'
#    describe() devuelve conteo, media, std, min, percentiles y max
stats = df['Dias_prestamo'].describe()
print("\n=== Estadísticas de Dias_prestamo ===")
print(stats)

# 5. Filtramos los estudiantes con un préstamo mayor a 8 dias
#    Creamos un DataFrame con la condición df['Dias_prestamo'] > 8
df_mayor_8 = df[df['Dias_prestamo'] > 8]

# 6. Imprimimos el gasto promedio y la lista de estudiantes con un préstamo mayor a 8 dias
tiempo_promedio = stats['mean']
max_prestamo= stats['max']
lista_altos = df_mayor_8['Estudiante'].tolist()

print(f"\nEl tiempo promedio por estudiante fue de {tiempo_promedio} dias.")
print(f"El tiempo máximo de préstamo fue de {max_prestamo} dias.")
print("Estudiantes que se prestaron un libro por más de 8 dias:")
for alumno in lista_altos:
    print(f" - {alumno}")