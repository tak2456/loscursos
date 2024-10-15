import pandas as pd

# dos products y 6 meses
df_ventas_semestre = pd.DataFrame({
    'productos': ['computador', 'telefono','computador', 'telefono','computador', 'telefono','telefono','computador', 'telefono','computador', 'telefono', 'computador'],
    'mes' : ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio'],
    'ventas' : [1000, 2000, 1500, 3000, 1500, 1600, 3500, 4500, 5000, 2000, 5500, 2000],  
})


print("DataFrame original:")
print(df_ventas_semestre)


#df_restructurado = df_ventas_semestre.pivot_table(index='mes', columns='productos', values='ventas')
df_restructurado = df_ventas_semestre.pivot(index='mes', columns='productos', values='ventas')
print("DataFrame restructurado:")
print(df_restructurado)

grupos = df_ventas_semestre.groupby(['productos'])
resultados = grupos.agg({'ventas': ['sum', 'mean', 'max', 'min']})
print("Resultados:")
print(resultados)


print("Estadísticas de ventas por producto:")
print(df_ventas_semestre.describe())

print()

print("Medidas de tendencia central:")
print(f"Media: {df_ventas_semestre['ventas'].mean()}")
print(f"Mediana: {df_ventas_semestre['ventas'].median()}")
print(f"Moda: {df_ventas_semestre['ventas'].mode()}")

