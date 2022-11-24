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
        print(status.user.screen_name + ": " + status.text)

        #if len(self.tweets) == self.limit:
         #   self.disconnect()

stream_tweet = Linstener(api_key, api_key_secret, access_token, access_token_secret)

users = [   'USRAmenaza',
            'USRAmenaza2',
            'USRAmenaza3']
user_ids = []

for user in users:
    user_ids.append(api.get_user(screen_name=user).id)
stream_tweet.filter(
                            #   follow=['USRAmenaza', 'USRAmenaza2']
                            #   locations=[] 
    
    follow=user_ids,
    )
    

#create DataFrame

columns = ['User', 'Tweet']
data = []

for tweet in stream_tweet.tweets:
    if not tweet.truncated:
        data.append([tweet.user.Owner_screen_name, tweet.text ])
    else:
        data.append([tweet.user.Owner_screen_name, tweet.extended_tweet['full_text']])

df = pd.DataFrame(data, columns=columns)

print(df)