import os
import json
import urllib2
import pickle

from pymongo import MongoClient

tmdb_key = os.environ['tmdb_key']
client = MongoClient()
db = client.mydb


with open('tmdb_ids.txt', 'rb') as f:
	tmdb_ids = pickle.load(f)

print type(tmdb_ids)

for movie_id in tmdb_ids:
	if movie_id:
		tmdb_url = "http://api.themoviedb.org/3/movie/"
		tmdb_url += str(movie_id)
		tmdb_url += "?api_key="
		tmdb_url += str(tmdb_key)

		req = json.load(urllib2.urlopen(tmdb_url))
		print req
		db.worst_movies.insert(req)


# f = open("tmdb_ids.txt", 'r')
# movie_list = f.read()
# movie_list = json.loads(movie_list)
# print movie_list