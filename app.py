from flask import Flask, render_template, request

import tweepy
import keys
import time
import simplejson as json

app = Flask(__name__)

followersList = []
follower = []


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/receiveName', methods=['POST'])
def receiveName():
    mReceivedName = request.get_data()

    auth = tweepy.OAuthHandler(keys.getConsumerkey(),keys.getConsumerSecret())

    auth.set_access_token(keys.getAccessToken(),keys.getAccessSecret())
    api = tweepy.API(auth)

    mCursor = tweepy.Cursor(api.followers, screen_name = mReceivedName, count=200).items()
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

@app.route('/show')
def show():
    return render_template('followers.html', followersList = followersList)

    

if(__name__ == "__main__"):
    app.run(debug = True)
