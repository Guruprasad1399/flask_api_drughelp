# importing all the necessary modules.
import os
from dotenv import load_dotenv
from pytwitter import Api
import json
import pandas as pd

# Calling the load_dotenv function to get the env files.
load_dotenv()

# Getting the api keys and access_token from the .env file !
consumer_key = os.environ["TWITTER_CONSUMER_KEY"]
consumer_secret = os.environ["TWITTER_CONSUMER_SECRET"]
access_token = os.environ["TWITTER_ACCESS_TOKEN"]
access_token_secret = os.environ["TWITTER_ACCESS_TOKEN_SECRET"]
bearer_token = os.environ["TWITTER_BEARER_TOKEN"]

api = Api(bearer_token)

tweets_Data=[]

for i in range(100):
    tweets = api.search_tweets(query="lang:en Drug help",max_results=100,return_json=True)
    for tweet in tweets['data']:
        tweets_Data.append(tweet)
    
json_data = json.dumps(tweets_Data)

# Save the JSON data to a file
with open('tweet_data.json', 'w') as f:
    f.write(json_data)