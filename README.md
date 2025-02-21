## Overview

This project demonstrates basic text preprocessing techniques using the Natural Language Toolkit (NLTK) in Python. The script performs the following tasks:

Tokenization: Splitting text into words.

Stopword Removal: Removing common words that do not add much meaning.

Stemming: Reducing words to their root form.

## Example Input:

text = "I really love this product! It works wonderfully and is very easy to use."

## Example Output:

Tokenized Words: ['I', 'really', 'love', 'this', 'product', '!', 'It', 'works', 'wonderfully', 'and', 'is', 'very', 'easy', 'to', 'use', '.']
Filtered Words (No Stopwords): ['really', 'love', 'product', 'works', 'wonderfully', 'easy', 'use']
Stemmed Words: ['realli', 'love', 'product', 'work', 'wonder', 'easi', 'use']


## Features

Uses NLTK for text processing

Supports stopword removal and stemming
