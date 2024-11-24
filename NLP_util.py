################################
#import nltk
#nltk.download('stopwords')
#nltk.download('wordnet')
################################


import numpy as np
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer


def tokenize(data, is_pandas=True, want_lemmatize=True):
    stop_words = set(stopwords.words('english'))
    lemmatizer = WordNetLemmatizer()
    tokens = []
    for text in data:
        tokenized_text = [
            lemmatizer.lemmatize(word) if want_lemmatize else word
            for word in text.split() 
            if (word not in stop_words) and (len(word) > 3)
        ]
        tokens.append(tokenized_text)
    return tokens

