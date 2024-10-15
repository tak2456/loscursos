import pandas as pd

lista_numerica = [ 1, 20, 25, 30, 36, 40, 49, 50, 60, 64, 70, 80, 81, 89, 90, 100, 101]
serie_numerica = pd.Series(lista_numerica)

print ('Hola! Soy el script numerica.py')
print ("Sumar:")
resultado_suma = serie_numerica + 5
print(resultado_suma)

resultado_suma = serie_numerica.add(6)
print(resultado_suma)


print ("Restar:")
resultado_resta = serie_numerica - 9
print(resultado_resta)

resultado_resta = serie_numerica.subtract(11)
print(resultado_resta)

print ("Multiplicar:")
resultado_multiplicacion = serie_numerica * 2
print(resultado_multiplicacion)
resultado_multiplicacion = serie_numerica.multiply(-2)
print(resultado_multiplicacion)

print ("Dividir:")
resultado_division = serie_numerica / 4
print(resultado_division)
resultado_division = serie_numerica.divide(4)
print(resultado_division)

print ("Mod:")
resultado_mod = serie_numerica % 3
print(resultado_mod)
resultado_mod = serie_numerica.mod(3)
print(resultado_mod)

print ("Potencia:") # Exponente
resultado_potencia = serie_numerica ** 2
print(resultado_potencia)
resultado_potencia = serie_numerica.pow(2)
print(resultado_potencia)

print ("Raiz cuadrada:")
resultado_raiz = serie_numerica ** 0.5
print(resultado_raiz)
resultado_raiz = serie_numerica.pow(0.5)
print(resultado_raiz)
