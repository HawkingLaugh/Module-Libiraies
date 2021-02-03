import sys
import tweepy
import os


CK = os.environ.get('CK')
CS = os.environ.get('CS')
AT = os.environ.get('AT')
ATS = os.environ.get('ATS')
auth = tweepy.OAuthHandler(CK, CS)

auth.set_access_token(AT,ATS)

api = tweepy.API(auth)

ids = []
for page in tweepy.Cursor(api.followers_ids, screen_name = 'NotToCryCryALot').pages():
    ids.append(page)

print(ids)