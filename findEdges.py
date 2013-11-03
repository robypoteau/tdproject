import nltk, os

#Import File
twitterLines  = []
raw = []
thisDir = os.path.dirname(os.path.realpath(__file__))
with open(os.path.join(thisDir, "twitter_raw.txt"), "r") as afile:
    for i in range(0,25):
        raw.append(afile.readline())
        raw[i] = raw[i].decode("utf-8-sig").encode('utf-8')
        #raw = raw
        line_tokens = nltk.word_tokenize(raw[i])
        twitterLines.append(line_tokens)
    #pos_tokens_
#twitterLines contains 2gram 1 append 1 to a list