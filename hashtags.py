import csv
import tweepy
# import pandas as pd
# Open/Create a file to append data
# csvFile = open('WiT.csv', 'a')
# #Use csv Writer
# csvWriter = csv.writer(csvFile)

def get_hashtags():
    for tweet in tweepy.Cursor(api.search,q="#womenintech",lang="en").items():
        print(tweet.created_at, tweet.text)
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
