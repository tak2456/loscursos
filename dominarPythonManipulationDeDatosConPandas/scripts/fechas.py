import pandas as pd
import matplotlib.pyplot as plt

df_ventas = pd.DataFrame({
    'fecha': pd.to_datetime(['2020-01-01', '2020-02-01', '2020-03-01', '2020-04-02', '2020-05-01']),
    'ventas': [5040, 2400, 4150, 4300, 2040]
})

print("DataFrame original:")
print(df_ventas)

df_ventas['Año'] = df_ventas['fecha'].dt.year
df_ventas['Mes'] = df_ventas['fecha'].dt.month
df_ventas['Día'] = df_ventas['fecha'].dt.day

print("DataFrame con columnas de año, mes y día:")
print(df_ventas)


print("Filtro de fechas:")
fecha_inicio = '2020-03-01'
fecha_fin = '2020-04-30'

df_filtro_fecha = df_ventas[(df_ventas['fecha'] >= fecha_inicio) & (df_ventas['fecha'] <= fecha_fin)]
print(df_filtro_fecha)

df_ventas.set_index('fecha', inplace=True)
df_ventas['ventas'].plot(title='Serie de tiempo de ventas', xlabel='Fecha', ylabel='Ventas', color='green')
plt.show()
