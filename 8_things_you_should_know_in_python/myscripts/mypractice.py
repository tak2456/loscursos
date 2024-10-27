#%%

mylist = []
for i in 'anxiety':
    print (i)
    mylist.append(i)

print (mylist)
print  (''.join(i for i in 'anxiety'))
# %%
[i.upper() for i in 'anxiety']

# %%
myset={3,1,2,6,4,5} 
makelist = lambda i:list(i)
myset=makelist(myset)
myset # [1, 2, 3, 4, 5, 6], ordred list

list(map(lambda x: x**2, myset)) # [1, 4, 9, 16, 25, 36]

# This code first takes a lambda expression: 
# For each value i, it returns i and maps this on each value in the set myset. 
# Next, it converts this into a python list and prints it.
list(map(lambda i:i, myset))

list(myset)
# %%
[i for i in range(10) if i%2!=0]

# %%
# format: [expression for item in iterable if condition]
[[i*j for j in range(1,10)] for i in range(1,10)]
# %%
# list contains a to z from ascii_lowercase
import string
alphabet = list(string.ascii_lowercase)
# concatenating the alphabets
print (alphabet)
[i in alphabet for i in 'anxiety']
all([i in alphabet for i in 'anxiety'])

print  (''.join(i for i in alphabet))
# generator
print ('generator')
all(i in alphabet for i in 'anxiety')

# %%
[x ** 2 for x in range(7) if x % 2 == 0]
# %%
nums = [1, 2, 3, 4, 5]
letters = ['a', 'b', 'c', 'd', 'e']
num_letters = [(n, l) for n in nums for l in letters]
print(num_letters)

# %%

dict_comp = {x:chr(65+x) for x in range(1, 11)}
type(dict_comp)
print(dict_comp)
# %%

set_comp = {x ** 3 for x in range(10) if x % 2 == 0}
type(set_comp)
print(set_comp)
# %%
hasattr(str, '__iter__')
hasattr(bool, '__iter__')
hasattr(list, '__iter__')
hasattr(float, '__iter__')
# %%
simple_list = [1, 2, 3, 4, 5]
my_iterator = iter(simple_list)
print(my_iterator)
next(my_iterator)
next(my_iterator)
next(my_iterator)
next(my_iterator)
next(my_iterator)
next(my_iterator)

# %%
def my_gen():
    for x in range(5):
        yield x

gen_expr = (x for x in range(5))
for x in gen_expr:
    print(x)
# %%
for x in (x for x in range(10)):
    print(f"{x}: {x * x * x}")

# %%
from sys import getsizeof
list_comp = [x ** 2 for x in range(10000) if x % 2 == 0]
print(list_comp)
gen_exp = (x ** 2 for x in range(10000) if x % 2 == 0)
print(gen_exp)

print(f'size of list:{getsizeof(list_comp)}')
print(f'size of list:{getsizeof(gen_exp)}')
# %%
# there are different ways to provide Python ‘generator to list’ conversion.
gen = (x for x in range(10))
# 1. Using list comprehension
print('list comprehension')
print([x for x in gen])
# 2. Using the list() function
print('list function')
gen = (x for x in range(10))
print(list(gen))
# 3. Using the * operator
print ('* unpack operator')
gen = (x for x in range(10))
print([*gen])

gen = (x for x in range(10))
print(*gen)

# %%
def contains_digit(input_str):
    for char in input_str:
        if char.isdigit():
            return True
    return False

assert contains_digit('This sentence does not contain any digits') == False
assert contains_digit('But th15 0ne d0e5') == True
assert contains_digit('123-456-7890')
print('Passed all tests ...')

# %%
def contains_digit(input_str):
    return any([char.isdigit() for char in input_str])
        
assert contains_digit('This sentence does not contain any digits') == False
assert contains_digit('But th15 0ne d0e5') == True
assert contains_digit('123-456-7890')
print('Passed all tests ...')
# %%

# %%
def contains_digit(input_str):
    return any(char.isdigit() for char in input_str)
        
assert contains_digit('This sentence does not contain any digits') == False
assert contains_digit('But th15 0ne d0e5') == True
assert contains_digit('123-456-7890')
print('Passed all tests ...')
# %%

import string

def contains_punctuation(input_str):
    ''' Return True if the input_str contains punctuations.
    Return False otherwise'''
    #return any([char in string.punctuation for char in input_str])    
    return any(char in string.punctuation for char in input_str)

assert contains_punctuation('Readability counts.') 
assert contains_punctuation('If the implementation is hard to explain, it\'s a bad idea.')
assert contains_punctuation('There should be one-- and preferably only one --obvious way to do it.')
assert contains_punctuation('Errors should never pass silently') == False
assert contains_punctuation('Simple is better than complex') == False
print('Passed all tests ...')

# %%
False
'False'
# %%
countries = ['Netherlands', 'Nigeria', 'Jordan', 'Nepal', 'Niger', 'Japan']
for index in range(len(countries)):
    print(f'{index+1}. {countries[index]}')

'''
Expected output:
1. Netherlands
2. Nigeria
3. Jordan
4. Nepal
5. Niger
6. Japan
'''

print('\nJust print')
print(countries)
print('\nEnumerate with for loop:')
for index, country in enumerate(countries, start=0):
    print(f'{index}. {country} -enumerate')

print('\nFor loop:')
for c in sorted(countries):
    print(c)

for index, country in sorted(enumerate(countries, start=0), key=lambda x: x[1], reverse=True):
    print(f'{index}. {country} -enumerate-sorted')
