import pandas as pd
import matplotlib.pyplot as plt

df_ventas = pd.DataFrame({
    'productos': ['ordenador', 'tablet', 'impresora', 'monitor', 'tablet', 'movil', 'teclado', 'raton', 'ordenador', 'movil', 'tablet'],
    'ventas': [10000, 2000, 1500, 3000, 2500, 4000, 3500, 4500, 5000, 6000, 5500]
})


print (df_ventas)

df_agrupamiento = df_ventas.groupby('productos')['ventas'].sum().reset_index()

df_agrupamiento.plot(kind='bar', x='productos', y='ventas', color='pink')
plt.title('Gráfico de barras de ventas por producto')
plt.xlabel('Productos')
plt.ylabel('Ventas')
plt.show()
