from nltk import word_tokenize, sent_tokenize
import nltk
nltk.download('punkt')

sentence = "I am working on a program that needs to create a sentence "
words = word_tokenize(sentence)
print(type(words), len(words))
print(words)
print("!!")
