from TwitterAPI import TwitterAPI
import sys, os
#import time

consumer_key = "7UhYU7wwZZAMQQnwperCUA"
consumer_secret = "gADPNwkySetoudLGRhYDd6dmHgABbPZjuthX1xM4C6k"
access_token_secret = "Lk16RRBkhrNZoIuMZ23RVmKAldYSmzGQiYJeIEm4R0"
access_token_key = "1587711043-x8cU7WbWjPBBXuwykoMgNwnpU6sO76BeBtHh7Aj"

call = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)
print "0"
#Contacts the twitter REST Api and asked for tweets satisfying the following criteria
thisDir = os.path.dirname(os.path.realpath(__file__))
print "1"
#finish_time = time.time() + 28800

while('true'): # for 8 hours
    print "2"
    call.request('statuses/sample')
    #call.request('friends/ids', '{user_id  = 392754790176129024, count = 250}')
    print "New Call"

    response = call.get_iterator()                        
                                               
    with open(os.path.join(thisDir, 'id_tweets.txt'), 'a') as afile:
        for item in response:
            try:
                lang = item[u'lang'].encode('utf-8')
                if(lang == 'en'):
                    ident = item[u"user"][u'id_str'].encode('utf-8')
                    tweet = item[u'text'].encode('utf-8')
                    tweet = " ".join(tweet.split()) #Removes the excess whitespace from the tweet
                    
                    afile.write(ident +'\t' + tweet + '\n') #Writes the id and tweet to a file
                    print ident +'\t'+ tweet + '\n'
                elif('warning' in item):
                    print item
                    
                elif('error' in item):
                    print item
                    
            except KeyError as ke:
                print "Key Error"
                continue
                
            except:
                print "Unexpected error:", sys.exc_info()[0]
                #continue'''
                
                
                
                '''    
    with open(os.path.join(thisDir, 'user_friends.tsv'), 'w') as file1:
        with open(os.path.join(thisDir, 'user_follow.tsv'), 'w') as file2:
            for i in range(0,N):
                file1.write(";A"+str(i+1))
                file2.write(";A"+str(i+1))
            
            for item in response:
                ids = item[u'ids']'''  