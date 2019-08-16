from tweet_processor import *
from filterToNotSpam import *
from emotion_analyzer import *
from file_io import *
from keys.keys import *
from keys.ibm_keys import *
import datetime
import time

# tweets = get_tweets('youresadlikeme', -1)
# print(len(tweets))
# print(find_sad_id(tweets))

# for tweet in tweets:
#     print(tweet.text)
#     print(str(tweet.created_at))
#     print('\n')

id_to_follower = {}

while True:
    cur_date = datetime.datetime.now()
    id_to_follower = get_follower_info()
    user_ids = get_follower_ids()

    for id in user_ids:
        print("id: " + str(id))

        if id in id_to_follower:
            follower = id_to_follower[id]

            if filterToNotSpam(str(follower.time_stamp), str(cur_date)):
                tweets = get_tweets(id, follower.last_tweet_id)

                sad_id = find_sad_id(tweets)
                timestamp = follower.time_stamp

                if sad_id != -1:
                    reply_to_tweet(id, sad_id)
                    timestamp = cur_date

                if len(tweets) == 0:
                    last_tweet_id = -1
                else:
                    last_tweet_id = tweets[0].id

                follower = Follower(id, timestamp, last_tweet_id)
                id_to_follower[id] = follower

        else:
            tweets = get_tweets(id, -1)

            sad_id = find_sad_id(tweets)
            timestamp = datetime.datetime(1999, 1, 1, 0, 0, 0)

            if sad_id != -1:
                reply_to_tweet(id, sad_id)
                timestamp = cur_date

            if len(tweets) == 0:
                last_tweet_id = -1
            else:
                last_tweet_id = tweets[0].id

            follower = Follower(id, timestamp, last_tweet_id)
            id_to_follower[id] = follower

    store_follower_info(id_to_follower)
    time.sleep(60) # Pause for 5 minutes

 