# -*- coding: utf-8 -*-
from tweepy import API
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy import TweepError
import json

consumer_key = 'your consumer key' #your consumer key here
consumer_secret = 'your consumer secret' #your consumer secret key here
access_token = 'your access token' #your access token here
access_token_secret = 'your access token secret' #your access token secret here

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = API(auth)

class StdOutListener(StreamListener):
    def on_data(self, data):
        tweet = json.loads(data.strip()
        print(data)
        text = tweet.get('text')
        retweeted_count = tweet.get('retweet_count')
        if "pic" in text and retweeted_count == 0:
            id_str = tweet.get('id_str')
            try:
                api.retweet(id_str)
            except TweepError as E:
                print(E)
        return True #if return False, then streaming stops, return True, streaming continues

if __name__ == "__main__":
    Listener = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, Listener) 
    stream.filter(track=['your_desired_word'])
