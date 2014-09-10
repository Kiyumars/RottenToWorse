import os
import json
import urllib2
import pickle

from StringIO import StringIO
from lxml import etree
import requests
from pymongo import MongoClient

base_url = "http://www.rottentomatoes.com/guides/worst_of_the_worst/"
tmdb_key = os.environ['tmdb_key']

rt_movie_ids =[] 
for i in range(1, 11):
	url = base_url + str(i) + "/"
	r = requests.get(url)
	content = r.content
	parser = etree.HTMLParser()
	tree = etree.parse(StringIO(content), parser)
	bad_movies = tree.xpath("//div[@class='details fl clearfix']/h1[@class='title']/a/@href")
	print bad_movies

	for movie_link in bad_movies:
		url = "http://www.rottentomatoes.com" + movie_link
		print url
		r = requests.get(url)
		content = r.content
		parser = etree.HTMLParser()
		tree = etree.parse(StringIO(content), parser)
		rt_id = tree.xpath("//meta[@name='movieID']/@content")
		print type(rt_id)
		rt_movie_ids.append(str(rt_id[0]))
		print str(rt_id[0])

with open("bad_movies_rt_ids.txt", "wb") as f:
	pickle.dump(rt_movie_ids, f)

