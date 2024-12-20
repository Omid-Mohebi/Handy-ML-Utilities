################################
#import nltk
#nltk.download('stopwords')
#nltk.download('wordnet')
################################


import numpy as np
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import re


def tokenize(data, is_pandas=True, want_lemmatize=True):
    stop_words = set(stopwords.words('english'))
    lemmatizer = WordNetLemmatizer()
    pattern = r'[0-9]'
    tokens = []
    for text in data.apply(str):
        temp_token = []
        for word in text.split():
            if (word not in stop_words) and (len(word) > 3):
                txt = re.sub(pattern, '', word)
                if want_lemmatize:
                    temp_token.append(lemmatizer.lemmatize(txt).lower())
                else:
                    temp_token.append(txt.lower())
        tokens.append(temp_token)
    return tokens


def word2index(data, existing_word2idx={}):
    word2idx = {}
    word2idx.update(existing_word2idx)
    starting_index = len(existing_word2idx)
    counter = starting_index
    for row in data:
        for text in row:
            if text not in word2idx:
                word2idx[text] = counter
                counter += 1

    return word2idx


def vectorize(data, word2idx):
    word_vector = np.zeros((len(data), len(word2idx)))
    i = 0
    for row in data:
        for text in row:
            word_vector[i, word2idx[text]] += 1
        i += 1

    return word_vector
    

def one_hard_encoding(data):
    classes = set(data)
    class_dict = {}
    N = len(data)
    K = len(classes)
    ohe = np.zeros((N, K))
    for i, clas in zip(range(K), classes):
        class_dict[clas] = i
    for i in range(N):
        ohe[i, class_dict[data[i]]] = 1
    return ohe