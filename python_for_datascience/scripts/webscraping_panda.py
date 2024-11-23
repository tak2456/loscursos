# %%
!pip install lxml
!pip install requests 
!pip install html5lib 
!pip install BeautifulSoup4
#%%
import pandas as pd
from bs4 import BeautifulSoup

#%%




# %%
URL = 'https://en.wikipedia.org/wiki/List_of_largest_banks'
tables = pd.read_html(URL)
df = tables[0]
print(df)
# %%
import pandas as pd
URL = 'https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)'
tables = pd.read_html(URL)
df = tables[2] # the required table will have index 2
print(df)
# %%
html="<!DOCTYPE html><html><head><title>Page Title</title></head><body><h3><b id='boldest'>Lebron James</b></h3><p> Salary: $ 92,000,000 </p><h3> Stephen Curry</h3><p> Salary: $85,000, 000 </p><h3> Kevin Durant </h3><p> Salary: $73,200, 000</p></body></html>"

# %%
soup = BeautifulSoup(html, 'html.parser')
# %%
tags = soup.find_all(['h3', 'b'])
# %%
tags
# %%
soup = BeautifulSoup(html, 'html5lib')
# %%
print(soup.prettify())
# %%
soup.title
# %%
soup.h3
# %%
tag_child=soup.h3.b
tag_child
# %%
tag_object=soup.h3
# %%
tag_object
# %%
tag_object.parent
# %%
tag_object.next_sibling
# %%
tag_child['id']	

# %%
tag_child.attrs
# %%
tag_string=tag_child.string
# %%
tag_string
# %%
type(tag_string)
# %%
unicode_string=str(tag_string)
# %%
unicode_string

# %%
type(unicode_string)
# %%
table="<table><tr><td id='flight'>Flight No</td><td>Launch site</td> <td>Payload mass</td></tr><tr> <td>1</td><td><a href='https://en.wikipedia.org/wiki/Florida'>Florida<a></td><td>300 kg</td></tr><tr><td>2</td><td><a href='https://en.wikipedia.org/wiki/Texas'>Texas</a></td><td>94 kg</td></tr><tr><td>3</td><td><a href='https://en.wikipedia.org/wiki/Florida'>Florida<a> </td><td>80 kg</td></tr></table>"
# %%
table_bs=BeautifulSoup(table, 'html.parser')
# %%
table_bs=BeautifulSoup(table, 'html5lib')
# %%
table_rows=table_bs.find_all('tr')
table_rows
# %%
first_row =table_rows[0]
first_row
# %%
first_row.td
# %%
for i,row in enumerate(table_rows):
    print("row",i,"is",row)
    
# %%
for i,row in enumerate(table_rows):
    print("row",i)
    cells=row.find_all('td')
    for j,cell in enumerate(cells):
        print('colunm',j,"cell",cell)
# %%
list_input=table_bs .find_all(name=["tr", "td"])
list_input
# %%
table_bs.find_all(id="flight")
# %%
list_input=table_bs.find_all(href="https://en.wikipedia.org/wiki/Florida")
list_input
# %%
table_bs.find_all(href=True)
# %%
table_bs.find_all(href=False)

# %%
%%html
<h3>Rocket Launch </h3>

<p>
<table class='rocket'>
  <tr>
    <td>Flight No</td>
    <td>Launch site</td> 
    <td>Payload mass</td>
  </tr>
  <tr>
    <td>1</td>
    <td>Florida</td>
    <td>300 kg</td>
  </tr>
  <tr>
    <td>2</td>
    <td>Texas</td>
    <td>94 kg</td>
  </tr>
  <tr>
    <td>3</td>
    <td>Florida </td>
    <td>80 kg</td>
  </tr>
</table>
</p>
<p>

<h3>Pizza Party  </h3>
  
    
<table class='pizza'>
  <tr>
    <td>Pizza Place</td>
    <td>Orders</td> 
    <td>Slices </td>
   </tr>
  <tr>
    <td>Domino's Pizza</td>
    <td>10</td>
    <td>100</td>
  </tr>
  <tr>
    <td>Little Caesars</td>
    <td>12</td>
    <td >144 </td>
  </tr>
  <tr>
    <td>Papa John's </td>
    <td>15 </td>
    <td>165</td>
  </tr>
  
# %%
two_tables="<h3>Rocket Launch </h3><p><table class='rocket'><tr><td>Flight No</td><td>Launch site</td> <td>Payload mass</td></tr><tr><td>1</td><td>Florida</td><td>300 kg</td></tr><tr><td>2</td><td>Texas</td><td>94 kg</td></tr><tr><td>3</td><td>Florida </td><td>80 kg</td></tr></table></p><p><h3>Pizza Party  </h3><table class='pizza'><tr><td>Pizza Place</td><td>Orders</td> <td>Slices </td></tr><tr><td>Domino's Pizza</td><td>10</td><td>100</td></tr><tr><td>Little Caesars</td><td>12</td><td >144 </td></tr><tr><td>Papa John's </td><td>15 </td><td>165</td></tr>"
# %%
two_tables_bs= BeautifulSoup(two_tables, 'html.parser')
# %%
two_tables_bs.find("table")
# %%
two_tables_bs.find("table",class_='pizza')
# %%
url = "http://www.ibm.com"
# %%
import requests
data  = requests.get(url).text 
# %%
data
# %%
soup = BeautifulSoup(data, 'html5lib')
# %%
for link in soup.find_all('a',href=True):  # in html anchor/link is represented by the tag <a>

    print(link.get('href'))

# %%
for link in soup.find_all('img'):# in html image is represented by the tag <img>
    print(link)
    print(link.get('src'))
# %%
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/datasets/HTMLColorCodes.html"
# %%
data  = requests.get(url).text
# %%
soup = BeautifulSoup(data,"html5lib")

# %%
table = soup.find('table') # in html table is represented by the tag <table>
# %%
#Get all rows from the table
for row in table.find_all('tr'): # in html table row is represented by the tag <tr>
    # Get all columns in each row.
    cols = row.find_all('td') # in html a column is represented by the tag <td>
    color_name = cols[2].string # store the value in column 3 as color_name
    color_code = cols[3].string # store the value in column 4 as color_code
    print("{}--->{}".format(color_name,color_code))
# %%
