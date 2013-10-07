import nltk

#Import File
with open("C:\Users\Roby\Documents\Python\tdproject\twitter_raw.txt") as afile
raw = afile.read()
tokens = nltk.word_tokenize(raw)

#Calculate n-grams
nltk.bigrams(tokens)

#find top five or 10

