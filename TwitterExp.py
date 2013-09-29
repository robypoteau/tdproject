from TwitterAPI import TwitterAPI

consumer_key = "7UhYU7wwZZAMQQnwperCUA"
consumer_secret = "gADPNwkySetoudLGRhYDd6dmHgABbPZjuthX1xM4C6k"
access_token_key = "1587711043-x8cU7WbWjPBBXuwykoMgNwnpU6sO76BeBtHh7Aj"
access_token_secret = "Lk16RRBkhrNZoIuMZ23RVmKAldYSmzGQiYJeIEm4R0"

issue = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)

issue.request('search/tweets', {'q':'Jesus', 'lang':'en', 'count':'10'})
iteration = issue.get_iterator()

with open('twitterNodes.csv', 'w+') as afile:
    for item in iteration:
        afile.write(item['id_str'].encode('utf-8') +','+ item['text'].encode('utf-8') + '\n')
    
