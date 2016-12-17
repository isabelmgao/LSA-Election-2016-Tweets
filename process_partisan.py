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
# LSA.lsa(tweets)

trump_list = []
t1 = "CrookedHillary" 
t2 = "MAGA"
t3 = "MakeAmericaGreatAgain"
for each in tweets:
	if t1.lower() in each or t2.lower() in each or t3.lower() in each:
		trump_list.append(each)
LSA.lsa(trump_list)

# clinton_list = []
# c1 = "imwithher"
# c2 = "nastywomen"
# for each in tweets:
# 	if c1.lower() in each or c2.lower() in each:
# 		clinton_list.append(each)
# LSA.lsa(clinton_list)