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
    friends = get_friends()
    follower_ids = get_follower_ids()

    for id in follower_ids:
        if not is_following('CheerPy_', id):
            follow_user(id)

        # mutual followers
        else:
            print("id: " + str(id))

            # existing follower
            if id in id_to_follower:
                follower = id_to_follower[id]

                if filterToNotSpam(str(follower.time_stamp), str(cur_date)):
                    print('filter pass')
                    tweets = get_tweets(id, follower.last_tweet_id)

                    # if current follower has no new tweets, skip
                    if len(tweets) == 0:
                        continue

                    print('pass length of tweets')

                    sad_id = find_sad_id(tweets)
                    # default timestamp value
                    timestamp = follower.time_stamp

                    print('sad id: ' + str(sad_id))

                    if sad_id != -1:
                        reply_to_tweet(id, sad_id)
                        timestamp = cur_date

                    last_tweet_id = tweets[0].id

                    follower = Follower(id, timestamp, last_tweet_id)
                    id_to_follower[id] = follower

            # new followers
            else:
                # get all tweets
                tweets = get_tweets(id, -1)

                # if the new follower has no tweets, don't store them
                if len(tweets) == 0:
                    continue

                last_tweet_id = tweets[0].id
                timestamp = datetime.datetime(1999, 1, 1, 0, 0, 0)

                follower = Follower(id, timestamp, last_tweet_id)
                id_to_follower[id] = follower

    # unfollow people who unfollowed us
    for id in friends:
        if not is_follower('CheerPy_', id):
            unfollow_user(id)

    store_follower_info(id_to_follower)
    time.sleep(60) # Pause for 5 minutes


    # for id in follower_ids:
    # print("id: " + str(id))

    # if id in id_to_follower:
    #     follower = id_to_follower[id]

    #     if filterToNotSpam(str(follower.time_stamp), str(cur_date)):
    #         print('filter pass')
    #         tweets = get_tweets(id, follower.last_tweet_id)

    #         # if current follower has no new tweets, skip
    #         if len(tweets) == 0:
    #             continue

    #         sad_id = find_sad_id(tweets)
    #         timestamp = follower.time_stamp

    #         if sad_id != -1:
    #             reply_to_tweet(id, sad_id)
    #             timestamp = cur_date

    #         last_tweet_id = tweets[0].id

    #         follower = Follower(id, timestamp, last_tweet_id)
    #         id_to_follower[id] = follower

    # # new followers
    # else:
    #     # get all tweets
    #     tweets = get_tweets(id, -1)

    #     # if the new follower has no tweets, don't store them
    #     if len(tweets) == 0:
    #         continue

    #     last_tweet_id = tweets[0].id
    #     timestamp = datetime.datetime(1999, 1, 1, 0, 0, 0)

    #     follower = Follower(id, timestamp, last_tweet_id)
    #     id_to_follower[id] = follower

 