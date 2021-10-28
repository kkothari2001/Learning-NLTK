# What are stop words?
# Filler words that don't really add a lot of meaning to the text - filler words
# They might make sense to us, but as far as data analysis is concerned we don't really care.

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

example_sent = "This is an example showing off stop word filtration."


stop_words = set(stopwords.words("english"))

words = word_tokenize(example_sent)
filtered = [word for word in words if word not in stop_words]

print(filtered)
# ['This', 'example', 'showing', 'stop', 'word', 'filtration', '.']
