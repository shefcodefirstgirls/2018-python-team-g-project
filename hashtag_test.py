import csv 
import tweepy 
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
	all_tweets = tweepy.Cursor(api.search,q="#womenintech",lang="en").items(1)
	for tweet in all_tweets:
		content = tweet.created_at
		text = tweet.text
		location = tweet.location if hasattr(tweet, 'location') else "Undefined location"
		# location = api.search(q,) 
		# return r.json()["location"]
		locations.append(location) 
		return locations
        # csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')]) 
 
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