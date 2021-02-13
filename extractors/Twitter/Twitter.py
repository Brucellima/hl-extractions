# -*- coding: UTF-8 -*-

import tweepy
import pandas as pd

"""
    Class Twitter: connect to Twitter API through tweepy library

    -> PARAMS:
        - consumer_key: Twitter application consumer key
        - consumer_secret: Twitter application consumer secret
        - access_token: Twitter application access token
        - access_token_secret: Twitter application secret access token

    -> METHODS:
        - create_tweet: update authenticated user status
        - get_tweets_by_keyword: save a .csv file with the most recent tweets about a keyword
"""

"""
    Class Credentials: get application credentials from credentials.csv file.

    -> PARAMS:
        - credentials_file: path of the credentials.csv file
            -> DEFAULT: credentials.csv

    -> METHODS:
        - CONSUMER_KEY: returns application consumer key
        - CONSUMER_SECRET: returns application consumer secret
        - ACCESS_TOKEN: returns application access token
        - ACCESS_TOKEN_SECRET: returns application secret access token
"""

class Twitter:
    def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret):
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.access_token = access_token
        self.access_token_secret = access_token_secret

        authentication = tweepy.OAuthHandler(consumer_key, consumer_secret)
        authentication.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(authentication)

        print('==================== HL TWITTER TOOL ====================')
        print('Welcome to HL Twitter Tool v. 0.0.1\n')
        
        print('Authenticated user information:')
        authenticated_user = self.api.me()
        print('\tId: ' + authenticated_user.id_str)
        print('\tName: ' + authenticated_user.name)
        print('\tScreen name: @' + authenticated_user.screen_name + '\n')

        print('==================== LOG ====================')

    def create_tweet(self, tweet_text):
        print('- Tweet creation: ' + tweet_text)
        self.api.update_status(tweet_text)

    def get_tweets_by_keyword(self, keyword, limit=10, mode='recent'):
        print('- Searching tweets | Keyword: ' + keyword)
        tweets = tweepy.Cursor(
            self.api.search,
            q = keyword + ' exclude:retweets exclude:replies',
            lang = 'pt',
            tweet_mode = 'extended'
        ).items(5)

        print('Processing tweets...')
        
        with open('tweets.csv', 'w') as f:
            for i, tweet in enumerate(tweets):
                cleaned_tweet = tweet.full_text.strip().replace('\n','').encode('utf-8')
                print('\t[' + str(i+1) + '] ' + cleaned_tweet)
                buffer += cleaned_tweet + '\n'
            f.write(str(buffer))

        print('Tweet file saved successfull.')

class Credentials:

    def __init__(self, credentials_file='credentials.csv'):
        self.credentials_file = credentials_file
        self.credentials = pd.read_csv(credentials_file)

    def CONSUMER_KEY(self):
        consumer_key = self.credentials.loc[:,'consumer_key'].iloc[0]
        return consumer_key
    
    def CONSUMER_SECRET(self):
        consumer_secret = self.credentials.loc[:,'consumer_secret'].iloc[0]
        return consumer_secret

    def ACCESS_TOKEN(self):
        access_token = self.credentials.loc[:,'access_token'].iloc[0]
        return access_token

    def ACCESS_TOKEN_SECRET(self):
        access_token_secret = self.credentials.loc[:,'access_token_secret'].iloc[0]
        return access_token_secret