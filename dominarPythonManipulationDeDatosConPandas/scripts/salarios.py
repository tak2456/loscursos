import pandas as pd

salariosAnuales = [ 50230.0, 55123.0, 75020.0, 61200.0, 73400.0, 870000.0, 9520.0 ]
serie_salarios = pd.Series(salariosAnuales)
print (serie_salarios)

print("Total de salarios anuales:")
print(serie_salarios.sum())

print("Promedio de salarios anuales:")
print(serie_salarios.mean())

print("Desviación estándar de salarios anuales:")
print(serie_salarios.std())

print("Mínimo salario anual:")
print(serie_salarios.min())

print("Máximo salario anual:")
print(serie_salarios.max())

print("Salarios anuales ordenados:")
print(serie_salarios.sort_values())

print("Salarios anuales ordenados de forma descendente:")
print(serie_salarios.sort_values(ascending=False))

print("Saraio mediana")
print(serie_salarios.median())