import os
import tweepy
from graphiql_request import get_profiles
from hashtag_test import authenticate, get_hashtags
from flask import Flask, render_template, request
from geocoding_tweets import shorten_json, geolocate_tweet, get_all_markers
from flask.json import jsonify

import config #delete before deployment, but need it for local testing

consumer_key = os.environ["twitter_consumer_key"]
consumer_secret = os.environ["twitter_consumer_secret"]
access_token = os.environ["twitter_access_token"]
access_token_secret = os.environ["twitter_access_token_secret"]

app = Flask("teamg_app")

# short_json = open("test_tweets.json")


@app.route("/")
def home():
    return render_template("index.html")

@app.route('/search',methods=['POST'])
def search():
    searchterm=request.form['searchbox']
    return render_template("hashtags.html", searchterm=searchterm)

@app.route("/about") #from kat
def about():
    profiles = get_profiles()
    return render_template("about.html", members=profiles, enumerate=enumerate)

@app.route("/hashtags/<searchterm>",methods=['GET'])
def hashtags(searchterm="#sheftechwomen"):
	# searchterm=searchterm
	# print(searchterm)
	api = authenticate(consumer_key, consumer_secret, access_token, access_token_secret)
	tweets= get_hashtags(api, searchterm, 10)
	# tweets = collect_tweets("#sheffield", 10, api)
    short_json = shorten_json(tweets)
    loc_json = geolocate_tweet(short_json)
	# return short_json
	# return loc_json #doesnt want to return a list
    # print(searchterm)
    return jsonify({"markers": [tweet for i, tweet in enumerate(loc_json)]})

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
