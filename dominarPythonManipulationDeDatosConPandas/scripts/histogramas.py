import pandas as pd
import matplotlib.pyplot as plt

archivo = 'data\\datos.json'
df_empleados = pd.read_json(archivo)

print("DataFrame original:")
print(df_empleados.sort_values('id'))


df_empleados['edad'].hist(bins=5, edgecolor='black', grid=False)
plt.title('Histograma de edades')
plt.xlabel('Groupos de Edad')
plt.ylabel('Frecuencia')
plt.show()
