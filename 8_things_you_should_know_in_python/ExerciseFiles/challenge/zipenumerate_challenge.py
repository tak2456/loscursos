years = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]
births = [723_165, 723_913, 729_674, 698_512, 695_233, 697_852, 696_271, 679_106, 657_076, 640_370]

def annual_births_average(year=years, births=births):
    '''Return a list of tuples with each entry in this format
       (year, birth, running_average)
       Round the running_average to the nearest integer. 
    '''  
    zip_births = zip(years, births)
    running_average = 0
    result = []
    for i, year_birth in enumerate(zip_births, start=0):
          running_average = (running_average * i + year_birth[1]) / (i + 1) 
          result.append((year_birth[0], year_birth[1], round(running_average)))
    return result
    
