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


# BUSQUEDA POR KEY /USR
keywords = [
                
                'Palabra o usr de tw'
                ]
limit=50

tweets = tweepy.Cursor(api.search_tweets, q=keywords, count=100, tweet_mode='extended').items(limit)

# DataFrame
columns = ['User', 'Tweet', 'App', 'Location', 'Date', 'Geo', 'Reply'] #  , 'Location', 'Date', 'Geo', 'Reply'
data = []

for tweet in tweets:
    data.append([tweet.user.screen_name, tweet.full_text, tweet.source, tweet.author.location, tweet.created_at, tweet.geo, tweet.in_reply_to_user_id])  #, tweet.author.location, tweet.created_at, tweet.geo, tweet.in_reply_to_user_id
    df = pd.DataFrame(data, columns = columns)
    usr = api.reverse_geocode(lat= '-34.59', long='-58.45')
    
print(df)
# df.to_html('usr_xxx.html')
