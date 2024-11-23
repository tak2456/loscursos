#%%
import sqlite3
import pandas as pd
import os, sys

# Add the project root directory to the Python path
#project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), './'))
#sys.path.insert(0, project_root)

print(os.getcwd())

conn = sqlite3.connect('STAFF.db')

table_name = 'DEPARTMENT'
attribute_list = ['ID', 'NAME', 'MANAGER_ID', 'LOC_ID']

file_path = './DEPARTMENTS.csv'
df = pd.read_csv(file_path, names = attribute_list)

df.to_sql(table_name, conn, if_exists = 'replace', index =False)
print('Table is ready')

# %%
query_statement = f"SELECT * FROM {table_name}"
query_output = pd.read_sql(query_statement, conn)
print(query_statement)
print(query_output)

# %%
insert_statement = f"INSERT INTO {table_name} VALUES (9, 'Quality Control', 30010, 'L0010')"
conn.execute(insert_statement)
conn.commit()
print('Data inserted successfully')
# %%
