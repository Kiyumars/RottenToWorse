import sys
import logging
import random
import json
import urllib2
from bson.objectid import ObjectId

import tornado.ioloop
import tornado.web
import tornado.autoreload

# from rottentomatoes import RT
# import imdb
from pymongo import MongoClient

# tmdb_key = os.environ['tmdb_key']
client = MongoClient()
db = client.mydb


class MainHandler(tornado.web.RequestHandler):
	def get(self):
		bad_movie_list = db.bad_movies.find()
		worst_movie_list = db.worst_movies.find()
		bad_movie = find_movie_from_list(bad_movie_list)
		worst_movie = find_movie_from_list(worst_movie_list)

		self.render("index.html", bad_movie=bad_movie, worst_movie=worst_movie)

def find_movie_from_list(movie_list):
	useful_movie = False
	while not useful_movie and movie_list.count() > 0:
		movie = movie_list[random.randint(0, movie_list.count())]
		if not all(key in movie.keys() for key in ("casts", "videos")):
			continue
		useful_movie = True
		return movie


application = tornado.web.Application([
										(r"/", MainHandler)
										],
										debug=True,
										static_path='static')

if __name__ == "__main__":
	application.listen(8888)
	tornado.autoreload.start()
	tornado.ioloop.IOLoop.instance().start()