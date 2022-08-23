# Chunking:
# Chunking involves breaking down paragraphs into smmaler parts/phrases that make contextual sense


from os import stat
import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer


train_text = state_union.raw("2006-GWBush.txt")
example_text = state_union.raw("2005-GWBush.txt")

tokenized = PunktSentenceTokenizer(
    train_text=train_text).tokenize(example_text)
