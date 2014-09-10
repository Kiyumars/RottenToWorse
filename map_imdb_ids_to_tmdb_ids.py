import pickle
import json
import os
import urllib2

tmdb_key = os.environ['tmdb_key']

with open("bad_movies_imdb_ids.txt", "rb") as f:
	imdb_id_list = pickle.load(f)

def parse_tmdb_request_for_tmdb_id(imdb_id):
	tmdb_url = "http://api.themoviedb.org/3/find/tt"
	tmdb_url += imdb_id + "?api_key=" + tmdb_key
	tmdb_url += "&external_source=imdb_id"
	print tmdb_url
	req = json.load(urllib2.urlopen(tmdb_url))
	print req
	try:
		return req['movie_results'][0]["id"]
	except IndexError:
		print "Did not find the movie on tmdb"
		return False

tmdb_ids = []
for imdb_id in imdb_id_list:
	tmdb_id = parse_tmdb_request_for_tmdb_id(imdb_id)
	if tmdb_id:
		tmdb_ids.append(tmdb_id) 

print len(tmdb_ids)

with open("bad_movies_tmdb_ids.txt", "w") as f:
	pickle.dump(tmdb_ids, f)