from flask import Flask, render_template

import tweepy
import keys

app = Flask(__name__)

auth = tweepy.OAuthHandler(keys.getConsumerkey(),keys.getConsumerSecret())

auth.set_access_token(keys.getAccessToken(),keys.getAccessSecret())

api = tweepy.API(auth)

user_name = "UserName"
followersList = []

try:
	for follower in tweepy.Cursor(api.followers, screen_name= user_name).items():
		followersList.append(follower.screen_name)
except Exception as e:
	print(e)

print(followersList)

#Decorator
@app.route('/')
def index():
	return render_template("index.html")

if(__name__ == "__main__"):
	app.run(debug = True)