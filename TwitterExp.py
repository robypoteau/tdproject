from TwitterAPI import TwitterAPI

consumer_key = "7UhYU7wwZZAMQQnwperCUA"
consumer_secret = "gADPNwkySetoudLGRhYDd6dmHgABbPZjuthX1xM4C6k"
access_token_key = "1587711043-x8cU7WbWjPBBXuwykoMgNwnpU6sO76BeBtHh7Aj"
access_token_secret = "Lk16RRBkhrNZoIuMZ23RVmKAldYSmzGQiYJeIEm4R0"

issue = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)

issue.request('search/tweets', {'q':'zzz'})
iteration = issue.get_iterator()
for item in iteration:
    print item