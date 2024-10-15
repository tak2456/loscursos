import pandas as pd

ventas = {
    'ventas': [1000, 2000, 1500, 3000, 2500, 4000, 3500, 4500, 5000, 6000, 5500, 7000, 6500],
    'cantidad': [10, 20, 15, 30, 25, 40, 35, 45, 50, 60, 55, 70, 65],
}

print(ventas)

indice = pd.MultiIndex.from_tuples([
    ('Electrodomesticos', 'Laptop', 'En linea'),
    ('Electrodomesticos', 'Tableta', 'En tienda'),
    ('Electrodomesticos', 'Movil', 'En tienda'),
    ('Electrodomesticos', 'Nivera', 'En linea'),
    ('Electrodomesticos', 'Ordenadro', 'En linea'),
    ('Electrodomesticos', 'Auriculaes', 'En linea'),
    ('Ropa', 'Pantalon', 'En tienda'),
    ('Ropa', 'Camiseta', 'En linea'),
    ('Ropa', 'Vestido', 'En tienda'),
    ('Ropa', 'Toalla', 'En tienda'),
    ('Ropa', 'Banador', 'En tienda'),
    ('Hogar', 'Alfombras', 'En linea'),
    ('Hogar', 'Cortinas', 'En linea'),
], names=['Categoria', 'Producto', 'Canal_Ventas'])

df_tienda = pd.DataFrame(ventas, index=indice)
print(df_tienda)


print("Acceder a los datos de un producto:")
print(df_tienda.loc[('Hogar')])
print(df_tienda.xs('En linea', level='Canal_Ventas'))

print("Ordenamiento")
df_ordenamiento = df_tienda.sort_index(axis = 0, level = ['Categoria', 'Producto'], ascending = [True, True])
print(df_ordenamiento)