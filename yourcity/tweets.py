import tweepy
from textblob import TextBlob
from wordcloud import WordCloud
import pandas as pd
import numpy as np
import re

# read access token(s) from auth file
# Idea for futures: loop through different login files after limit exceeded
login = pd.read_csv('auth_twitter.csv')

# Auth definitions
consumer_key = login['consumer_key'].to_string(index=False)
consumer_secret = login['consumer_secret'].to_string(index=False)
# bearer = login['bearer']
access_token = login['access_token'].to_string(index=False)
access_secret = login['access_secret'].to_string(index=False)
authenticate = tweepy.OAuthHandler(consumer_key, consumer_secret)

# Define tweepy API
api = tweepy.API(authenticate, wait_on_rate_limit = True)

def auth():
    authenticate.set_access_token(access_token, access_secret)


def get_tweets(hashtag):
    # Extract 100 tweets from Bill grantAccess
    i = 1
    # posts = api.user_timeline(screen_name = "BillGates", count = 50, lang = "en", tweet_mode = "extended")
    posts = api.search_tweets(q = hashtag, lang = "en", count = 5)
    print("show the last 5 recent tweets")
    for tweet in posts [0:5]:
        print(str(i) + tweet.text + '\n')
        i = i + i
    
    return posts

def dummy():
    get_tweets('fahrrad')
    return 1


dummy()
