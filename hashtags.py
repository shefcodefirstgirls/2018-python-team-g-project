import csv
import cgi
import tweepy
from helpers import hashtagcheck
#from hashtag_help import collect_tweets, show_content
# import pandas as pd

searchterm = ["#shefcodefirst",]
print(searchterm)

def authenticate(consumer_key, consumer_secret, access_token, access_token_secret):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    return tweepy.API(auth)

# Open/Create/write a file to append data
csvFile = open('WiT.csv', 'a')
csvWriter = csv.writer(csvFile)

# form=web.input()
# print form.searchbox

# form=cgi.FieldStorage()
# searchterm = form.getvalue('searchbox')

def get_hashtags():
    searchterm = hashtagcheck()
    search_hashtag = tweepy.Cursor(api.search,q=searchterm,lang="en").items(10)
    for tweet in search_hashtag:
        return csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])#,tweet.user.location.encode('utf8')])
        # show_content(tweets)
        print (tweet.user.location.encode('utf8'))#, tweet.created_at, tweet.text)
        # # print json.dumps(tweet, json.dumps(trends,ident=1))
        # print(searchterm)
# def get_hashtags():#api):
# 	locations = []
# 	all_tweets = tweepy.Cursor(api.search,q=searchterm,lang="en").items()
# 	for tweet in all_tweets:
# 		content = tweet.created_at
# 		text = tweet.text
# 		location = tweet.location
#         if hasattr(tweet, 'location')
#         # else "Undefined location"
# 		# location = api.search(q,)
# 		# return r.json()["location"]
#         locations.append(location)
#         return locations
#         csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
#         #,tweet.user.location.encode('utf8')])

# location = API.search(q,)
# return r.json()["location"]
# https://api.twitter.com/1.1/search/tweets.json?q=%23womenintech&src=typd
# user.derived.locations.locality
# user.derived.locations.region
# User.derived.locations.geo

# # app actions??
# https://developer.twitter.com/en/docs/tweets/enrichments/overview/profile-geo
# https://developer.twitter.com/en/docs/tweets/rules-and-filtering/overview/all-operators
