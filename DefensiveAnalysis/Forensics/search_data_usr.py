import tweepy
import configparser
import pandas as pd

# configs
config = configparser.ConfigParser()

api_key = "#################################"
api_key_secret = ""#################################""

access_token = "#################################"
access_token_secret = "#################################"

# authentication
auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True)

try: 
    api.verify_credentials()
    print("Conectado")
except:
    print("No se conecto!!")


# BUSQUEDA POR USR
user = 'usuario de tw'
limit = 1000
tweets = tweepy.Cursor(api.user_timeline, screen_name=user, count=200, tweet_mode='extended').items(limit)

# DataFrame
columns = ['User',  'App','Tweet', 'Date',  'Location', 'Geo', 'Reply_id'] # , 'respuesta''url',
data = []

for tweet in tweets:
    data.append([tweet.user.screen_name, tweet.source, tweet.full_text, tweet.created_at, tweet.author.location, tweet.geo, tweet.in_reply_to_user_id])  # tweet.author.url, place , 
    df = pd.DataFrame(data, columns = columns)

df.to_html('usuario_de_tw.html') 
print(df)

