#Sentiment Analysis of keyword "Election 2016" from 2016-11-6 to 2016-11-12

import tweepy
from textblob import TextBlob

import getoldtweets
import numpy as np
import operator


consumer_key= 'Consumer key from twitter'
consumer_secret= 'Consumer secret from twitter'

access_token='Access token from twitter'
access_token_secret='Access token secret from twitter'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

topic_name = "Election 2016"
#To find data for week 1
since_date = "2016-11-6"
until_date = "2016-11-12"

def get_label(analysis, threshold = 0):
	if analysis.sentiment[0]>threshold:
		return 'Positive'
	else:
		return 'Negative'

all_polarities = dict()
for topic_name in tweets:
	this_topic_polarities = []

	this_topic_tweets = api.search(q=[topic_name, topic], count=10000, since = since_date, until=until_date)

	with open('%s_tweets.csv' % topic, 'wb') as this_topic_file:
		this_topic_file.write('tweet,sentiment_label\n')
		for tweet in this_topic_tweets:
			analysis = TextBlob(tweet.text, pos_tagger=PatternTagger(), analyzer=PatternAnalyzer())


			this_topic_polarities.append(analysis.sentiment[0])
			this_topic_file.write('%s,%s\n' % (tweet.text.encode('utf8'), get_label(analysis)))


	all_polarities[topic] = np.mean(this_topic_polarities)
