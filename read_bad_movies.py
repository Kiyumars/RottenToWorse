import pickle
import json
import os
import urllib2
#from urllib2 import urlopen
rt_key = os.environ['rt_key']

with open("bad_movies_rt_ids.txt", "rb") as f:
	rt_id_list = pickle.load(f)

imdb_ids = []
for rt_id in rt_id_list:
	url = "http://api.rottentomatoes.com/api/public/v1.0/movies/"
	url += rt_id
	url += ".json?apikey=" + rt_key
	req = json.load(urllib2.urlopen(url))
	try:
		imdb_ids.append(req['alternate_ids']['imdb'])
		print req['title']
	except KeyError:
		continue

with open("bad_movies_imdb_ids.txt", "wb") as f:
	pickle.dump(imdb_ids, f)



