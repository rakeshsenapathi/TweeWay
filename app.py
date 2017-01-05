from flask import Flask, render_template

import tweepy
import keys
import time

app = Flask(__name__)

auth = tweepy.OAuthHandler(keys.getConsumerkey(), keys.getConsumerSecret())

auth.set_access_token(keys.getAccessToken(), keys.getAccessSecret())

api = tweepy.API(auth)

followersList = []
follower = []

user_name = "username"

mCursor = tweepy.Cursor(api.followers, screen_name = user_name, count=200).items()

while True:
    try:
        follower = mCursor.next()
        followersList.append(follower.screen_name)
    except tweepy.TweepError:
        print("Rate Limit! . Sleeping for 15 minutes...")
        time.sleep(60 * 15)
        follower = mCursor.next()
        followersList.append(follower.screen_name)
    except StopIteration:
        break

if(len(followersList)):
	print("Printing %d follower ids"%len(followersList))
	print(followersList)
