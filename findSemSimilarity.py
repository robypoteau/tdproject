import nltk
#import numpy as np
from nltk.corpus import wordnet as wn

#def sem_similarity(sent1, sent2):
sent1 = "\xe2\x80\x9c@itsss_ervin: I don't understand how I'm so bad at math and I'm Asian\xe2\x80\x9d \xf0\x9f\x98\x82\xf0\x9f\x98\x82\xf0\x9f\x98\x82\xf0\x9f\x91\x8f\xf0\x9f\x91\x8f\xf0\x9f\x91\x8f\xf0\x9f\x91\x8f\t\t\n"
sent2 = '@saaaamanthaa_ samantha is soooo perf like omg \xf0\x9f\x98\xad\xf0\x9f\x98\xad\xf0\x9f\x98\xad\xf0\x9f\x92\x98\xf0\x9f\x92\x81\n'

#Clean up text 
sent1 = sent1.decode('ascii', 'ignore').encode('utf-8')
sent2 = sent2.decode('ascii', 'ignore').encode('utf-8')

#Tokenize text
sent1 = nltk.word_tokenize(sent1)
sent2 = nltk.word_tokenize(sent2)

#Stem text
#porter = nltk.PorterStemmer()
#stem1 = [porter.stem(t) for t in sent1]
#stem2 = [porter.stem(t) for t in sent2]

#Tag tokens with parts of speech
sent1 = nltk.pos_tag(sent1)
sent2 = nltk.pos_tag(sent2)

#Word sense disambiguations
word_sense1 = []
word_sense2 = []

for word in sent1:
    ws = wn.synsets(word[0])
    a = (word[1].lower())[0]
    for sense in ws:
        if(sense.pos != a):
            ws.pop(ws.index(sense))
    word_sense1.append(ws)

for word in sent2:
    ws = wn.synsets(word[0])
    a = (word[1].lower())[0]
    print a
    for sense in ws:
        if(sense.pos != a):
            ws.pop(ws.index(sense))
    word_sense2.append(ws)

#Create a similarity matrix
#sim_mat = np.zeros(len(sent1),len(sent2))

#Add to a file
#return [word_sense1, sent2]