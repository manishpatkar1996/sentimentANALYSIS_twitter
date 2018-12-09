# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 02:57:34 2018

@author: MANISH PATKAR
"""

from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import senti as s

#consumer key, consumer secret, access token, access secret.
ckey="VOPVIExPhQsPhs6GUEU0WpKWO"
csecret="OYKzv48M97nrMrtZXkd0ATrwA4FNNQRRn7xogtnz4z9WA9YU1T"
atoken="2807065872-lMvfJzjYGHiDUkcB3ZAMtID3Ebd66udBuYCTd7D"
asecret="KV4njzTWFHrX5L0h4kjk1eL9Lq6haKbM6Olxv4QS47566"

#from twitterapistuff import *

class listener(StreamListener):
    
    def on_data(self, data):
        

	    all_data = json.loads(data)

	    tweet = all_data["text"]
	    sentiment_value, confidence = s.sentiment(tweet)
	    print(tweet, sentiment_value, confidence)

	    if confidence*100 >= 80:
	    	output = open("twitter-out.txt","a")
	    	output.write(sentiment_value)
	    	output.write('\n')
	    	output.close()

	    return True

    def on_error(self, status):
        print(status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["happy"])