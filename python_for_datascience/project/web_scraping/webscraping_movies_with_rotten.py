#%%
import requests
from bs4 import BeautifulSoup
import pandas as pd
import sqlite3


# Specify the URL of the webpage you want to scrape
url = 'https://web.archive.org/web/20230902185655/https://en.everybodywiki.com/100_Most_Highly-Ranked_Films'
db_name = 'RottenMovies.db'
table_name = 'Top_50'
csv_path = 'output/top_50_rottenfilms.csv'
df = pd.DataFrame(columns=["Average Rank","Film","Year", 'Rotten Tomatoes Score'])
count = 0

# Send an HTTP GET request to the webpage
response = requests.get(url)
html_page = response.text

data = BeautifulSoup(html_page, 'html.parser')

# %%
tables = data.find_all('tbody')
rows = tables[0].find_all('tr')
rows
# %%
for row in rows:
    if count<100:
        col = row.find_all('td')
        if len(col)!=0:
            data_dict = {"Average Rank": col[0].contents[0],
                         "Film": col[1].contents[0],
                         "Year": col[2].contents[0],
                         "Rotten Tomatoes Score": col[3].contents[0]}
            
            if isinstance(data_dict['Year'], str) and data_dict['Year'].isdigit():  # Comprueba si es una cadena numérica
                if(int(data_dict['Year']) >= 2000):
                    df1 = pd.DataFrame(data_dict, index=[0])
                    df = pd.concat([df,df1], ignore_index=True)
            count+=1
    else:
        break
# %%
df
# %%
df.to_csv(csv_path, index=False)
# %%

conn = sqlite3.connect(db_name)
df.to_sql(table_name, conn, if_exists='replace', index=False)
conn.close()
# %%
