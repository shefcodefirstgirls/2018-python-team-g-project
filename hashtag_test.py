import csv 
import tweepy 
from flask.json import jsonify
import json
# import pandas as pd 
# Open/Create a file to append data 
# csvFile = open('WiT.csv', 'a') 
# #Use csv Writer 
# csvWriter = csv.writer(csvFile) 

def authenticate(consumer_key, consumer_secret, access_token, access_token_secret):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    return tweepy.API(auth)

def show_content(tweets):
    for tweet in tweets:
        print("\n" + tweet.text)

def collect_tweets(keyword, stop_num, twitter):
    keyword = keyword.strip()
    print('Finding tweets with {} keyword'.format(keyword))
    tweets = twitter.search(keyword, limit=stop_num)
    show_content(tweets)

def get_hashtags(api): 
	locations = []
	j_tweets = []
	all_tweets = tweepy.Cursor(api.search,q="#womenintech",lang="en").items(100)
	for tweet in all_tweets:
		content = tweet.created_at
		text = tweet.text
		user = tweet.user.screen_name
		user = tweet.user.location
		user = tweet.user.time_zone
		location = tweet.location if hasattr(tweet, 'location') else "Undefined location"
		place = tweet.place if hasattr(tweet, 'place') else "Undefined place"
		place = getattr(tweet, 'place', "Undefined place")


		locations.append(str(user)) 
		# return place
		j_tweets.append(tweet._json)
	
	# return jsonify({'locations': locations})
	return json.dumps(j_tweets)

	# print(tweet.get('user', {}).get('location', {}))
        # csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')]) 
 
#https://api.twitter.com/1.1/search/tweets.json?q=%23womenintech

# location = API.search(q,) 
# return r.json()["location"] 
# https://api.twitter.com/1.1/search/tweets.json?q=%23womenintech&src=typd 
# user.derived.locations.locality 
# user.derived.locations.region 
# User.derived.locations.geo 
# 
# # app actions?? 
# https://developer.twitter.com/en/docs/tweets/enrichments/overview/profile-geo 
# https://developer.twitter.com/en/docs/tweets/rules-and-filtering/overview/all-operators 