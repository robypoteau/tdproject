from TwitterAPI import TwitterAPI

consumer_key = "7UhYU7wwZZAMQQnwperCUA"
consumer_secret = "gADPNwkySetoudLGRhYDd6dmHgABbPZjuthX1xM4C6k"
access_token_key = "1587711043-x8cU7WbWjPBBXuwykoMgNwnpU6sO76BeBtHh7Aj"
access_token_secret = "Lk16RRBkhrNZoIuMZ23RVmKAldYSmzGQiYJeIEm4R0"

issue = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)

#Contacts the twitter REST Api and asked for tweets satisfying the following criteria
issue.request('search/tweets', {'q':'obama', 'geocode':'28.07925,-80.621903,5mi', 'lang':'en', 'count':'10'})
iteration = issue.get_iterator()

with open('C:/Users/Roby/Documents/Python/tdproject/twitterNodes.csv', 'a') as afile:
    for item in iteration:
        ident = item['id_str'].encode('utf-8')
        tweet = item['text'].encode('utf-8')
        tweet = " ".join(tweet.split()) #Removes the excess whitespace from the tweet
        afile.write(ident +','+ tweet + '\n') #Writes the id and tweet to a file
    
