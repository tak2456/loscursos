import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df_estudiantes = pd.read_csv('data\\estudiantes.csv')

print("DataFrame original:")
print(df_estudiantes)

matriz_correlacion = df_estudiantes.corr()

correlation_promedio = matriz_correlacion['promedio']
print("Correlación del promedio obtenido en el curso")
print(correlation_promedio)

sns.heatmap(matriz_correlacion, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Matriz de Correlación')
plt.show()