import os
import sys
import pickle
from Follower import *

filename = 'data.pkl'

def get_follower_info():
    try:
        id_to_follower = pickle.load(open(filename, "rb"))
        # print(id_to_follower)
        return id_to_follower
    except IOError:
        sys.stderr.write("Could not find read file.\n")
        return {}

def store_follower_info(id_to_follower):
    # if not os.path.isfile(filename):
    #     with open(filename,'wb') as file:
    #         pickle.dump(dict, file)
    #     file.close() 
    f = open(filename, 'wb')
    pickle.dump(id_to_follower,f)
    f.close()

get_follower_info()