from TwitterAPI import TwitterAPI
import sys
import time

consumer_key = "7UhYU7wwZZAMQQnwperCUA"
consumer_secret = "gADPNwkySetoudLGRhYDd6dmHgABbPZjuthX1xM4C6k"
access_token_secret = "Lk16RRBkhrNZoIuMZ23RVmKAldYSmzGQiYJeIEm4R0"
access_token_key = "1587711043-x8cU7WbWjPBBXuwykoMgNwnpU6sO76BeBtHh7Aj"

call = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)

#Contacts the twitter REST Api and asked for tweets satisfying the following criteria

finish_time = time.time() + 28800
while(finish_time > time.time()): # for 8 hours
    try:
        call.request('statuses/sample')
    except :
        print 'Call fail'

    response = call.get_iterator()

    with open('C:/Users/Roby/Documents/Python/tdproject/twitterNodes2.tsv', 'a') as afile:
        for item in response:
            try:
                lang = item[u'lang'].encode('utf-8')
                if(lang == 'en'):
                    #print item[u'id_str'].encode('utf-8')
                    ident = item[u'id_str'].encode('utf-8')
                    tweet = item[u'text'].encode('utf-8')
                    tweet = " ".join(tweet.split()) #Removes the excess whitespace from the tweet
                    afile.write(lang + "\t" + ident +'\t'+ tweet + '\n') #Writes the id and tweet to a file
            
            except KeyError as ke:
                continue
                
            except:
                print "Unexpected error:", sys.exc_info()[0]
                continue
time.sleep(1200)
                