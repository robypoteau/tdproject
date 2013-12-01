import os, time, numpy as np, csv
from TwitterAPI import TwitterAPI

consumer_key = "7UhYU7wwZZAMQQnwperCUA"
consumer_secret = "gADPNwkySetoudLGRhYDd6dmHgABbPZjuthX1xM4C6k"
access_token_secret = "Lk16RRBkhrNZoIuMZ23RVmKAldYSmzGQiYJeIEm4R0"
access_token_key = "1587711043-x8cU7WbWjPBBXuwykoMgNwnpU6sO76BeBtHh7Aj"

call = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)

#Import File
start_time =  time.time()
raw=[]
N = 1000 #3977
count = 0
start = 28

thisDir = os.path.dirname(os.path.realpath(__file__))
with open(os.path.join(thisDir, "id_tweets.txt")) as afile:
    csvfile = csv.reader(afile, delimiter='\t')
    for row in csvfile:
        raw.append(row)

src_id = list(np.array(raw)[:,0])

with open(os.path.join(thisDir, "friends"), 'a') as file1:
    with open(os.path.join(thisDir, "followers"), 'a') as file2:
            
        for i in range(start,N):
            
            if(count > 13):
                print "sleeping"
                time.sleep(900)
                count = 1
            
            call.request('friends/ids', {'user_id' : src_id[i], 'count' : "5000", 'stringify_ids' : 'true' })
            friend = call.get_iterator()
            
            call.request('followers/ids', {'user_id' : src_id[i], 'count' : "5000", 'stringify_ids' : 'true' })
            follow = call.get_iterator()
            
            if('<Response [200]>' == str(call.response)):
                for item in friend:
                    target_ids = item["ids"]
                file1.write(src_id[i] + "\t" + "\t".join(target_ids)  + '\n')
                for item in follow:
                    target_ids = item["ids"]
                file2.write(src_id[i] + "\t" + "\t".join(target_ids)  + '\n')
                count  += 1
            elif('<Response [200]>' != str(call.response)):
                file1.write(src_id[i] + "\tmiss")
                file2.write(src_id[i] + "\tmiss")
                print call.response
'''
with open(os.path.join(thisDir, "friends")) as file1:
    csvfile = csv.reader(afile, delimiter='\t')
    for row in csvfile:
        friends_mat.append(row)
        
with open(os.path.join(thisDir, "followers")) as file1:
    csvfile = csv.reader(afile, delimiter='\t')
    for row in csvfile:
        followers_mat.append(row)

np.array(friends_mat)
np.array(followers_mat)

src_id = list(friends_mat[:,0])
frEdgeMat = np.zeros((N,N))
flEdgeMat = np.zeros((N,N))
'''

'''        
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
                            if(src_id[j] in friends_mat[i,:]):
                                frEdgeMat[i,j] = 1
                                file1.write(";1")
                            else:
                                afile.write(';') 
                        
                            if(src_id[j] in followers_mat[i,:]):
                                flEdgeMat[i,j] = 1
                                file2.write(";1")
                            else:
                                afile.write(';') 
                        
                            if(frEdgeMat[i,j] == 1 and frEdgeMat[i,j] == flEdgeMat[i,j] ):
                                file3.write(";1")
                            else:
                                afile.write(';')

                        else:
                            frEdgeMat[i,j] = frEdgeMat[j,i]
                            flEdgeMat[i,j] = flEdgeMat[j,i]
                            
                            if(frEdgeMat[i,j] == 1):
                                file1.write(";1")
                            else:
                                afile.write(';') 
                        
                            if(flEdgeMat[i,j] == 1):
                                file2.write(";1")
                            else:
                                afile.write(';') 
                        
                            if(frEdgeMat[i,j] = 0 and frEdgeMat[i,j] == flEdgeMat[i,j] ):
                                file3.write(";1")
                            else:
                                afile.write(';') 
                    else:
                        afile.write(';')'''
print  str((time.time() - start_time)/60.) + " minutes"
