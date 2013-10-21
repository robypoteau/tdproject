import nltk

#Import File
twitterLines  = []
with open("C:/Users/Roby/Documents/Python/tdproject/twitter_raw.txt") as afile:
    raw = afile.readline()
    line_tokens = nltk.word_tokenize(raw)
    twitterLines.append(line_tokens)

twitterLines contains 2gram 1 append 1 to a list