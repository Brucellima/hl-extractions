# -*- coding: UTF-8 -*-

import pandas as pd

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