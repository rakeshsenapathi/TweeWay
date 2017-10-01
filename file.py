import tweepy
import keys2
import time
import random
import simplejson as json
import csv

auth = tweepy.OAuthHandler(keys2.getConsumerkey(), keys2.getConsumerSecret())

auth.set_access_token(keys2.getAccessToken(), keys2.getAccessSecret())

api = tweepy.API(auth)

follower_list = []

# mCursor = tweepy.Cursor(api.followers_ids, id="easynhx", count=5000).items()

try:
	for follower in tweepy.Cursor(api.followers_ids, id="easynhx", count=5000).items():
		follower_list.append(str(follower))

except tweepy.TweepError:
	print("Rate Limit exceeded")

print(random.choice(follower_list))

	 	



           