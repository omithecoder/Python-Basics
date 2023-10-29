import nltk

# nltk.download("wordnet")
nltk.download("vader_lexicon")
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.sentiment import SentimentIntensityAnalyzer

text = """Hello EveryOne , I am Going Home. Today I am Playing Cricket with my friends. They are Enjoying the game. 
Our Oponents are trying to win this match. But we are also playing well today and we can win today."""
demowords = {"play", "playing", "programming", "codding", "helping", "fight", "caught", "catch", "kill", "killing",
             "killed", "broken", "breaking", "ran"}

# lemmatizer = WordNetLemmatizer()
# stemmer = PorterStemmer()
# for word in demowords:
#     print(word, "=>", stemmer.stem(word), "=>", lemmatizer.lemmatize(word, "v"))

# This convert any type of verb means verb in any tense into simple tense both stemmer and lemmatizer but according
# to output observation lemmatizer is very accurate than stemmer




# Sentimental Analysis:
sia = SentimentIntensityAnalyzer()
print(sia.polarity_scores("I had an amazing dining experience at this restaurant. The food was delicious, the staff was attentive, and the atmosphere was cozy. I'll definitely be coming back."))