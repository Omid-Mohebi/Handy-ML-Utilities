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

### 2. `word2index(data, existing_word2idx={})`

This function creates a mapping of words to unique indices.

**Parameters:**
- `data`: A list of lists containing tokenized text data.
- `existing_word2idx`: A dictionary of an existing mapping of words (default is `{}`).

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

## Computer Vision Utilities (`CV_utils.py`)

This repository also includes utilities for computer vision tasks. Below is an overview of the available function:

### 1. `image_preprocessing(data, class_names, path)`

This function processes images and their labels from a specified directory.

**Parameters:**
- `data`: Unused placeholder parameter (can be ignored in current implementation).
- `class_names`: A list of class folder names to process.
- `path`: The path to the parent directory containing the class folders.

**Returns:**
- `images_array`: A NumPy array of the processed images.
- `labels_array`: A NumPy array of the corresponding labels.

**Functionality:**
- Reads images in `.jpg` or `.png` format.
- Converts images to RGB format.
- Resizes images to 128x128 pixels.
- Converts the images and labels into NumPy arrays.

## Installation

To use the utilities in this repository, you need to have Python installed along with the required libraries. You can install the necessary libraries using pip:

```bash
pip install numpy nltk pillow
```

Make sure to download the required NLTK resources by uncommenting the following lines in your code:

```python
import nltk
nltk.download('stopwords')
nltk.download('wordnet')
```

## Usage

Here is a simple example of how to use the provided utilities:

### NLP Utilities Example

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

### Computer Vision Utilities Example

```python
from cv_utils import image_preprocessing

# Define class names and path
class_names = ['cat', 'dog']
path = './dataset'

# Preprocess images and labels
images_array, labels_array = image_preprocessing(None, class_names, path)
```

## Contributing

Contributions are welcome! If you have any utilities that you would like to add or improvements to suggest, please feel free to submit a pull request.

---

Stay tuned for more utilities as I continue to expand the Handy-ML-Utilities repository!

