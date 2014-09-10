import pickle
import json
import os
import urllib2

from pymongo import MongoClient

tmdb_key = os.environ['tmdb_key']
client = MongoClient()
db = client.mydb

with open("bad_movies_tmdb_ids.txt", "rb") as f:
	tmdb_id_list = pickle.load(f)

for tmdb_id in tmdb_id_list:
	if tmdb_id:
		tmdb_url = "http://api.themoviedb.org/3/movie/"
		tmdb_url += str(tmdb_id)
		tmdb_url += "?api_key="
		tmdb_url += str(tmdb_key)

		req = json.load(urllib2.urlopen(tmdb_url))
		print req
		db.bad_movies.insert(req)