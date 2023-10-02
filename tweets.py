from __future__ import absolute_import, print_function
import csv

consumer_key= '0E3nQy1HE20wc4MFhjlzdcTNE'
consumer_secret= 'mV7XVWOwMDwAy9O2vXhhZZKtkF2lNrG75uNE5gnPqNmdh8DmSD'
access_token_key= '880134360-7lJUwslgfkMl14wfOdppNFounKGQ4v5GHdywA3j9'
access_token_secret= 'XQoEjeYmKkfAmMSEyjZhFrtnKrScTxHroORCKtVFznzDC'

import tweepy
from tweepy import OAuthHandler
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token_key, access_token_secret)
 
api = tweepy.API(auth)
user = api.me()
l=[]
import re
import sys 
import json
from pprint import pprint
#from textblob import TextBlob

kt={}

tweets= tweepy.Cursor(api.search,q="BJP",count=20,
                           lang="en").items(20)
for tweet in tweets:
	jtweet=tweet._json['text']
	l.append(jtweet)
	df = open('tweetcheck.csv','w',encoding="utf8")
	csv.writer(df).writerow(l)
	print(l)