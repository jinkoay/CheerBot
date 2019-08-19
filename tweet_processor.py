import tweepy
import time
import random
import os
import json

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

def get_tweets(user_id, lastId): 
          
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
  
    api = tweepy.API(auth)

    username = api.get_user(user_id).screen_name
    print('username: ' + username)
    
    if lastId == -1:
        print('getting all tweets')
        tweets = api.user_timeline(screen_name=username, count=30)
    else:
        print('getting since')
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

# Added by Jin 8/19
def follow_user(user_id):
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

    api = tweepy.API(auth)
    api.create_friendship(user_id)

def unfollow_user(user_id):
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

    api = tweepy.API(auth)
    api.destroy_friendship(user_id)

def get_friends():
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

    api = tweepy.API(auth)
    api.friends_ids('CheerPy_') 

def is_following(this, other):
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

    api = tweepy.API(auth)

    source, target = api.show_friendship(source_screen_name=this, target_id=other)
    return other.following
#  

def reply_to_tweet(user_id, tweet_id):
    
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api = tweepy.API(auth)

    run()
    imageLocs = []
    count = 0

    username = api.get_user(user_id).screen_name
    
    
    with open('images.txt', 'r') as fp:
        for line in fp:
            line = line.strip()
            imageLocs.append(line)

    
    
    size = len(imageLocs)
    choose = random.randint(0, size - 1)
    reply = imageLocs[choose]    

    filename = 'temp.jpg'
    request = requests.get(reply, stream=True)
    if request.status_code == 200:
        with open(filename, 'wb') as image:
            for chunk in request:
                image.write(chunk)

        api.update_with_media(filename, status= "@" + username, in_reply_to_status_id = tweet_id)
        os.remove(filename)
    else:
        print("Unable to download image")

    #api.update_status("@"+ username + " " + reply, tweet_id)
    

 #reply_to_tweet(1132848667092803584, 1133213334302527494)
