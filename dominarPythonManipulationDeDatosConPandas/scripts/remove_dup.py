import pandas as pd

df_ventas_semestre = pd.DataFrame({
    'mes' : ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Junio', 'Mayo', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'],
    'ventas' : [1000, 2000, 1500, 3000, 2500, 4000, 3500, 4500, 5000, 6000, 5500, 7000, 6500]
})	

print(df_ventas_semestre)

valores_duplicados = df_ventas_semestre.duplicated(subset='mes')
print("Valores duplicados:")
print(valores_duplicados)

valores_duplicados = df_ventas_semestre[df_ventas_semestre.duplicated(subset='mes')]
print("Valores duplicados:")
print(valores_duplicados)


df_ventas_semestre_sin_duplicados = df_ventas_semestre.drop_duplicates(subset='mes')
print("DataFrame sin duplicados:")
print(df_ventas_semestre_sin_duplicados)