# %%
countries = ['Netherlands', 'Nigeria', 'Jordan', 'Nepal', 'Niger', 'Japan', 'Korea', 'China', 'Spain']
for index, country in sorted(enumerate(countries, start=0), key=lambda x: x[1], reverse=False):
    print(f'{index}. {country} -enumerate-sorted')

print('now reverse')
for index, country in sorted(enumerate(countries, start=0), key=lambda x: x[1], reverse=True):
    print(f'{index}. {country} -enumerate-sorted')    
# %%
countries = ['Netherlands', 'Nigeria', 'Jordan', 'Nepal', 'Niger', 'Japan']
capitals = ['Amsterdam', 'Abuja', 'Amman', 'Kathmandu', 'Niamey', 'Tokyo', 'Seoul']


for country, capital in zip(countries, capitals):
    print(f'The capital city of {country} is {capital}')

print('zip_longest')
from itertools import zip_longest
for country, capital in zip_longest(countries, capitals, fillvalue='Unknown'):   
    print(f'The capital city of {country} is {capital}')

print ('unzip')
z = zip(countries, capitals)
print(f'z is {z}')
pairs = list(z)
print(f'print paris is {pairs}')
country, capital = zip(*pairs)
print(country)
print(capital)

# %%
years = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]
births = [723_165, 723_913, 729_674, 698_512, 695_233, 697_852, 696_271, 679_106, 657_076, 640_370]

def test_output():
    year = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]
    births = [723_165, 723_913, 729_674, 698_512, 695_233, 697_852, 696_271, 679_106, 657_076, 640_370]
    run_avg = [723165, 723539, 725584, 718816, 714099, 711392, 709231, 705466, 700089, 694117]
    expected = list(zip(year, births, run_avg))
    actual = annual_births_average(year, births)
    assert expected == actual

# def annual_births_average(year=years, births=births):
#     '''Return a list of tuples with each entry in this format
#        (year, birth, running_average)
#        Round the running_average to the nearest integer. 
#     '''  
#     zip_births = zip(years, births)
#     running_average = 0
#     result = []
#     for i, year_birth in enumerate(zip_births, start=0):
#           running_average = (running_average * i + year_birth[1]) / (i + 1) 
#           result.append((year_birth[0], year_birth[1], round(running_average)))
#     return result

# Solution
# def annual_births_average(year=years, births=births):
#     '''Return a list of tuples with each entry in this format
#        (year, birth, running_average)
#        Round the running_average to the nearest integer. 
#     '''   
#     result = []
#     sum_ = 0
#     for index, (year, births) in enumerate(zip(year, births), start=1):
#         sum_ += births
#         result.append((year, births, round(sum_/index)))
#     return result    

def annual_births_average(year=years, births=births):
    return [(year, birth, round(sum(births[:index + 1]) / (index + 1)))
            for index, (year, birth) in enumerate(zip(years, births))]

# Explanation of births[:index + 1]
# births[:index + 1] is a slice of the births list.
# index + 1 is the endpoint of this slice, which means that Python will take elements from the start of births up to, but not including, index + 1.
# Effectively, births[:index + 1] creates a sublist containing elements from the start of births up to and including the element at position index.

def test_output():
    year = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]
    births = [723_165, 723_913, 729_674, 698_512, 695_233, 697_852, 696_271, 679_106, 657_076, 640_370]
    run_avg = [723165, 723539, 725584, 718816, 714099, 711392, 709231, 705466, 700089, 694117]
    expected = list(zip(year, births, run_avg))
    actual = annual_births_average(year, births)
    assert expected == actual

test_output()
# %%
small = [100, 200, 300, 400, 500]
[(x, index, small[:index], sum(small[:index])) for index, x in enumerate(small) ]
# %%
countries = ['Netherlands', 'Nigeria', 'Jordan', 'Nepal', 'Niger', 'Japan', 'Korea', 'China', 'Spain']
# in place modification
countries.reverse()
print(countries)


# %%
countries = ['Netherlands', 'Nigeria', 'Jordan', 'Nepal', 'Niger', 'Japan', 'Korea', 'China', 'Spain']
# slicing to reverse
countries[::-1]
countries
# %%
countries = ['Netherlands', 'Nigeria', 'Jordan', 'Nepal', 'Niger', 'Japan', 'Korea', 'China', 'Spain']
c = [i for i in reversed(countries)]
print (c)
tuple(countries)[::-1]
# %%
list((i for i in range(10)))
# %%
import re

def remove_punctuation(words):
    '''Helper function to return a string, removing all punctuations and spaces'''
    return re.sub(r'\W+', '', words)

def is_palindrome(words):
    '''Palindromes are case insensitive, so both radar and Radar are valid'''
    # split words into an array
    words = remove_punctuation(words).lower()
    return words == words[::-1]



assert is_palindrome('sagas')
assert is_palindrome('Radar')
assert is_palindrome('Was it a cat I saw?')
assert is_palindrome('Eva, can I see bees in a cave?')
assert is_palindrome('Red rum, sir, is MURDER!!')

assert is_palindrome("This should not not work") == False
assert is_palindrome('radars') == False    

print('palindrome test passed!!!')
# %%
countries = ['Netherlands', 'Nigeria', 'Jordan', 'Nepal', 'Niger', 'Japan']
population = [17_500_000, 198_000_000, 10_000_000, 30_000_000, 24_000_000, 128_000_000]

max(population)
min(population)
max(countries)
min(countries)
# %%
print(f'min :{min(zip(countries, population))}')
print(f'min w lambda: {min(zip(countries, population), key=lambda x:x[1])}')
print(f'tuple order: {min(zip(population, countries))}');

# %%
