from tweepy import API, OAuthHandler, Stream, TweepError
from tweepy.streaming import StreamListener
import json
from random import choice
consumer_key = 'your consumer key'
consumer_secret = 'your consumer secret'
access_token = 'your access token'
access_token_secret = 'your access token secret'
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = API(auth)

class StdOutListener(StreamListener):
    def on_data(self, data):
        if 'retweeted_status' in data:
            return True
        else:
            tweet = json.loads(data.strip())       
            text = tweet.get('text')
            id_str = tweet.get('user').get('screen_name')
            reply_status = tweet.get('id_str')
            text_list = text.split()
            result_list = list()
            for item in text_list:
                if item[0] != '@':
                    result_list.append(item)
            result = choice(result_list)
            api.update_status(status = "@%s %s"%(id_str, result), in_reply_to_status_id = reply_status)
            return True
    
if __name__ == '__main__':
    
    #main function
    
    Listener = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, Listener)
    stream.filter(track=['account_name'])
