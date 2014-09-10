import os
import json
import urllib2
import pickle

from StringIO import StringIO
from lxml import etree
import requests
from pymongo import MongoClient()

imdb_match = 'http://www.imdb.com/title/'
url = "http://en.wikipedia.org/wiki/List_of_films_with_a_0%25_rating_on_Rotten_Tomatoes"
tmdb_key = os.environ['tmdb_key']
r = requests.get(url)
content = r.content
parser = etree.HTMLParser()
tree = etree.parse(StringIO(content), parser)
column = tree.xpath("//div[@class='div-col columns column-count column-count-2']/ul/li/i/a/@href")

def parse_tmdb_request_for_tmdb_id(imdb_id):
	tmdb_url = "http://api.themoviedb.org/3/find/" + imdb_id + "?api_key=" + tmdb_key + "&external_source=imdb_id"
	req = json.load(urllib2.urlopen(tmdb_url))
	try:
		return req['movie_results'][0]["id"]
	except IndexError:
		print "Did not find the movie on tmdb"

wiki_links = []
for link in column:
	wiki_links.append("http://en.wikipedia.org" + link)

imdb_ids = []
for page in wiki_links:
	req = requests.get(page)
	wiki_content = req.content
	wiki_tree = etree.parse(StringIO(wiki_content), parser)

	imdb_links = wiki_tree.xpath("//div[@id='mw-content-text']/ul/li/a[@class='external text']/@href")
	
	for i in range(len(imdb_links)):
		if imdb_links[i].startswith(imdb_match):
			imdb_ids.append(imdb_links[i][len(imdb_match): -1])


tmdb_ids = []
for imdb_id in imdb_ids:
	tmdb_id = parse_tmdb_request_for_tmdb_id(imdb_id)
	tmdb_ids.append(tmdb_id)

with open("tmdb_ids.txt", "w") as f:
	pickle.dump(tmdb_ids, f)
	
# f = open("tmdb_ids.txt", "w")
# f.write(str(tmdb_ids))





