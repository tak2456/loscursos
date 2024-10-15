import json
import random
from faker import Faker

# Create a Faker instance
fake = Faker()

# Generate 100 random entries
data = []
for _ in range(100):

    first_name = fake.first_name().lower()
    last_name = fake.last_name().lower()
    email = f"{first_name}.{last_name}@example.com"
    id =  random.randint(1000, 9999)
    person = {
        "id": id,
        "nombre": first_name.capitalize(),
        "apellido": last_name.capitalize(),
        "email": email,
        "telefono": fake.phone_number(),
        "direccion": fake.address(),
        "ciudad": fake.city(),
        "pais": fake.country(),
        "edad": fake.random_int(min=18, max=65),
        "codigo_postal": fake.zipcode(),
        "fecha_nacimiento": fake.date_of_birth().isoformat(),
        "empresa": fake.company(),
        "trabajo": fake.job(),
        "salario": fake.random_int(min=1000, max=10000) if id % 5 != 0 else None,
    }
    data.append(person)


# Write to a JSON file
with open('data\\datos.json', 'w') as json_file:
    json.dump(data, json_file, indent=4)

print("Data successfully written to datos.json")
