from flask import Flask, render_template

import tweepy
import keys

app = Flask(__name__)

auth = tweepy.OAuthHandler(keys.getConsumerkey(),keys.getConsumerSecret())

auth.set_access_token(keys.getAccessToken(),keys.getAccessSecret())

api = tweepy.API(auth)

followersList = api.followers_ids("718946692")

for follower in followersList:
	userdetails = api.get_user(follower)
	print(userdetails.screen_name)

#Decorator
@app.route('/')
def index():
	return render_template("index.html")

if(__name__ == "__main__"):
	app.run(debug = True)