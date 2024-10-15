import pandas as pd

archivo = 'data\\datos.json'
df = pd.read_json(archivo)

print("DataFrame original:")
print(df.sort_values('id'))

total_elementos = df.size
print(f"El DataFrame tiene {total_elementos} elementos")

dimensiones = df.shape
print(f"El DataFrame tiene {dimensiones[0]} filas y {dimensiones[1]} columnas")

filas, columns = df.shape
print(f"El DataFrame tiene {filas} filas y {columns} columnas")


num_dimensions = df.ndim
print(f"El DataFrame tiene {num_dimensions} dimensiones")

print("Eliminar columnas para reducir la dimensionalidad")
df_reduced = df.drop(columns=['fecha_nacimiento', 'empresa', 'codigo_postal'])
print(df_reduced)

print("Eliminar filas para reducir la dimensionalidad")
df_reduced = df_reduced[df_reduced['salario']>9000]

filas, columns = df_reduced.shape
print(f"El DataFrame tiene {filas} filas y {columns} columnas")
print(df_reduced)