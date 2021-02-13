# -*- coding: UTF-8 -*-

# Import Twitter and Credentials class from Twitter module
from Twitter import Twitter
from Credentials import Credentials

# Instance of Credentials class with credential file as parameter
credentials = Credentials('credentials.csv')

# Instance of Twitter class with authentication stuff
twitter = Twitter(
    consumer_key = credentials.CONSUMER_KEY(),
    consumer_secret = credentials.CONSUMER_SECRET(),
    access_token = credentials.ACCESS_TOKEN(),
    access_token_secret = credentials.ACCESS_TOKEN_SECRET()
)

# Get a .csv file with the last 10 tweets about the keyword
keyword = 'vacina'
twitter.get_tweets_by_keyword(keyword)