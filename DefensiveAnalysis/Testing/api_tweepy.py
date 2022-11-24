from email import header
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


#autenticacion

auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True)

try: 
    api.verify_credentials()
    print("Conectado")
except:
    print("No se conecto!!")
    
    
# calling the api 
api = tweepy.API(auth)

my_time = api.home_timeline()
#print(my_time)

columns = set()
allowed_type = [str, int]

for status in my_time:
    #print(status.text)
    #print(vars(status))

    keys = vars(status).keys()
    for k in keys:
        #print(k)
        columns.add(k)
#print(columns)

header_cols = list(columns)

df = pd.DataFrame(tweets_data, columns=header_cols)