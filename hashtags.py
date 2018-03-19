import csv
import tweepy
import config

#searchterm="#ShefCodeFirst"
#print("searchterm loaded from code")

def authenticate(consumer_key, consumer_secret, access_token, access_token_secret):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    return tweepy.API(auth)

def get_hashtags(api):
    # searchterm = hashtagcheck(searchterm)
    csvFile = open('tweets.csv', 'a')
    csvWriter = csv.writer(csvFile)
    search_hashtag = tweepy.Cursor(api.search,q=searchterm).items()
    for tweet in search_hashtag:
        return csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8'), tweet.user.location.encode('utf-8'),tweet.user.time_zone,tweet.place,tweet.coordinates])
#        csvFile.close()
        print(tweet.user.location)

# def get_hashtags(api):
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
