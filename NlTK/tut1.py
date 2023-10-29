import matplotlib.pyplot as plt
import nltk
import matplotlib.pyplot as pltt

# To download any ntlk package
# nltk.download()

text = """Hello Hello Everyone I am Omkar. And I am Learning nltk Library here."""
# Tokenization means separate each and every string in the statement
# from nltk.tokenize import word_tokenize
# print(word_tokenize(text))
# Tokenization Successfull

# Sentence tokenization here sentences are separate out from given text
# from nltk.tokenize import sent_tokenize
# print(sent_tokenize(text))


# Frequency Distributor
from nltk.tokenize import word_tokenize

tokenizedWord = word_tokenize(text)
from nltk.probability import FreqDist

# print(FreqDist(tokenizedWord))
fd = FreqDist(tokenizedWord)
print(fd.most_common(3))

# this plot the graph of words with there count in statement
fd.plot(30, cumulative=False)
plt.show()
