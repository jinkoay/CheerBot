import tweepy
import time

from keys import *


def get_all_tweets_follower():
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

    api = tweepy.API(auth)
    tweets = []
    ids = []
    for page in tweepy.Cursor(api.followers_ids, screen_name="CheerPy_").pages():
        ids.extend(page)
        time.sleep(1)

    for id in ids: 
        tweets.append(get_tweets(id))

    for tweet in tweets:
        print(tweet.text)

def get_tweets(username, lastId): 
          
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
  
    api = tweepy.API(auth) 
    
    if lastId == -1:
        tweets = api.user_timeline(screen_name=username, count=30)
    else:
        tweets = api.user_timeline(screen_name=username, count=30, since_id = lastId)

    return tweets

