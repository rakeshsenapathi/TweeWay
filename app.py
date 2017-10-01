from flask import Flask, render_template, request

import tweepy
import keys
import simplejson as json
import random

app = Flask(__name__)

winner_id = []


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/receiveName', methods=['POST'])
def receiveName():
    mReceivedName = request.get_data()

    auth = tweepy.OAuthHandler(keys.getConsumerkey(), keys.getConsumerSecret())

    auth.set_access_token(keys.getAccessToken(), keys.getAccessSecret())
    api = tweepy.API(auth)

    try:
        for follower in tweepy.Cursor(api.followers_ids, id="easynhx", count=5000).items():
            follower_list.append(str(follower))
    except tweepy.TweepError:
        print("Rate Limit exceeded")

    winner_id = random.choice(follower_list)
    
@app.route('/show')
def show():
    json_followers = json.dumps(followersList)
    return render_template('followers.html', winner_id = winner_id ) 

if(__name__ == "__main__"):
    app.run(debug = True)
