import os
import tweepy
from graphiql_request import get_profiles
from hashtags import get_hashtags
import config #delete before deployment, but need it for local testing
from tweepy import Stream, OAuthHandler
import csv

consumer_key = os.environ["twitter_consumer_key"]
consumer_secret = os.environ["twitter_consumer_secret"]
access_token = os.environ["twitter_access_token"]
access_token_secret = os.environ["twitter_access_token_secret"]

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# @app.route("/feedback", methods=["POST"])
# def get_feedback():
#     data = request.values
#     return render_template("feedback.html", form_data=data)

#searchterm = ["#womenintech",]
#user input to gather hashtag to search??

from flask import Flask, render_template, request

app = Flask("teamg_app")

@app.route("/")
def home():
    return render_template("index.html")
# hashtags= get_hashtags()

@app.route("/about") #from kat
def about():
    profiles = get_profiles()
    return render_template("about.html", members=profiles, enumerate=enumerate)

"""
This piece of logic checks whether you are running the app locally or on Heroku
(make an account at https://www.heroku.com/ before the deployment session!). When
running the app on Heroku, the PORT environment/config variable is pre-populated by
Heroku to tell our app the correct port to run on.
"""
if "PORT" in os.environ:
    app.run(host="0.0.0.0", port=int(os.environ["PORT"]))
else:
    app.run(debug=True)
