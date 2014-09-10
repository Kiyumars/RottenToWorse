from StringIO import StringIO
from lxml import etree
import requests
import pickle

actor_id_match = 'http://www.imdb.com/name/'
url = "http://www.imdb.com/list/ls051275456/"
r = requests.get(url)
content = r.content
parser = etree.HTMLParser()
tree = etree.parse(StringIO(content), parser)
actor_entries = tree.xpath("//div[@class='list detail']/div[@class='list_item odd' or @class='list_item even']/div[@class='info']/b/a/@href")

actor_ids = []
for name in actor_entries:
	actor_ids.append(name[len("/name/"):-1])

with open("actor_ids.txt", "w") as f:
	pickle.dump(actor_ids, f)