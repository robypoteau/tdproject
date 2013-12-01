import time, os, numpy as np, nltk

def sem_similarity(sent1, sent2):
    #sent1 = "\xe2\x80\x9c@itsss_ervin: I don't understand how I'm so bad at math and I'm Asian\xe2\x80\x9d \xf0\x9f\x98\x82\xf0\x9f\x98\x82\xf0\x9f\x98\x82\xf0\x9f\x91\x8f\xf0\x9f\x91\x8f\xf0\x9f\x91\x8f\xf0\x9f\x91\x8f\t\t\n"
    #sent2 = '@saaaamanthaa_ samantha is soooo perf like omg \xf0\x9f\x98\xad\xf0\x9f\x98\xad\xf0\x9f\x98\xad\xf0\x9f\x92\x98\xf0\x9f\x92\x81\n'
    
    #Clean up text 
    sent1 = sent1.decode('ascii', 'ignore').encode('utf-8')
    sent2 = sent2.decode('ascii', 'ignore').encode('utf-8')
    
    #Tokenize text
    sent1 = nltk.tokenize.TreebankWordTokenizer().tokenize(sent1.lower())
    sent2 = nltk.tokenize.TreebankWordTokenizer().tokenize(sent2.lower())
    
    for word1 in sent1:
        for word2 in sent2:
            if(word1 == word2):
                return 1.0
    return 0.0

start_time =  time.time()
raw=[]
N = 1000 #23472
threshold = 0.0
EdgeMatrix = np.zeros((N,N))
thisDir = os.path.dirname(os.path.realpath(__file__))
with open(os.path.join(thisDir, "forEdges.tsv")) as afile:
    for i in range(0,N):
        raw.append(afile.readline())
        
with open(os.path.join(thisDir, "unigrams.csv"), 'a') as afile:
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