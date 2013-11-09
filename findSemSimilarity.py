import nltk
#import numpy as np
from nltk.corpus import wordnet as wn
wnl = nltk.stem.WordNetLemmatizer()

def compare(list1, list2):
    list3 = set(list1) & set(list2)
    return len(list3)

def rmv_contractions(token):
    if(token == "n't"):
        token = 'not'
    elif(token == "'m"):
        token = "am"
    elif(token == "'ve"):
        token = "have"
    elif(token == "'ll"):
        token = 'will'
    elif(token == "'re"):
        token = 'are'
    elif(token == "'d"):
        token = "would"
    return token

#def sem_similarity(sent1, sent2):
sent1 = "\xe2\x80\x9c@itsss_ervin: I don't understand how I'm so bad at math and I'm Asian\xe2\x80\x9d \xf0\x9f\x98\x82\xf0\x9f\x98\x82\xf0\x9f\x98\x82\xf0\x9f\x91\x8f\xf0\x9f\x91\x8f\xf0\x9f\x91\x8f\xf0\x9f\x91\x8f\t\t\n"
sent2 = '@saaaamanthaa_ samantha is soooo perf like omg \xf0\x9f\x98\xad\xf0\x9f\x98\xad\xf0\x9f\x98\xad\xf0\x9f\x92\x98\xf0\x9f\x92\x81\n'

#Clean up text 
sent1 = sent1.decode('ascii', 'ignore').encode('utf-8')
sent2 = sent2.decode('ascii', 'ignore').encode('utf-8')

#Tokenize text
sent1 = nltk.tokenize.TreebankWordTokenizer().tokenize(sent1.lower())
sent2 = nltk.tokenize.TreebankWordTokenizer().tokenize(sent2.lower())

#Remove Contractions
sent1 = [rmv_contractions(token) for token in sent1]

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
    a = (word[1].lower())[0]
    if(a == 'n'):
        ws = wn.synsets(wnl.lemmatize(word[0]), wn.NOUN)
    elif(a == 'v'):
        ws = wn.synsets(wnl.lemmatize(word[0]), wn.VERB)
    elif(a == 'j'):
        ws = wn.synsets(wnl.lemmatize(word[0]), wn.ADJ)
    else:
        ws = wn.synsets(wnl.lemmatize(word[0]))
    if(ws != []):
        word_sense1.append(ws)

#Word sense disambiguagtion
for word in sent2:
    a = (word[1].lower())[0]
    if(a == 'n'):
        ws = wn.synsets(wnl.lemmatize(word[0]), wn.NOUN)
    elif(a == 'v'):
        ws = wn.synsets(wnl.lemmatize(word[0]), wn.VERB)
    elif(a == 'j'):
        ws = wn.synsets(wnl.lemmatize(word[0]), wn.ADJ)
    else:
        ws = wn.synsets(wnl.lemmatize(word[0]))
    if(ws != []):
        word_sense2.append(ws)

#gloss matrix
gloss1 = []
for word in word_sense1:
    element = []
    for synonym in word:
        defn = synonym.definition
        '''
        hype = synonym.hypernyms()
        hype = [h.definition for h in hype]
        hype = " ".join(hype)
        
        hypo = synonym.hyponyms()
        hypo = [h.definition for h in hypo]
        hypo = " ".join(hypo)
        
        element.append([defn, hype, hypo])
        '''
        element.append(defn)
    gloss1.append(element)

gloss2 = []
for word in word_sense1:
    element = []
    for synonym in word:
        defn = synonym.definition
        
        '''
        hype = synonym.hypernyms()
        hype = [h.definition for h in hype]
        hype = " ".join(hype)
        
        hypo = synonym.hyponyms()
        hypo = [h.definition for h in hypo]
        hypo = " ".join(hypo)
        
        element.append([defn, hype, hypo])'''
        element.append(defn)
    gloss2.append(element)
    


end = len(word_sense1)

if(end > 1):
    for i in range(0,end):    
        score = []
        indices = []
        j=k=0
        if(i == 0):
            #Compare first and second word
            for wa in gloss1[i]:
                j+=1
                print j
                for wb in gloss1[i+1]:
                    k+=1
                    print j, k
                    score.append(compare(wa[0], wb[0]))
                    indices.append([j,k])
    
        elif(i == end-1):
            #Compare last two words
            for wa in gloss1[i-1]:
                j+=1
                for wb in gloss1[i]:
                    k+=1
                    score.append(compare(wa[0], wb[0]))
                    indices.append([j,k])
        else:
            #Compare middles words
            for wa in gloss1[i]:
                j+=1
                for wb in gloss1[i+1]:
                    k+=1
                    score.append(compare(wa[0], wb[0]))
                    indices.append(j)
        mx = indices[score.index(max(score))]
        word_sense1[i] = word_sense1[i][mx]
#Create a similarity matrix
#sim_mat = np.zeros(len(sent1),len(sent2))

#Add to a file
#return [word_sense1, sent2]