import nltk
from nltk.corpus import wordnet


# Use to find Definition of any word
# syn = wordnet.synsets('Boy')
# print(syn[0].definition())

synonyms = []
for syn in wordnet.synsets('man'):
    for lemma in syn.lemmas():
        synonyms.append(lemma.name())
print(synonyms)

antonyms = []
for syn in wordnet.synsets('small'):
    for lemma in syn.lemmas():
        if lemma.antonyms():
            antonyms.append(lemma.antonyms()[0].name())
print(antonyms)