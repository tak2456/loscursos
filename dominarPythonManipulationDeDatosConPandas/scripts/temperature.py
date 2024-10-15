from numpy import nan as NaN

import pandas as pd
import matplotlib.pyplot as plt

diccionario_temperaturas = {
    2010: 73,
    2011: 73.2,
    2012: 73.4,
    2013: 73.5,
    2014: NaN,
    2015: 74.4,
    2016: 75.3,
    2017: 75.4,
    2018: 72.5,
    2019: NaN,
    2020: 74.5,
}

serie_temperaturas = pd.Series(diccionario_temperaturas)


mean = serie_temperaturas.mean()
reemplazar_temperaturas = serie_temperaturas.fillna(mean)

print(f"Reemplazar valores faltantes por la media: {mean}")
print(reemplazar_temperaturas)

reemplazar_temperaturas.plot(
    kind='line', 
    marker='o',	
    title='Temperaturas por año del 2010 al 2020',
    xlabel='Año',
    ylabel='Temperatura (F)',
    color='green'
    )

plt.show()