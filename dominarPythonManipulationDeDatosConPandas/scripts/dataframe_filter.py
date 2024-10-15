import pandas as pd

archivo = 'data\\datos.json'
df_empleados = pd.read_json(archivo)

print("DataFrame original:")
print(df_empleados.sort_values('id'))

df_empleados = df_empleados[df_empleados['salario'] > 2000]
print("Empleados con salario mayor a 2000:")
print(df_empleados.sort_values('salario'))
