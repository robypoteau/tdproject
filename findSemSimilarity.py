import nltk, os, time
import numpy as np
from nltk.corpus import wordnet as wn
wnl = nltk.stem.WordNetLemmatizer()

def lcs(s1, s2):
    #s1 = "tom is the man tom tom tom"
    #s2 = "tom is a man"
    
    #s1 = s1.split(" ")
    #s2 = s2.split(" ")
    
    l1 = len(s1) + 1
    l2 = len(s2) + 1
    
    C = np.zeros((l1,l2))
    
    for w1 in range(1,l1):
        for w2 in range(1,l2):
            if(s1[w1-1] == s2[w2-1]):
                C[w1,w2] = C[w1-1,w2-1] + 1
            else:
                C[w1,w2] = max(C[w1,w2-1], C[w1-1,w2])
    return C[l1-1,l2-1]

def compare(list1, list2):
    l1 = list1.split(" ")
    l2 = list2.split(" ")
    len3 = lcs(l1, l2)
    list3 = set(l1) & set(l2)
    return len3*len3 + len(list3) - len3

def scoreall(wa, wb):
   return compare(wa[0], wb[0]) + compare(wa[0], wb[1]) + compare(wa[0], wb[2]) + compare(wa[1], wb[1]) + compare(wa[1], wb[2])  + compare(wa[2], wb[2])

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

