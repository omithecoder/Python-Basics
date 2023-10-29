import nltk
# nltk.download('stopwords')

text = """Hello Everyone I am Omkar. I am 20 Years Old. here I am Learning NLTK library in Python."""

from nltk.corpus import stopwords
stop_words = stopwords.words('english')
# print(stop_words)

from nltk.tokenize import word_tokenize,sent_tokenize
tokenized_words = word_tokenize(text)
# print(tokenized_words)

tokenized_words_without_stopword =[]
for word in tokenized_words:
    if word not in stop_words:
        tokenized_words_without_stopword.append(word)

print(tokenized_words_without_stopword)
print("StopWords Removed => ",set(tokenized_words)-set(tokenized_words_without_stopword))
print("Tokenized word which include all words => ",tokenized_words)
print("Tokenized word without stopwords => ",tokenized_words_without_stopword)

