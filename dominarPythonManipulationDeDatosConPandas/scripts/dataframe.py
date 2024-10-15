import pandas as pd

df_clients = pd.DataFrame({
    "nombre" : ["Pedro Infante", "Maria Lopez", "Jose Perez", "Ana Lopez", "Juan Perez", "Clara Ortiz", "Carlos Torres"],	
    "edad" : [30, 25, 35, 40, 52, 50, 45],
    "ciudad" : ["Buenos Aires", "Lima", "Ciudad de México", "Bogotá", "Santiago", "Caracas", "Quito"],
})


lista_profesion = ["Médico", "Ingeniera civil", "Abogado", "Profesora", "Contador", "Enfermera", "Ingeniero de sistemas"]

df_clients["profesion"] = lista_profesion

print(df_clients)


archive = "data\\clients.csv"
df_clients.to_csv(archive, index=False)
print(f"Archivo guardado en '{archive}'")

print("Nombres en mayúsculas:")
print(df_clients["nombre"].str.upper())


print("Nombres que tienen la palabra Lopez:")
print(df_clients[df_clients["nombre"].str.contains("Lopez", case=False)])

print("Personas con nombre que finalizan con ez")
print(df_clients[df_clients["nombre"].str.endswith("ez")]['nombre'])