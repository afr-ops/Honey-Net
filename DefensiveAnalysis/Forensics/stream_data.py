import tweepy
import configparser
import json
import pandas as pd
import time 
import random
from time import sleep


# read configs
config = configparser.ConfigParser()
#config.read('config.ini')

api_key = "#################################"
api_key_secret = ""#################################""

access_token = "#################################"
access_token_secret = "#################################"


#autebnticacion

auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True)

try: 
    api.verify_credentials()
    print("Conectado")
except:
    print("No se conecto!!")
    
    
class Linstener(tweepy.Stream):

    tweets = [str, int]
    limit = 10

    def on_status(self, status):
        self.tweets.append(status)
        print(status.user.screen_name + ": " + status.text + ": " + status.source + ": ")

        if len(self.tweets) == self.limit:
            
            time.sleep(random.uniform(1, 3)) 
            self.disconnect()

stream_tweet = Linstener(api_key, api_key_secret, access_token, access_token_secret)

# Stream keywords HRL
keywords = [
                'Messi'
            ]

stream_tweet.filter(    track=keywords,                                   
                        languages=['es']
                        locations=[-75.4566721729,-56.3165690342,-51.4097993186,-18.6296379741]                           
)

#DataFrame__

columns = ['User', 'Tweet'] # ,  'geo', 'respuesta''url','Date',
data = []

for tweet in stream_tweet.tweets:
    if not tweet.truncated:
        data.append([tweet.user.screen_name, tweet.text])
    else:
        data.append([tweet.user.screen_name, tweet.extended_tweet['full_text']])

df = pd.DataFrame(data, columns=columns)



# df.to_csv('archivo.csv') 
# df.to_html('archivo.html') 
print(df)
