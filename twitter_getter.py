#modified from http://adilmoujahid.com/posts/2014/07/twitter-analytics/

#tweepy methods for accessing the streaming API
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

access_token =
access_token_secret =

consumer_key =
consumer_secret = 

#Basic listner that prints tweets to stdout
class StdOutListner(StreamListener):

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status

if __name__ == '__main__':

    #Handle Twitter authentification adn the connection to Twitter Streaming API
    l = StdOutListner()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filters Twitter SStreams to capture data by the key words
    stream.filter(track=['python','javascript','ruby'])
