import pickle
import json
import os
import urllib2

from pymongo import MongoClient

tmdb_key = os.environ['tmdb_key']
client = MongoClient()
db = client.mydb

worst_movies = db.worst_movies.find()
# bad_movies = db.bad_movies.find()

def request_movie_info(movie_id, api_key):
	# video_url = "http://api.themoviedb.org/3/movie/"
	# video_url += str(movie_id) + "/videos?"
	# video_url += "api_key=" + api_key
	# video_req = json.load(urllib2.urlopen(video_url))

	# casts_url = "http://api.themoviedb.org/3/movie/"
	# casts_url += str(movie_id) + "/casts?"
	# casts_url += "api_key=" + api_key
	# casts_req = json.load(urllib2.urlopen(casts_url))

	# return video_req, casts_req

	img_url = "http://api.themoviedb.org/3/movie/"
	img_url += str(movie_id) + "/images?"
	img_url += "api_key=" + api_key
	img_req = json.load(urllib2.urlopen(img_url))

	return img_req

for i in range(worst_movies.count()):
	tmdb_id = worst_movies[i]['id']
	img_dict = request_movie_info(tmdb_id, tmdb_key)

# 	video_dict, casts_dict = request_movie_info(tmdb_id, tmdb_key)
	db.worst_movies.update({'id': tmdb_id}, {"$push": {'images': img_dict}})
	print "updated movie info for", worst_movies[i]['title']
# 	

# for i in range(bad_movies.count()):
# 	tmdb_id = bad_movies[i]['id']
# 	# video_dict, casts_dict = request_movie_info(tmdb_id, tmdb_key)
# 	# db.bad_movies.update({'id': tmdb_id}, {"$push": {"videos": video_dict, "casts": casts_dict}})
# 	img_dict = request_movie_info(tmdb_id, tmdb_key)
# 	db.bad_movies.update({'id': tmdb_id}, {"$push": {'images': img_dict}})

	# print "updated movie info for", bad_movies[i]['title']
