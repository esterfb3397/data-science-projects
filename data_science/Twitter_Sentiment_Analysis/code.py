import tweepy

import textblob

#The keys you can find it on the developer dashboard on Twitter, you can regenerate it every time you want.

consumer_key = " "
consumer_secret = " "

access_tokens = " "
access_tokens_secret = " "

auth = tweepy.OAuth1UserHandler(consumer_key,consumer_secret)
auth.set_access_token(access_tokens,access_tokens_secret)

api = tweepy.API(auth)

public_tweets = api.search_tweets("Russia")

for tweet in public_tweets:
    print(tweet.text)
    analysis = textblob.TextBlob(tweet.text)
    print(analysis.sentiment)