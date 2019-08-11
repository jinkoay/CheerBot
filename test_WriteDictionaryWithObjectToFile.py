from datetime import datetime
import pickle
time1 = "2020-03-01 00:00:00.758604"
time2 = "2020-02-28 22:59:59.944674"
t1 = datetime.strptime(time1[0:19], "%Y-%m-%d %H:%M:%S")
t2 = datetime.strptime(time2[0:19], "%Y-%m-%d %H:%M:%S")

class Follower:
    def __init__(self, id, time_stamp, last_tweet_id):
        self.id = id
        self.time_stamp = time_stamp
        self.last_tweet_id = last_tweet_id

follower = Follower(489685, t1, 1234567890)

dictionary = {
    "123" : "1234567",
    "1234" : follower
}


'''
proof of concept for writing and accessing the file with
object as value inside a dictionary using pickle
'''
f = open("dictionary.pkl", "wb")
pickle.dump(dictionary,f)
f.close()

dict = pickle.load(open("dictionary.pkl", "rb"))
print(dict.get("123"))
print(dict.get("1234").id)
