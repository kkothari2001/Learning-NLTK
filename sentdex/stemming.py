# Stemming:
# Finding the root of a word or the stem of the word
# Eg. riding, rode, rid etc may have the same root i.e. ride

# Need for stemming is so that we can extract the meaning of
# the word more easily withouth differentiating the above words
# as seperate words


# I was riding in the car.
# I was taking a ride in the car.
# Here the words mean the same thing

from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

ps = PorterStemmer()

example_words = ["python", "pythoner", "pythoning",
                 "pythonic", "pythoned", "pythonly"]

print([ps.stem(w) for w in example_words])
# ['python', 'python', 'python', 'python', 'python', 'pythonli']

example_sentence = "It is very important to be pythony while you are pythoning with python. All pythoners have pythoned poorly atleast once"

print([ps.stem(w) for w in word_tokenize(example_sentence)])
# ['it', 'is', 'veri', 'import', 'to', 'be', 'pythoni', 'while', 'you', 'are', 'python', 'with', 'python', '.', 'all', 'python', 'have', 'python', 'poorli', 'atleast', 'onc']
