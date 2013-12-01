import os, numpy as np, csv

N = 10

thisDir = os.path.dirname(os.path.realpath(__file__))
friends_mat = []
followers_mat = []
raw = []
with open(os.path.join(thisDir, "id_tweets.txt")) as afile:
    csvfile = csv.reader(afile, delimiter='\t')
    for row in csvfile:
        raw.append(row)

src_id = list(np.array(raw)[:,0])
raw = []

with open(os.path.join(thisDir, "friends")) as file1:
    csvfile = csv.reader(file1, delimiter='\t')
    for row in csvfile:
        friends_mat.append(row)
        
with open(os.path.join(thisDir, "followers")) as file1:
    csvfile = csv.reader(file1, delimiter='\t')
    for row in csvfile:
        followers_mat.append(row)

friends_mat = np.array(friends_mat)
followers_mat = np.array(followers_mat)

frEdgeMat = np.zeros((N,N))
flEdgeMat = np.zeros((N,N))
       
with open(os.path.join(thisDir, "friends_edges.csv"), 'a') as file1:
    with open(os.path.join(thisDir, "followers_edges.csv"), 'a') as file2:
        with open(os.path.join(thisDir, "friendfollower_edges.csv"), 'a') as file3:
    
            for i in range(0,N):
                file1.write(";" + src_id[i])
                file2.write(";" + src_id[i])
                file3.write(";" + src_id[i])
                
            for i in range(0,N):
                file1.write("\n" + src_id[i])
                file2.write("\n" + src_id[i])
                file3.write("\n" + src_id[i])
                
                for j in range(0,N):
                    if(i != j):
                        if(i < j):
                            if(src_id[j] in friends_mat[i]):
                                frEdgeMat[i,j] = 1
                                file1.write(";1")
                            else:
                                file1.write(';') 
                        
                            if(src_id[j] in followers_mat[i]):
                                flEdgeMat[i,j] = 1
                                file2.write(";1")
                            else:
                                file2.write(';') 
                        
                            if(frEdgeMat[i,j] == 1 and frEdgeMat[i,j] == flEdgeMat[i,j] ):
                                file3.write(";1")
                            else:
                                file3.write(';')

                        else:
                            frEdgeMat[i,j] = frEdgeMat[j,i]
                            flEdgeMat[i,j] = flEdgeMat[j,i]
                            
                            if(frEdgeMat[i,j] == 1):
                                file1.write(";1")
                            else:
                                file1.write(';') 
                        
                            if(flEdgeMat[i,j] == 1):
                                file2.write(";1")
                            else:
                                file2.write(';') 
                        
                            if(frEdgeMat[i,j] == 0 and frEdgeMat[i,j] == flEdgeMat[i,j] ):
                                file3.write(";1")
                            else:
                                file3.write(';') 
                    else:
                        file1.write(';')
                        file2.write(';')
                        file3.write(';')