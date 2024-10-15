import pandas as pd

diccionaryio_empleados = {
    15380: 'Pedro Infante',
    15381: 'Maria Lopez',
    15382: 'Jose Perez',
    15383: 'Ana Lopez',
    0: None,
    15384: 'Juan Perez',
    20000: None,
    47131 : 'Carlos Torres',
    47139 : 'Pablo García',
    47140 : 'Laura González',
    47141 : 'Manuel González',    
    99999: None,
    9999: None,
    999: None,
    32188 : 'María Hernández',
    32190 : 'Sonia Blanco',
    32191 : 'Carlos Blanco',
}

serie_empleados = pd.Series(diccionaryio_empleados)
print(serie_empleados)

# Verificar si hay valores faltantes
print(serie_empleados.isnull())
print()
print(serie_empleados.isna())

# Total de valores faltantes
print(f"total de valores faltantes: {serie_empleados.isnull().sum()}")


print("Eliminar registros")
eliminar_registros = serie_empleados.dropna()
print(eliminar_registros)

print("Reemplazar valores faltantes por 'Desconocido'")
reemplazar_valores = serie_empleados.fillna('Desconocido')
print(reemplazar_valores)
