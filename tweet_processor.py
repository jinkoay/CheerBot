import tweepy
import time
import random

from keys.keys import *
from scraper import *



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


def get_follower_ids():
    
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

    api = tweepy.API(auth)
    ids = []
    
    for page in tweepy.Cursor(api.followers_ids, screen_name="CheerPy_").pages():
        ids.extend(page)
        time.sleep(1)
    
    return ids

def reply_to_tweet(user_id, tweet_id):
    
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api = tweepy.API(auth)

    run()
    imageLocs = []
    count = 0

    username = api.get_user(user_id).screen_name
    
    try:
        fp = open("images.txt", 'r')
        
        line = fp.readline
        imageLocs.append(line)

        while line:
            line = fp.readline
            imageLocs.append(line)

    finally:
        fp.close()
    
    size = len(imageLocs)
    choose = random.randint(0, size - 1)
    reply = imageLocs[choose]    

    api.update_status("@<"+ username + "> " + reply, tweet_id)
    

reply_to_tweet(1132848667092803584, 1133213334302527494)