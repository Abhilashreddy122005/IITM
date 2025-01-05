import tweepy
from textblob import TextBlob


consumer_key = 'your-consumer-key'
consumer_secret = 'your-consumer-secret'
access_token = 'your-access-token'
access_token_secret = 'your-access-token-secret'


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

def get_sentiment(query):
    public_tweets = api.search(q=query, count=100)
    sentiment = 0
    for tweet in public_tweets:
        analysis = TextBlob(tweet.text)
        sentiment += analysis.sentiment.polarity
    return sentiment / len(public_tweets)

