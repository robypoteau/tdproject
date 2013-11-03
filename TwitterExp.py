from TwitterAPI import TwitterAPI
import sys, os
import time

consumer_key = "7UhYU7wwZZAMQQnwperCUA"
consumer_secret = "gADPNwkySetoudLGRhYDd6dmHgABbPZjuthX1xM4C6k"
access_token_secret = "Lk16RRBkhrNZoIuMZ23RVmKAldYSmzGQiYJeIEm4R0"
access_token_key = "1587711043-x8cU7WbWjPBBXuwykoMgNwnpU6sO76BeBtHh7Aj"

call = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)

#Contacts the twitter REST Api and asked for tweets satisfying the following criteria
thisDir = os.path.dirname(os.path.realpath(__file__))

finish_time = time.time() + 28800

while(finish_time > time.time()): # for 8 hours
    try:
        call.request('statuses/sample', '{stall_warnings = true}')
        print "New Call"
    except :
        print 'Call fail'

    response = call.get_iterator()
    
    with open(os.path.join(thisDir, 'twitterNodes3.tsv'), 'a') as afile:
        for item in response:
            try:
                if('lang' in item):
                    lang = item[u'lang'].encode('utf-8')
                    if(lang == 'en'):
                        #print item[u'id_str'].encode('utf-8')
                        ident = item[u'id_str'].encode('utf-8')
                        tweet = item[u'text'].encode('utf-8')
                        tweet = " ".join(tweet.split()) #Removes the excess whitespace from the tweet
                        afile.write(lang + "\t" + ident +'\t'+ tweet + '\n') #Writes the id and tweet to a file
                
                elif('warning' in item):
                    print item
                    
                elif('error' in item):
                    print item
                    
            except KeyError as ke:
                print "Key Error"
                continue
                
            except:
                print "Unexpected error:", sys.exc_info()[0]
                #continue

                