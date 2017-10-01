import tweepy
import keys
import simplejson as json
import random

auth = tweepy.OAuthHandler(keys.getConsumerkey(), keys.getConsumerSecret())

auth.set_access_token(keys.getAccessToken(), keys.getAccessSecret())
api = tweepy.API(auth)

follower_list = []

try:
	for follower in tweepy.Cursor(api.followers_ids, id="rakeshsenapathi", count=5000).items():
            follower_list.append(str(follower))

except tweepy.TweepError:
	print("Rate Limit exceeded")
        
winner_id = random.choice(follower_list)

winner_details = api.get_user(int(winner_id))
print(winner_details.screen_name)
print(winner_details.profile_image_url)