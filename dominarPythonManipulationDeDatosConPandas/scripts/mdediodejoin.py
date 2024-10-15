import pandas as pd

df_datos_personal = pd.DataFrame({
    "id": [283924, 220392, 2393483, 4324344, 323455],
    "nombre": ["Juan", "Maria", "Pedro", "Luis", "Ana"],
    "apellido": ["Perez", "Gomez", "Gonzalez", "Rodriguez", "Diaz"],
    "edad": [30, 25, 35, 40, 52],
    "fecha_nacimiento": ["1990-01-01", "1995-05-12", "1985-12-25", "1980-03-15", "1968-07-20"],
    "empresa": ["IBM", "Google", "Microsoft", "Amazon", "Oracle"],
    "salario": [5000, 6000, 7000, 8000, 9000],
    "codigo_postal": ["10001", "20002", "30003", "40004", "50005"]
})

df_datos_puestos = pd.DataFrame({
    "id": [283924, 2393483, 323455, 4324344],
    "puesto": ["Ingeniero de sistemas", "Diseñadora gráfica", "Contador", "Abogado"],
    "departamento": ["Tecnología", "Diseño", "Finanzas", "Legal"],
    "experiencia": [5, 3, 7, 10]
})

union_df = pd.merge(df_datos_personal, df_datos_puestos, on='id', how='left')
print(union_df)