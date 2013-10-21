import nltk

#Import File
with open("C:/Users/Roby/Documents/Python/tdproject/twitter_raw.txt") as afile:
    raw = afile.read()
    tokens = nltk.word_tokenize(raw)

#Calculate n-grams
twotuples = nltk.bigrams(tokens)
#Remove the duplicates from the list
twogram = list(set(twotuples))

#find top five or 10
freqTable = []

for i in range(0,len(twogram)):
    count = twotuples.count(twogram[i])
    freqTable.append([count, twogram[i]])
    
freqTable.sort()
freqTable.reverse()

with open('C:/Users/Roby/Documents/Python/tdproject/frequency_table.txt', 'w') as afile:
    for i in range(0,len(freqTable)):
        if(freqTable[i][0] > 1 ):
            afile.write(str(freqTable[i][0]) + " | "+ " | ".join(freqTable[i][1])+ '\n')
        else:
            break