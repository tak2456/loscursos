import re

def remove_punctuation(words):
    '''Helper function to return a string, removing all punctuations and spaces'''
    return re.sub(r'\W+', '', words)

def is_palindrome(words):
    '''Palindromes are case insensitive, so both radar and Radar are valid'''
    # split words into an array
    words = remove_punctuation(words).lower()
    return words == words[::-1]

    