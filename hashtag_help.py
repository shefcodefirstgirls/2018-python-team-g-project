import csv
import tweepy
# import pandas as pd

def show_content(tweets):
    for tweet in tweets:
        print("\n" + tweet.text)

def collect_tweets(keyword, stop_num, twitter):
    keyword = keyword.strip()
    print('Finding tweets with {} keyword'.format(keyword))
    tweets = twitter.search(keyword, limit=stop_num)
    show_content(tweets)

# def get_hashtags(api):
# 	locations = []
# 	all_tweets = tweepy.Cursor(api.search,q="#womenintech",lang="en").items(1)
# 	for tweet in all_tweets:
# 		content = tweet.created_at
# 		text = tweet.text
# 		location = tweet.location if hasattr(tweet, 'location') else "Undefined location"
# 		# location = api.search(q,)
# 		# return r.json()["location"]
# 		locations.append(location)
# 		return locations
        # csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
