import csv
import cgi
import tweepy
from helpers import hashtagcheck
# import pandas as pd

# Open/Create/write a file to append data
csvFile = open('WiT.csv', 'a')
csvWriter = csv.writer(csvFile)

# form=web.input()
# print form.searchbox

form=cgi.FieldStorage()
searchterm = form.getvalue('searchbox')

def get_hashtags():
    searchterm = hashtagcheck()
    search_hashtag = tweepy.Cursor(api.search,q=searchterm,lang="en").items()
    for tweet in search_hashtag:
        return csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
        # print (tweet.user.location.encode('utf8'))#, tweet.created_at, tweet.text)
        # # print json.dumps(tweet, json.dumps(trends,ident=1))
        # print(searchterm)
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
