import numpy as np
import pandas as pd
import tweepy
import matplotlib.pyplot as plt
import pymongo
import ipywidgets as wgt
from IPython.display import display
from sklearn.feature_extraction.text import CountVectorizer
import re
from datetime import datetime

# %matplotlib inline

api_key = "zLwXfUOKaNPdj1Ha8LYT9SOuD"
api_secret = "b75hSBTudTqUFQ7cZVNh2ou1uMSYgUcMbmM2hmCzkqE5qLq509"
access_token = "525398212-DjplhjcTo96EKpbFz380hESJhtqdIZLxXBuRGOAa" 
access_token_secret = "94jUEIpcjYAbPxv6RwU8i3p7ddx0GZBxweCwRVGwy9zcu" 

auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

col = pymongo.MongoClient()["tweets"]["StreamingAPITweets"]
col.count()

class MyStreamListener(tweepy.StreamListener):
    
    counter = 0
    
    def __init__(self, max_tweets=1000, *args, **kwargs):
        self.max_tweets = max_tweets
        self.counter = 0
    
    def on_connect(self):
        self.counter = 0
        self.start_time = datetime.now()
    
    def on_status(self, status):
        # Increment counter
        self.counter += 1
        print status
        
        # Store tweet to MongoDB
        col.insert_one(status._json)
        
        if self.counter >= self.max_tweets:
            myStream.disconnect()
            print("Finished")
    
myStreamListener = MyStreamListener(max_tweets=10)
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)

keywords = ["Trump",
            "Clinton",
            "imwithher",
            "election2016",
            "MyVote2016",
            "ElectionNight",
            "CrookedHillary",
            "nastywomen",
            "DonaldTrump",
            "MAGA",
            "MakeAmericaGreatAgain",
           ]

try:
    myStream.filter(track=keywords)
    # print("Tweets collected: %s" % myStream.listener.counter)
    # print("Total tweets in collection: %s" % col.count())
    # break
except:
    print 'what the fuck?'
    # print("ERROR# %s" % (error_counter + 1))