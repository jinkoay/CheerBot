from datetime import datetime
import pickle
from Follower import *
time1 = "2020-03-01 00:00:00.758604"
time2 = "2020-02-28 22:59:59.944674"
t1 = datetime.strptime(time1[0:19], "%Y-%m-%d %H:%M:%S")
t2 = datetime.strptime(time2[0:19], "%Y-%m-%d %H:%M:%S")

followers = []
followers.append(Follower(123, t1, 1234567890))
followers.append(Follower(234, t1, 1234567890))
followers.append(Follower(345, t1, 1234567890))
followers.append(Follower(456, t1, 1234567890))
followers.append(Follower(567, t1, 1234567890))
followers.append(Follower(678, t1, 1234567890))
followers.append(Follower(789, t1, 1234567890))
followers.append(Follower(890, t1, 1234567890))
followers.append(Follower(901, t1, 1234567890))
followers.append(Follower("012", t1, 1234567890))

dictionary = {
    "0" : followers[0]#,
#     "1" : followers[1],
#     "2" : followers[2],
#     "3" : followers[3],
#     "4" : followers[4],
#     "5" : followers[5],
#     "6" : followers[6]
}


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
    print(key, ",", dict.get(key).id), ",", dict.get(key).key.time_stamp, ",", dict.get(key).key.last_tweet_id)
#  id, time_stamp, last_tweet_id



