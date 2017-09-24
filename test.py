from flask import Flask, render_template, request

import tweepy
import keys
import time
import simplejson as json

app = Flask(__name__)

ret_value = []

auth = tweepy.OAuthHandler(keys.getConsumerkey(), keys.getConsumerSecret())

auth.set_access_token(keys.getAccessToken(), keys.getAccessSecret())

api = tweepy.API(auth)

mRetweetId = "https://twitter.com/Zellsis/status/893128165387894784"

mCursor = tweepy.Cursor(api.retweeters, id=mRetweetId, count=200).items()

while True:
	try:
		ret_value.append(mCursor.next())

	except tweepy.TweepError:
		print("Rate Limit! . Sleeping for 15 minutes...")
		time.sleep(60 * 15)
		ret_value.append(mCursor.next())
	except StopIteration:
		break
print(ret_value)




