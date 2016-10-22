import os
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import *


def preprocessing_single_user(dir, user):
    # read a set of tweets from a single user

    # input: username
    # output: a list with tweets after stemming
    tweets = []
    for line in open('output/' + dir + '/'  + user + "_user_timeline.txt"):
        line_filtered = re.sub('"', '', line)
        tweets.append(line_filtered)
    tweets_stemmed = []
    for tweet in tweets:
        tokens = get_tokens(tweet)
        filtered_tokens = [w for w in tokens if w not in stopwords.words('english')]
        stemmer = PorterStemmer()
        stemmed = stem_tokens(filtered_tokens, stemmer)
        tweets_stemmed.append(stemmed)
    return tweets_stemmed


def get_tokens(text):
    lowers = text.lower()
    # Remove the punctuation using the character deletion step of translate
    remove_punctuation_map = dict((ord(char), None) for char in string.punctuation)
    no_punctuation = lowers.translate(remove_punctuation_map)
    tokens = nltk.word_tokenize(no_punctuation)
    return tokens


def stem_tokens(tokens, stemmer):
    stemmed = []
    for item in tokens:
        stemmed.append(stemmer.stem(item))
    return stemmed
