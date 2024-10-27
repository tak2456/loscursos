import string

def contains_punctuation(input_str):
    ''' Return True if the input_str contains punctuations.
    Return False otherwise'''
    #return any([char in string.punctuation for char in input_str])    
    return any(char in string.punctuation for char in input_str)
