import os
import sys
import pickle
from Follower import *

filename = 'data.pkl'

def get_follower_info():
    try:
        dict = pickle.load(open(filename, "rb"))
        # print(dict)
        return dict
    except IOError:
        sys.stderr.write("Could not find read file. Abort.\n")
        exit()
    


def store_follower_info(dict):
    # if not os.path.isfile(filename):
    #     with open(filename,'wb') as file:
    #         pickle.dump(dict, file)
    #     file.close() 
    f = open(filename, 'wb')
    pickle.dump(dict,f)
    f.close()

get_follower_info()