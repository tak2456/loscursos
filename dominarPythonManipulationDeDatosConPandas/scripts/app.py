import pandas as pd

print(pd.__version__)


# create a list of emails
lista_email = [
    "xxx@gmail.com",
    "xxy@gmail.com",
    "xxz@gmail.com",
    "xxa@gmail.com",
    "xxb@gmail.com",
]

etiquetas_id = [
    100001,
    100002,
    100003,
    100004,
    100005,
]



diccionaryio_empleados = {
    15380: 'Pedro Infante',
    15381: 'Maria Lopez',
    15382: 'Jose Perez',
    15383: 'Ana Lopez',
    15384: 'Juan Perez',
    47130 : 'Clara Ortiz',
    47131 : 'Carlos Torres',
    47132 : 'Rosa Melendez',
    47133 : 'Luis Melendez',
    47134 : 'Elena Domínguez',
    47135 : 'Jorge Domínguez',
    47136 : 'Marta Sánchez',
    47137 : 'Felipe Sánchez',
    47138 : 'Sara García',
    47139 : 'Pablo García',
    47140 : 'Laura González',
    47141 : 'Manuel González',    
    32188 : 'María Hernández',
    32189 : 'Javier Hernández',
    32190 : 'Sonia Blanco',
    32191 : 'Carlos Blanco',
}

serie_email = pd.Series(lista_email, index=etiquetas_id)
print('Hola! Soy el script app.py')
print(serie_email)
#print(f"4th element is '{serie_email[4]}'")
print(f"4th element is '{serie_email[100005]}'")

print()

serie_empleados = pd.Series(diccionaryio_empleados)

print("Serie empleados:")
print(serie_empleados)

print()

serie_ordenada_valores = serie_empleados.sort_values(ascending=True)
print("Serie empleados ordenada por valores:")
print(serie_ordenada_valores)

print()

serie_ordenada_indices = serie_empleados.sort_index(ascending=True)
print("Serie empleados ordenada por indices:")
print(serie_ordenada_indices)

print("Minúsculas:")
print(serie_ordenada_indices.str.lower())

print("Mayúsculas:")
print(serie_ordenada_indices.str.upper())

print("Longitud:")
print(serie_ordenada_indices.str.len())

print("Reemplazar:")
print(serie_ordenada_indices.str.replace('Blanco', 'Negro'))

print("Contiene:")
print(serie_ordenada_indices.str.contains('Blanco'))
