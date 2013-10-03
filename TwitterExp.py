from TwitterAPI import TwitterAPI
import sys

consumer_key = "7UhYU7wwZZAMQQnwperCUA"
consumer_secret = "gADPNwkySetoudLGRhYDd6dmHgABbPZjuthX1xM4C6k"
access_token_secret = "Lk16RRBkhrNZoIuMZ23RVmKAldYSmzGQiYJeIEm4R0"
access_token_key = "1587711043-x8cU7WbWjPBBXuwykoMgNwnpU6sO76BeBtHh7Aj"

call = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)

#Contacts the twitter REST Api and asked for tweets satisfying the following criteria
try:
    call.request('statuses/sample')
except :
    print 'Call fail'
    sys.exit()
    
response = call.get_iterator()

with open('C:/Users/Roby/Documents/Python/tdproject/twitterNodes.csv', 'a') as afile:
    for item in response:
        try:
            #print item[u'id_str'].encode('utf-8')
            ident = item[u'id_str'].encode('utf-8')
            tweet = item[u'text'].encode('utf-8')
            lang = item[u'lang'].encode('utf-8')
            tweet = " ".join(tweet.split()) #Removes the excess whitespace from the tweet
            afile.write(lang + "," + ident +','+ tweet + '\n') #Writes the id and tweet to a file
            #sys.exit()
        
        except KeyError as ke:
            print 'Key Fail'
            #sys.exit()
            #continue
