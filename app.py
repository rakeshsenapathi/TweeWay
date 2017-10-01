from flask import Flask, render_template, request

import tweepy
import keys2
import simplejson as json
import random

app = Flask(__name__)

follower_list = []


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/receiveName', methods=['GET','POST'])
def receiveName():
    mReceivedName = request.get_data()

    auth = tweepy.OAuthHandler(keys2.getConsumerkey(), keys2.getConsumerSecret())

    auth.set_access_token(keys2.getAccessToken(), keys2.getAccessSecret())

    api = tweepy.API(auth)

    try:
        for follower in tweepy.Cursor(api.followers_ids, id = mReceivedName , count=5000).items():
            follower_list.append(str(follower))
    except tweepy.TweepError:
        print("Rate Limit exceeded")

    winner_id = random.choice(follower_list)
    winner_details = api.get_user(int(winner_id))
    winner_name = str(winner_details.screen_name)
    winner_img = str(winner_details.profile_image_url)
    return render_template('followers.html',
                            winner_name = winner_name,
                            winner_img = winner_img)


# @app.route('/show')
# def show():
#     return render_template('followers.html', winner_id=winner_id)


if(__name__ == "__main__"):
    app.run(debug=True)
