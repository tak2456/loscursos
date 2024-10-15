import pandas as pd

df_ventas_anuales = pd.DataFrame(
    {
        "mes": ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"],
        "ventas": [10000, 2000, 1500, 3000, 2500, 4000, 35000, 45000, 5000, 6000, 5500, 70000]
    
    }    
)

print(df_ventas_anuales)

valores_atipicos = df_ventas_anuales['ventas'] > 10000
print("Valores atípicos:")
print(valores_atipicos)

valores_atipicos = df_ventas_anuales[df_ventas_anuales['ventas'] > 10000]
print("Valores atípicos:")
print(valores_atipicos)

Q1 = df_ventas_anuales['ventas'].quantile(0.25)
Q3 = df_ventas_anuales['ventas'].quantile(0.75)
IQR = Q3 - Q1

umbral = 1.5
limite_inferior = Q1 - umbral * IQR
limite_superior = Q3 + umbral * IQR

df_valores_atipicos = df_ventas_anuales[
    (df_ventas_anuales['ventas'] < limite_inferior) 
    | (df_ventas_anuales['ventas'] > limite_superior)]

print("Valores atípicos with quantile:")
print(df_valores_atipicos)