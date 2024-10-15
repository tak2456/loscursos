import pandas as pd

#pd.set_option('display.max_columns', None)
#pd.set_option('display.max_rows', None)

archivo = 'data\\datos.json'
df = pd.read_json(archivo)

print(df.sort_values('id'))


num_filas, num_columnas = df.shape
print(f"El DataFrame tiene {num_filas} filas y {num_columnas} columnas")

valores_faltantes_colmnas = df.isna().sum()
print("Valores faltantes por columna:")
print(valores_faltantes_colmnas)

media_salarios = df['salario'].mean(skipna=True)
print(f"Media de salarios: {media_salarios}")

print("Reemplazar valores faltantes por la media")
df['salario'] = df['salario'].fillna(media_salarios)
print(df)


valores_faltantes_colmnas = df.isna().sum()
print("Valores faltantes por columna:")
print(valores_faltantes_colmnas)


df_reduced = df.drop(columns=['fecha_nacimiento', 'empresa', 'codigo_postal'])

print(df_reduced)

df_reduced = df_reduced.drop(index=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print(df_reduced)