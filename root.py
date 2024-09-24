import tweepy
import os
from datetime import  date, datetime, timedelta
from json import dumps
consumer_key = os.environ['TWITTER_API_KEY']
consumer_secret = os.environ['TWITTER_API_SECRET_KEY']
access_token = os.environ['TWITTER_ACCESS_TOKEN']
access_token_secret = os.environ['TWITTER_ACCESS_TOKEN_SECRET']
client = tweepy.Client(consumer_key=consumer_key,
                    consumer_secret=consumer_secret,
                    access_token=access_token,
                    access_token_secret=access_token_secret)
now = datetime.now()
target_date = datetime(2024, 9, 27)
difference = target_date - now
hours = difference.total_seconds() / 3600
hrs = round(hours) - 3
message = f"All Hail the Tiger. {hrs} Hours to go. #Devara "
cd = dumps(message)
response = client.create_tweet(text=cd)
