from nltk.book import *


def space_out():
    print()
    print()
    print()


space_out()

# print(text1)
# <Text: Moby Dick by Herman Melville 1851>

# There are many ways to examine the context of a text apart from simply reading it. A concordance view shows us every occurrence of a given word, together with some context.

# print(text1.concordance("large"))

# The first time you use a concordance on a particular text, it takes a few extra seconds to build an index so that subsequent searches are fast.

# A concordance permits us to see words in context. What other words appear in a similar range of contexts? We can find out by appending the term similar to the name of the text in question, then inserting the relevant word in parentheses.
# text1.similar("large")
# print()
# text2.similar("large")
