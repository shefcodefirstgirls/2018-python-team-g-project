import json
import sys
from pygeocoder import Geocoder
from geopy.geocoders import Nominatim
from flask.json import jsonify
from flask import Flask

app = Flask(__name__)

def shorten_json(json_file):
	short_json = []

	# # file with json text saved
	# with open(json_file) as f:
	# 		j = json.load(f)
	# 		# json.dump(j, sys.stdout, indent = 2)
	# 		for i, item in enumerate(j):
	# 			entry = {'created_at': item['created_at'], 'id_str': item['id_str'], 'text': item['text'], 'hashtags': item['entities']['hashtags'], 'name': item['user']['name'], 'screen_name': item['user']['screen_name'], 'location': item['user']['location'], 'time_zone': item['user']['time_zone'], 'coordinates': item['coordinates'], 'retweet_count': item['retweet_count'], 'favorite_count': item['favorite_count'] }
	# 			short_json.append(entry)

	#variable
	j = json.loads(json_file)
	for i, item in enumerate(j):
		entry = {'created_at': item['created_at'], 'id_str': item['id_str'], 'text': item['text'], 'hashtags': item['entities']['hashtags'], 'name': item['user']['name'], 'screen_name': item['user']['screen_name'], 'location': item['user']['location'], 'time_zone': item['user']['time_zone'], 'coordinates': item['coordinates'], 'retweet_count': item['retweet_count'], 'favorite_count': item['favorite_count'] }
		short_json.append(entry)

	return short_json


def geolocate_tweet(json_file):
	geolocator = Nominatim()
	short_json = json_file
	result = []
	for i, item in enumerate(short_json):
		# tweet_coordinates = item['coordinates']
		tweet_location = item['location']
		tweet_timezone = item['time_zone']
		# if tweet_coordinates != None:
			
		# 	print("coordinates")
		# 	print(tweet_coordinates)
		# 	break
		# 	# location = geolocator.geocode(tweet_coordinates)
		# 	# print(location.address)
		# 	# print(location.latitude, location.longitude)
		if tweet_location != "":
			# print("location")
			# print(tweet_location)
			location = geolocator.geocode(tweet_location, timeout = 1)
			if location != None:
				item['address'] = location.address
				item['lng'] = location.longitude
				item['lat'] = location.latitude
				result.append(item)
				continue
			# print(location.address)
			# print(location.latitude, location.longitude)
		if tweet_timezone != None:
			# print("timezone")
			# print(tweet_timezone)
			location = geolocator.geocode(tweet_timezone, timeout = 1)
			print(location)
			if location != None:
				item['address'] = location.address
				item['lng'] = location.longitude
				item['lat'] = location.latitude
				result.append(item)
				continue
			# print(location.address)
			# print(location.latitude, location.longitude)
	return result

@app.route("/api/tweets")
def get_all_markers(json_file):
    markers = json_file
    return markers
# @app.route("/api/drugs")
# def get_all_drugs():
#     drugs = Drug.query.all()
#     return jsonify({"drugs": [drug.name for drug in drugs]})


# short_json = shorten_json("test_tweets.json")
# short_json = geolocate_tweet(short_json)

# # pretty printing
# json.dump(short_json, sys.stdout, indent = 2)
