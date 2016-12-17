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

collection = pymongo.MongoClient()["tweets"]["StreamingAPITweets"]
objects = collection.find()

tweet_list = []
data_twitter = []

# with open('new.txt', 'w') as outfile:
for each in objects:
	try:
		strip_newline = each['text'].replace('\n', ' ')
		convert_string = unicodedata.normalize('NFKD', strip_newline).encode('ascii','ignore')
		remove_punc = convert_string.translate(None, string.punctuation)
		# tweet_list.append({each['timestamp_ms']: ['geo'+str(each['geo']), remove_punc]})
		# tweet_list.append({each['timestamp_ms']: [each['user']['location'], remove_punc]})
		data_twitter.append((int(each['timestamp_ms']), remove_punc.lower().strip()))
	except:
		pass
data_sorted = sorted(data_twitter, key=lambda x: x[0])
json.dump(tweet_list, outfile)


with open("data_pickled.pickle",'w')as f:
    pick.dump(data_sorted,f)


int1 = []
int2 = []
int3 = []
int4 = []
int5 = []
for i in range(len(data_persist)):
	if data_persist[i][0] >= 1478662847222 and data_persist[i][0] <= 1478670255733:
		int1.append(data_persist[i][1]) 
	elif data_persist[i][0] > 1478670255733 and data_persist[i][0] <= 1478697167163:
		int2.append(data_persist[i][1]) 
		data_persist.pop(i)
	elif data_persist[i][0] > 1478697167163 and data_persist[i][0] <= 1478709600000:
		int3.append(data_persist[i][1]) 
		data_persist.pop(i)
	elif data_persist[i][0] > 1478709600000 and data_persist[i][0] <= 1478711940000:
		int4.append(data_persist[i][1]) 
		data_persist.pop(i)
	elif data_persist[i][0] > 1478711940000:
		int5.append(data_persist[i][1]) 
		data_persist.pop(i)

with open("data_pickled_1.pickle",'w')as f:
    pick.dump(int1,f)

with open("data_pickled_2.pickle",'w')as f:
    pick.dump(int2,f)

with open("data_pickled_3.pickle",'w')as f:
    pick.dump(int3,f)

with open("data_pickled_4.pickle",'w')as f:
    pick.dump(int4,f)

with open("data_pickled_5.pickle",'w')as f:
    pick.dump(int5,f)




