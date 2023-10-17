from acquire import get_blog_articles, get_news_article
import unicodedata
import re
import json

import nltk
nltk.download('wordnet')
nltk.download('omw-1.4')
from nltk.tokenize.toktok import ToktokTokenizer
from nltk.corpus import stopwords

import pandas as pd


def basic_clean(string_cleaning):
    '''
    basic clean will take in a string and after making all characters lower case and making sure only ASCII characters 
    will return the cleaned string
    '''
    string_cleaning = string_cleaning.lower()
    string_cleaning = re.sub(r"[^a-z0-9'\s]", '', string_cleaning)
    return string_cleaning


def tokenize(string_cleaning):
    '''
    tokenize will take in a string and return the string tokenized
    '''
    tokenizer = nltk.tokenize.ToktokTokenizer()
    return tokenizer.tokenize(string_cleaning, return_str=True)


def stem(string_cleaning):
    '''
    stem will take in a string and return the string after stemming
    '''
    ps = nltk.porter.PorterStemmer()
    stems = [ps.stem(word) for word in string_cleaning.split()]
    spring_cleaning_stemmed = ' '.join(stems)
    return spring_cleaning_stemmed


def lemmatize(string_cleaning):
    '''
    lemmatize will take in a string and return the string after lemmatizing it
    '''
    wnl = nltk.stem.WordNetLemmatizer()
    lemmas = [wnl.lemmatize(word) for word in string_cleaning.split()]
    spring_cleaning_lemmatized = ' '.join(lemmas)
    return spring_cleaning_lemmatized


def remove_stopwords(string_cleaning, extra_words='', exclude_words=''):
    '''
    remove_stopwords will take in a string, any extra words to be removed, and and words to keep, and return the string with stop words removed
    '''
    stopword_list = stopwords.words('english')
    stopword_list = stopword_list.remove(exclude_words)
    stopword_list = [stopword_list] + [extra_words]
    words = string_cleaning.split()
    filtered_words = [w for w in words if w not in stopword_list]
    string_without_stopwords = ' '.join(filtered_words)
    return string_without_stopwords


def create_clean(df, extra_words, exclude_words):
    '''
    create_clean will take a dataframe, and extra words you want removed as stopwords, and any words you'd like excluded
    and will take a column named 'original', and tokenize/clean the data before returning the new dataframe
    '''
    # create new column
    i = 0
    for line in df.original:
        df['clean'] = remove_stopwords(tokenize(basic_clean(df.original[i])),extra_words = extra_words, exclude_words=exclude_words)
        i += 1
    # for loop for clean column to iterate through articles
    i = 0
    for line in df.original:
        df['clean'][i] = remove_stopwords(tokenize(basic_clean(df.original[i])),extra_words = extra_words, exclude_words=exclude_words)
        i += 1
    return df


def create_stemmed(df, extra_words, exclude_words):
    '''
    create_stemmed will take a dataframe, and extra words you want removed as stopwords, and any words you'd like excluded
    and will take a column named 'original', and tokenize/clean/stem the data before returning the new dataframe
    '''
    # create new column
    i = 0
    for line in df.original:
        df['stemmed'] = remove_stopwords(stem(tokenize(basic_clean(df.original[i]))),extra_words = extra_words, exclude_words=exclude_words)
        i += 1
    # for loop for clean column to iterate through articles
    i = 0
    for line in df.original:
        df['stemmed'][i] = remove_stopwords(stem(tokenize(basic_clean(df.original[i]))),extra_words = extra_words, exclude_words=exclude_words)
        i += 1
    return df


def create_lemmatize(df, extra_words, exclude_words):
    '''
    create_lemmatize will take a dataframe, and extra words you want removed as stopwords, and any words you'd like excluded
    and will take a column named 'original', and tokenize/clean/lemmatize the data before returning the new dataframe
    '''
    # create new column
    i = 0
    for line in df.original:
        df['lemmatized'] = remove_stopwords(lemmatize(tokenize(basic_clean(df.original[i]))),extra_words = extra_words, exclude_words=exclude_words)
        i += 1
    # for loop for clean column to iterate through articles
    i = 0
    for line in df.original:
        df['lemmatized'][i] = remove_stopwords(lemmatize(tokenize(basic_clean(df.original[i]))),extra_words = extra_words, exclude_words=exclude_words)
        i += 1
    return df