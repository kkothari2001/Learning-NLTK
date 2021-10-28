# Part of Speech Taggin in nltk
# Cool preproceesing B-D

import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer


sample_text = state_union.raw("2006-GWBush.txt")
train_text = state_union.raw("2005-GWBush.txt")

tokenized = PunktSentenceTokenizer(train_text=train_text).tokenize(sample_text)

for sent in tokenized:
    words = nltk.word_tokenize(sent)
    ##############################################
    pos_tagged = nltk.pos_tag(words)
    ##############################################
    print(pos_tagged)
    print()