def sem_similarity(sent1, sent2):
    #sent1 = "\xe2\x80\x9c@itsss_ervin: I don't understand how I'm so bad at math and I'm Asian\xe2\x80\x9d \xf0\x9f\x98\x82\xf0\x9f\x98\x82\xf0\x9f\x98\x82\xf0\x9f\x91\x8f\xf0\x9f\x91\x8f\xf0\x9f\x91\x8f\xf0\x9f\x91\x8f\t\t\n"
    #sent2 = '@saaaamanthaa_ samantha is soooo perf like omg \xf0\x9f\x98\xad\xf0\x9f\x98\xad\xf0\x9f\x98\xad\xf0\x9f\x92\x98\xf0\x9f\x92\x81\n'
    
    #Clean up text 
    sent1 = sent1.decode('ascii', 'ignore').encode('utf-8')
    sent2 = sent2.decode('ascii', 'ignore').encode('utf-8')
    
    #Tokenize text
    sent1 = nltk.tokenize.TreebankWordTokenizer().tokenize(sent1.lower())
    sent2 = nltk.tokenize.TreebankWordTokenizer().tokenize(sent2.lower())
    
    #Remove Contractions
    sent1 = [rmv_contractions(token) for token in sent1]
    sent2 = [rmv_contractions(token) for token in sent2]
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

    if(word_sense1 == [] or word_sense2 == []):
        return 0.0
                
    #gloss matrix
    gloss1 = []
    for word in word_sense1:
        element = []
        for synonym in word:
            examples = " ".join(synonym.examples)
            defn = synonym.definition + " " + examples
            
            
            hype = synonym.hypernyms()
            hype = [h.definition for h in hype]
            hype = " ".join(hype)
            
            hypo = synonym.hyponyms()
            hypo = [h.definition for h in hypo]
            hypo = " ".join(hypo)
            
            element.append([defn, hype, hypo])
            '''
            element.append(defn)'''
        gloss1.append(element)
    
    gloss2 = []
    for word in word_sense2:
        element = []
        for synonym in word:
            examples = " ".join(synonym.examples)
            defn = synonym.definition + " " + examples
            
            
            hype = synonym.hypernyms()
            hype = [h.definition for h in hype]
            hype = " ".join(hype)
            
            hypo = synonym.hyponyms()
            hypo = [h.definition for h in hypo]
            hypo = " ".join(hypo)
            
            element.append([defn, hype, hypo])
            '''
            element.append(defn)'''
        gloss2.append(element)
    
        
    #Pick one synset out of them all to represent our word            
    end = len(word_sense1)
    if(end > 1):
        for i in range(0,end):    
            score = []
            indices = []
            j=0
            
            if(len(word_sense1[i]) > 1):
                if(i == 0):
                    #Compare first and second word
                    for wa in gloss1[i]:
                        j+=1
                        k=0
                        for wb in gloss1[i+1]:
                            k+=1
                            score.append(scoreall(wa, wb))
                            indices.append(j)
            
                elif(i == end-1):
                    #Compare last two words
                    for wa in gloss1[i-1]:
                        j+=1
                        k=0
                        for wb in gloss1[i]:
                            k+=1
                            score.append(scoreall(wa, wb))
                            indices.append(k)
                else:
                    #Compare middles words
                    for wa in gloss1[i]:
                        j+=1
                        k=0
                        for wb in gloss1[i+1]:
                            k+=1
                            score.append(scoreall(wa, wb))
                            indices.append(j)
    
                #return the j index
                mx = indices[score.index(max(score))] - 1
                word_sense1[i] = word_sense1[i][mx]
            else:
                word_sense1[i] = word_sense1[i][0]
    else:
        if(len(word_sense1[0]) > 1):
            pick = [-1*len(word.name) for word in word_sense1[0]]
            word_sense1[0] = word_sense1[0][pick.index(max(pick))]
        else:
            word_sense1[0] = word_sense1[0][0]

    end = len(word_sense2)
    if(end > 1):
        for i in range(0,end):    
            score = []
            indices = []
            j=0
            
            if(len(word_sense2[i]) > 1):
                if(i == 0):
                    #Compare first and second word
                    for wa in gloss2[i]:
                        j+=1
                        k=0
                        for wb in gloss2[i+1]:
                            k+=1
                            score.append(scoreall(wa, wb))
                            indices.append(j)
            
                elif(i == end-1):
                    #Compare last two words
                    for wa in gloss2[i-1]:
                        j+=1
                        k=0
                        for wb in gloss2[i]:
                            k+=1
                            score.append(scoreall(wa, wb))
                            indices.append(k)
                else:
                    #Compare middles words
                    for wa in gloss2[i]:
                        j+=1
                        k=0
                        for wb in gloss2[i+1]:
                            k+=1
                            score.append(scoreall(wa, wb))
                            indices.append(j)
    
                #return the j index
                mx = indices[score.index(max(score))] - 1
                word_sense2[i] = word_sense2[i][mx]
            else:
                word_sense2[i] = word_sense2[i][0]
    else:
        if(len(word_sense2[0]) > 1):
            pick = [-1*len(word.name) for word in word_sense2[0]]
            word_sense2[0] = word_sense2[0][pick.index(max(pick))]
        else:
            word_sense2[0] = word_sense2[0][0]
    #Create a similarity matrix
    sim_mat = []
    for word1 in word_sense1:
        for word2 in word_sense2:
            if(word1.pos == word2.pos):
                value = (word1.path_similarity(word2))
                if(value == None):
                    value =0
            else:
                value = 0
            sim_mat.append(value)
    
    return 2*sum(sim_mat)/(len(word_sense1)+end)

#Import File
start_time =  time.time()
raw=[]
N = 11 #23472
threshold = 0.0
EdgeMatrix = np.zeros((N,N))
thisDir = os.path.dirname(os.path.realpath(__file__))
with open(os.path.join(thisDir, "test.txt")) as afile:
    for i in range(0,N):
        raw.append(afile.readline())

with open(os.path.join(thisDir, "test.csv"), 'a') as afile:
    for i in range(0,N):
        afile.write(";A"+str(i+1))
        
    for i in range(0,N):
        afile.write("\nA"+str(i+1))
        for j in range(0,N):
            if(i != j):
                if(i < j):
                    EdgeMatrix[i][j] = sem_similarity(raw[i], raw[j])
                    if(EdgeMatrix[i][j] > threshold):
                        afile.write(";"+str(EdgeMatrix[i][j]))
                    else:
                        afile.write(';') 
                else:
                    EdgeMatrix[i][j] = EdgeMatrix[j][i]
                    if(EdgeMatrix[i][j] > threshold):
                        afile.write(";"+str(EdgeMatrix[j][i]))
                    else:
                        afile.write(';') 
            else:
                afile.write(';')
print  str((time.time() - start_time)/60.) + " minutes"