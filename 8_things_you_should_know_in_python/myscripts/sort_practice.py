#%%
class Country:
    def __init__(self, name, population):
        self.name = name
        self.population = population    
    def __repr__(self):
        return f'Country({self.name}, {self.population})'

country_list = [
                Country('Taiwan', 24_000_000),
                Country('Portugal', 10_000_000), 
                Country('Netherlands', 17_500_000), 
                Country('Nigeria', 198_000_000), 
                Country('Jordan', 10_000_000), 
                Country('Nepal', 30_000_000), 
                Country('Niger', 24_000_000), 
                Country('Japan', 128_000_000)
]

iso = [('Taiwan', 'iso24000000'), ('Portugal', 'iso10000000'), ('Netherlands', 'iso17500000'), ('Nigeria', 'iso198000000'), ('Jordan', 'iso10000000'), ('Nepal', 'iso30000000'), ('Niger', 'iso24000000'), ('Japan', 'iso128000000')]
# %%
print('sorted by population reverse')
sorted(country_list, key=lambda x: x.population, reverse=True)

# %%
print('sorted by population minus')
sorted(country_list, key=lambda x: -x.population)
# %%
sorted(country_list, key=lambda x: (-x.population, x.name))
# %%
sorted(iso, key=lambda x: int(x[1][3:]))
# %%
[(c,int(i[3:])) for c,i in iso]
# %%
class Country:
    def __init__(self, name, population):
        self.name = name
        self.population = population    
    def __repr__(self):
        return f'Country({self.name}, {self.population})'
    def __eq__(self, other):
        return f'Country({self.name}, {self.population})' == f'Country({other.name}, {other.population})'

country_list = [
                Country('Taiwan', '24000000iso'),
                Country('Portugal', '10000000iso'), 
                Country('netherlands', '17500000iso'), 
                Country('nigeria', '198000000iso'), 
                Country('jordan', '10000000iso'), 
                Country('nepal', '30000000iso'), 
                Country('niger', '24000000iso'), 
                Country('japan', '128000000iso')
]

def get_sorted():
    """Return the country list so that it is sorted first by population 
    and then alphabetically by country name.""" 
    return sorted(country_list, key=lambda x: (int(x.population[:-3]), x.name.lower()))
# %%
[(x.name, x.population[:-3]) for x in country_list]
# %%
get_sorted()
# %%

def test_sorted():
    expected = [
                Country('jordan', '10000000iso'), 
                Country('Portugal', '10000000iso'), 
                Country('netherlands', '17500000iso'), 
                Country('niger', '24000000iso'), 
                Country('Taiwan', '24000000iso'), 
                Country('nepal', '30000000iso'), 
                Country('japan', '128000000iso'), 
                Country('nigeria', '198000000iso')
                ]
    actual = get_sorted()
    assert actual == expected
test_sorted()    
# %%
import string
[ord(char) for char in string.ascii_lowercase]
[ord(char) for char in string.ascii_uppercase]
# %%
test = ('11','','yes','10.2')
all(test)# %%

# %%
### '0' is TRUE!!!
### 'False' is TRUE!!!
### 'False' => True
### 0 => False
### '' => False
### False => False
### None => False
### 0 => True
test = ['False', 0, '', False, None, '0']
any(test)
for t in test:
    print(f'{t} => {bool(t)}')

# %%
test1 = (False, '0', '')
test2 = ('False', 0, '')
test3 = (False, 0, 'False')
test4 = (False, 0, '')
print([any(test1), any(test2), any(test3), any(test4)])
print('lets check individual elements:')
for t in [test1, test2, test3, test4]:
    print([bool(x) for x in t])

# %%
test = ('11','','yes','10.2')
all(test)
# %%
dogs=('Jim','Pablo','Moa')
cats=('Al','Tina','Sasha','Pierre')
pairs=list(zip(dogs,cats))
ndogs, ncats = zip(*pairs)
ncats
# %%
words = ['Oslocious', 'Oslo', 'Oslos', 'Ostrich', 'Oslaxxx']
sorted(words)
# %%
