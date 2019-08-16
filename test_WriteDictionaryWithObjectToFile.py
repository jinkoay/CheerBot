from datetime import datetime
import pickle
from Follower import *
import random
times = ["2020-03-01 00:00:00.758604", 
         "2019-02-28 23:59:59.944674",
         "8793-02-28 03:59:59.944674",
         "1434-02-28 06:59:59.944674",
         "4577-02-28 21:59:59.944674",
         "1223-02-28 22:59:59.944674",
         "2023-02-28 22:59:59.944674",
         "2040-02-28 04:59:59.944674",
         "2000-02-28 19:59:59.944674",
         "2620-02-28 07:59:59.944674"]

ids = [123, 234, 345, 456, 567, 678, 789, 890, 901, "012"]

'''
building the dictionary/mapping from an key value to the follower
'''
followers = []
dictionary = {}
for i in range(len(times)):
    time = datetime.strptime(times[i][0:19], "%Y-%m-%d %H:%M:%S")
    id = ids[i]
    key = "$" + str(i)
    dictionary.update({key: Follower(id, time, random.randint(0, 123456789))})

'''
proof of concept for writing and accessing the file with
object as value inside a dictionary using pickle
'''
f = open("dictionary.pkl", "wb")
pickle.dump(dictionary,f)
f.close()

dict = pickle.load(open("dictionary.pkl", "rb"))


print(type(dict))
for key in dict:
    print(key, ",", dict.get(key).id, ",", dict.get(key).time_stamp, ",", dict.get(key).last_tweet_id)
#  id, time_stamp, last_tweet_id


f.close()
