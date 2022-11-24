import tweepy
import configparser
import json
import pandas as pd


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

    tweets = []
    limit = 1

    def on_status(self, status):
        self.tweets.append(status)
        print(status.user.screen_name + ": " + status.text + ": " + status.source + ": ")

        #if len(self.tweets) == self.limit:
         #   self.disconnect()

stream_tweet = Linstener(api_key, api_key_secret, access_token, access_token_secret)

# stream keywords
keywords = [    
                'USR_de_busqueda',
                'USR_de_busqueda2',
                'USR_de_busqueda3'    
                
            ]

stream_tweet.filter(track=keywords,                                   
                   
                            #   follow=['USR_de_busqueda', 'USR_de_busqueda2']
                            #   locations=['coordenadas']                          
)      


#DataFrame languages=['es'], 

columns = ['User', 'Tweet', 'App', 'Date']
data = []

for tweet in stream_tweet.tweets:
    if not tweet.truncated:
        data.append([tweet.user.screen_name, tweet.text, tweet.status.source, tweet.created_at ])
    else:
        data.append([tweet.user.screen_name, tweet.extended_tweet['full_text'], tweet.status.source, tweet.created_at])

df = pd.DataFrame(data, columns=columns)

print(df)