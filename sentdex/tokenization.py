from nltk.tokenize import sent_tokenize, word_tokenize

#  Common terms in NLP
#  Tokenizing - Grouping things (seperate by words and sentences)
#  Corporus - A body of text ( eg: mdeical journals, speeches)
#  Lexicon - Words and their meanings ( can mean different too, eg lexicons of investors may differ from the layman as meanings can change)


example_text = "Hello Mr. Kothari, how are you? The weather is great and Python is awesome. The sky is pinkish-blue. You should not eat cardboard"

print(sent_tokenize(example_text))
# ['Hello Mr. Kothari, how are you?', 'The weather is great and Python is awesome.', 'The sky is pinkish-blue.', 'You should not eat cardboard']

print()
print(word_tokenize(example_text))
# ['Hello', 'Mr.', 'Kothari', ',', 'how', 'are', 'you', '?', 'The', 'weather', 'is', 'great', 'and', 'Python', 'is', 'awesome', '.', 'The', 'sky', 'is', 'pinkish-blue', '.', 'You', 'should', 'not', 'eat', 'cardboard']

# for i in word_tokenize(example_text):
#     print(i)
