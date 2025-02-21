import nltk
from nltk.tokenize import word_tokenize,sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

review="I really love this product! It works wonderfully and is very easy to use."
review=review.lower()


#sentence tokenization
sentences=sent_tokenize(review)
print(sentences)

#word tokenization
words=[word_tokenize(sentence) for sentence in sentences]
print(words)

#flattening words
words=[word for sublist in words for word in sublist]
print(words)

#removing stop words
stop_words=set(stopwords.words("english"))
filtered_words=[word for word in words if word not in stop_words]
print(filtered_words)

#stemming
ps=PorterStemmer()
stemmed_words=[ps.stem(word) for word in filtered_words]
print(stemmed_words)
