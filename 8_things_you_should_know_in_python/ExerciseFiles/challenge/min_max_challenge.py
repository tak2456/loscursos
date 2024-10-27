
import string
import os
DICTIONARY = 'dictionary.txt'
base_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(base_dir, DICTIONARY)

letter_scores = {
                    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 
                    'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 
                    'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 
                    'y': 4, 'z': 10
                }

def get_scrabble_dictionary():
    
    """Helper function to return the words in DICTIONARY as a list"""
    with open(file_path, 'rt', encoding='utf-8') as file:
        content = file.read().splitlines()
    return content

def score_word(word) -> int:
    """Return the score for a word using letter_scores.
    If the word isn't in DICTIONARY, it gets a score of 0.""" 
    # use set for faster lookup
    dictionary = set(get_scrabble_dictionary())
    if(word.upper() not in dictionary):
        return 0
    # split the string into an array of characters
    #chracters = list(word.lower())
    #return sum([ letter_scores[c] if c in letter_scores else 0 for c in chracters])

    return sum(letter_scores.get(c.lower(), 0) for c in word)

def remove_punctuation(word):
    """Helper function to remove punctuation from word"""
    table = str.maketrans({char:None for char in word if char in string.punctuation})
    return word.translate(table)

def get_word_largest_score(sentence) -> str:
    """Given a sentence, return the word in the sentence with the largest score."""
    # split sentence to an array of words
    removed = remove_punctuation(sentence)
    words = removed.split()
    scored_words = [(w,score_word(w)) for w in words]
    # get the word with the largest score
    #return max(scored_words , key=lambda w: w[1])[0]

    return max([word for word in removed.split()], key=score_word)
