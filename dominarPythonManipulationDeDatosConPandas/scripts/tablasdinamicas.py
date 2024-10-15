import pandas as pd

df_ventas = pd.DataFrame({
    'producto': ['Ordenador', 'Impresora', 'Monitor', 'Tablet', 'Smartphone', 'Smartwatch', 'Altavoces', 'Auriculares', 'Vestido', 'Camiseta', 'Alfombras', 'Cortinas'],
    'categoria': ['Informática', 'Informática', 'Informática', 'Informática', 'Telefonía', 'Wearables', 'Audio', 'Audio', 'Ropa', 'Ropa', 'Hogar', 'Hogar'],
    "ventas": [10000, 27000, 71500, 37000, 72500, 40700, 35700, 74500, 57000, 76000, 55700, 27000],
})

print(df_ventas)

df_tabla_dinamica = df_ventas.pivot_table(index='categoria', columns='producto', values='ventas', aggfunc='sum')

print(df_tabla_dinamica)