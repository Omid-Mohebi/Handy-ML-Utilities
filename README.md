# Handy-ML-Utilities

Welcome to the Handy-ML-Utilities repository! This repository is designed to provide a collection of useful utilities for machine learning. The goal is to simplify common tasks and enhance productivity when working with machine learning projects.

## NLP Utilities (`NLP_util.py`)

Currently, the repository includes several NLP utilities that can be used for text processing and feature extraction. Below is a brief overview of the available functions:

### 1. `tokenize(data, is_pandas=True, want_lemmatize=True)`

This function tokenizes the input text data, removes stop words, and optionally lemmatizes the words. 

**Parameters:**
- `data`: A pandas Series or list of strings containing the text data to be tokenized.
- `is_pandas`: A boolean indicating whether the input data is a pandas Series (default is `True`).
- `want_lemmatize`: A boolean indicating whether to lemmatize the tokens (default is `True`).

**Returns:**
- A list of lists containing the processed tokens.

### 2. `word2index(data, starting_index=0)`

This function creates a mapping of words to unique indices.

**Parameters:**
- `data`: A list of lists containing tokenized text data.
- `starting_index`: An integer indicating the starting index for the word mapping (default is `0`).

**Returns:**
- A dictionary mapping each unique word to its corresponding index.

### 3. `vectorize(data, word2idx)`

This function converts the tokenized text data into a word vector representation based on the provided word-to-index mapping.

**Parameters:**
- `data`: A list of lists containing tokenized text data.
- `word2idx`: A dictionary mapping words to their corresponding indices.

**Returns:**
- A NumPy array representing the word vectors.

### 4. `one_hard_encoding(data)`

This function performs one-hot encoding on the input class labels.

**Parameters:**
- `data`: A list or array of class labels.

**Returns:**
- A NumPy array representing the one-hot encoded class labels.

## Installation

To use the utilities in this repository, you need to have Python installed along with the required libraries. You can install the necessary libraries using pip:

```bash
pip install numpy nltk
```

Make sure to download the required NLTK resources by uncommenting the following lines in your code:

```python
import nltk
nltk.download('stopwords')
nltk.download('wordnet')
```

## Usage

Here is a simple example of how to use the provided utilities:

```python
import pandas as pd
from nlp_utilities import tokenize, word2index, vectorize, one_hard_encoding

# Sample data
data = pd.Series(["This is a sample sentence.", "Another example of text processing."])

# Tokenization
tokens = tokenize(data)

# Create word-to-index mapping
word_index = word2index(tokens)

# Vectorization
word_vectors = vectorize(tokens, word_index)

# One-hot encoding
classes = ['class1', 'class2', 'class1']
one_hot = one_hard_encoding(classes)
```

## Contributing

Contributions are welcome! If you have any utilities that you would like to add or improvements to suggest, please feel free to submit a pull request.

---

Stay tuned for more utilities as I continue to expand the Handy-ML-Utilities repository!
