import pymongo
import json
from pymongo import MongoClient
import sys
from pprint import pprint
import json
from bson import ObjectId
import string
import unicodedata
import LSA
import cPickle as pick

# with open("data_pickled_1.pickle",'r')as f:
#     tweets = pick.load(f)

# with open("data_pickled_2.pickle",'r')as f:
#     tweets = pick.load(f)

# with open("data_pickled_3.pickle",'r')as f:
#     tweets = pick.load(f)

# with open("data_pickled_4.pickle",'r')as f:
#     tweets = pick.load(f)

with open("data_pickled_5.pickle",'r')as f:
    tweets = pick.load(f)


LSA.lsa(tweets)